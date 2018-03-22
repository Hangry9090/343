/**************************************
* This is the parser for
* the language Zoomjoystrong
* 
* @author Marshal Brummel
* @version 3.11.2018
***************************************/

%{ 
	
	#include <stdio.h>
	#include <string.h>
	#include "zoomjoystrong.h"
	void yyerror(const char* ch);
	int yylex();

%}

%error-verbose
%start statement

%union {int i; double d;}

%token END
%token END_STATEMENT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token <i> INT
%token <d> FLOAT
%token ERROR


%%

statement: term end
	|	term statement
;

term: end
	|	point
	|	line
	|	circle
	|	rectangle
	|	set_color
;

end: END END_STATEMENT
	{finish();exit(1);}


point: POINT INT INT END_STATEMENT
	{
		//Checks to see if number are within the range of the screen
		if($2 < 0 || $2 > HEIGHT){
			printf("The first number is not within the screen.");
		}
		else if($3 < 0 || $3 > HEIGHT) {
			printf("The second number is not within the screen.");
		}
		else {
			point($2, $3);
		}
	}
;

line: LINE INT INT INT INT END_STATEMENT
	{	
		//Checking to see if the numbers are on the screen
		if($2 < 0 || $2 > WIDTH) {
			printf("The first number is not within the screen.");
		}
		else if($3 < 0 || $3 > HEIGHT) {
			printf("The second number is not within the screen.");
		}
		else if($4 < 0 || $4 > WIDTH){
			printf("The third number is not within the screen.");
		}
		else if($5 < 0 || $5 > WIDTH) {
			printf("The fourth number is not within the screen.");
		} 
		else {
			line($2, $3, $4, $5);
		}
	}
;

circle: CIRCLE INT INT INT END_STATEMENT
	{
		//Checking if numbers are within bounds
		if($2 < 0 || $2 > WIDTH) {
			printf("The first number is not within the screen.");
		}
		else if($3 < 0 || $3 > HEIGHT) {
			printf("The second number is not within the screen.");
		}
		else if($2 + $4 > WIDTH || $2 - $4 < 0) {
			printf("Part of the circle will appear off the screen");

		}
		else if($3 + $4 > HEIGHT || $3 - $4 < 0) {
			printf("Part of the circle will appear off the screen.");
		}
		else {
			circle($2, $3, $4); 
		}
	}
;

rectangle: RECTANGLE INT INT INT INT END_STATEMENT
	{
		//Checking to see if numbers are within bounds
		if($2 < 0 || $2 > WIDTH) {
			printf("The first number is not within the screen.");
		}
		else if($2 < 0 || $2 > HEIGHT) {
			printf("The first number is not within the screen.");
		}
		else if($3 < 0 || $3 > WIDTH){
			printf("The second number is not within the screen.");
		}
		else if($3 < 0 || $3 > WIDTH) {
			printf("The second number is not within the screen.");
		} 
		else if($4 < 0 || $4 > WIDTH) {
			printf("The third number is not within the screen.");
		}
		else if($4 < 0 || $4 > HEIGHT) {
			printf("The third number is not within the screen.");
		}
		else if($5 < 0 || $5 > WIDTH){
			printf("The fourth number is not within the screen.");
		}
		else if($5 < 0 || $5 > WIDTH) {
			printf("The fourth number is not within the screen.");
		} 
		else {
			rectangle($2, $3, $4, $5);
		}
	}
;

set_color: SET_COLOR INT INT INT END_STATEMENT
	{
		//Checking to see if numbers are within bounds
		if($2 < 0 || $2 > 255 || $3 < 0 || $3 > 255 || $4 < 0 || $4 > 255) {
			printf("All RGB values must be between 0 and 255.");
		}
		set_color($2, $3, $4);
	}


%%


/*********************************************
* The method that starts the parsing.
* 
* @param argc int
@ @param argv char**
* @return 0
*********************************************/
int main(int argc, char** argv) {
	setup();
	printf("Welcome!\n");
	yyparse(); //Starts the parsing
	return 0;
}

/*********************************************
* The method that runs once an error occurs.
* 
* @param ch const char*
**********************************************/
void yyerror(const char* ch) {
	printf("Command entered caused an error. Code: %s\n", ch);
	yyparse(); //Continues parsing after the error
}


