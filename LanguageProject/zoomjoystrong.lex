%{
	#include <stdio.h>
	#include <string.h>
	#include "zoomjoystrong.tab.h"
%}

%option noyywrap

%%

(end) 		{return END;}
;		{return END_STATEMENT;}
(point) 	{return POINT;}
(line) 		{return LINE;}
(circle) 	{return CIRCLE;}
(rectangle) 	{return RECTANGLE;}
(set_color) 	{return SET_COLOR;}
[0-9]+ 		{yylval.i = atoi(yytext); return INT;}
[0-9]+\.[0-9]* 	{yylval.d = atof(yytext); return FLOAT;}
[ \t\n]   	;
[a-zA-Z]+ |
[:punct:]+	{return ERROR;}

%%

//Helpful link for [:punct:]: ftp://ftp.gnu.org/old-gnu/Manuals/flex-2.5.4/html_mono/flex.html
