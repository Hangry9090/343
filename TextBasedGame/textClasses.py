from random import randint, uniform
import time

from observe import Observable
from observe import Observer

###########################################################
# The game hold the neighborhood and player object
# it also contains the game engine
###########################################################
class Game(Observer):

	##############################
	# Iniciate the Game Object
	#
	# @param self
	##############################
	def __init__(self):
		self.neighborhood = Neighborhood()
		self.player = Player("Holder")
		self.gameOver = "in-progress"

	###########################################################
	# Prints the introduction screen and takes the players name
	#
	# @param self
	###########################################################
	def introScreen(self):

		print("""                      ,____
                      |----|
              ___     |     `
             / .-\  ./=)
            |  |"|_/\/|         Come here, what isss your name?
            ;  |-;| /_|
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /""")
		# Cred: http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/mythos.html
		self.player.name = input("Your name: ")
		print("""                      ,____
                      |----|
              ___     |     `
             / .-\  ./=)
            |  |"|_/\/|        %s this neighborhood hass fallen to a terrible fate...
            ;  |-;| /_|	       I should reap the souls of all its people who are
           / \_| |/ \ |	       now monstersssss....
          /      \/\( |
          |   /  |` ) |	       But I am on vacation in 20 minutesss.... 
          /   \ _/    |	       So I propose a way to ssssave them.....
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /""" % self.player.name)
		input("Press Enter to continue...")
		print("""                                                          
         .eec.              .e$$$c                                
        z$*^*$$eec..       zP  .3$c              
       .$^  d$^  ^^^****bee*=*^^ *$                               
       $%  d$$                   ^$%                              
      .$  z$%$bc.                 $%                              
      4F 4$^ $^^$*ec..  .ee.    ./^ b                             
      dF $P  P  F   ^^^^^3F""""""   4
      3b4$   "           $F         4      Take my "Backpack of Dessstiny" and ssssave 
      4$$$  -            $F         4      this neighborhood!                       
       $$$               $F         4                             
       *$$               $F         @                             
       4$$               $F         F                             
       ^$F   .......     $F        .F                            
        $"  z"     ^^^^^^$F^^^^^^^^^%.                            
       4$  4F     e      $L          ".                           
       4F  ^L    4$     z%"c    *.    b                           
       d    ^$*=e$$eer=$^  ^be..JL..ee*                           
       $     $   $F    $   zP   4P   F                            
       F     F   $F    4. .P    d%  J                             
      4%     F   $F     F $^   zP   P                             
      J      F   '%     Fd^   4P   4^                             
      $      F          $F         P                              
      $      L         .$         4%                              
      *      '.       .$$.       .$                               
      l       ^"****^^^  ^*******$                              
       P                         P                                
        c                      @                                 
          %4c...        ...zed*                         
               ^^^^^^^^^                                          
                              """)
		# Cred: http://www.chris.com/ascii/index.php?art=sports%20and%20activities/other
		input("Press Enter to continue...")
		print("""		

		Introducing....


			 """)
		time.sleep(5)

		print(""" 	
		
		
		By the production of Marshal Brummel and the rest of the 9090 Industries team...


			 """) 
		time.sleep(5)
		print("""		
		



			'The Text Based Game'




			""")
		time.sleep(3)
	
	###########################################################
	# Returns the status of the game
	#
	# @param self
	# @return self.gameOver
	###########################################################
	def getStatus(self):
		return self.gameOver
	
	###########################################################
	# Prints the credits if the player won
	#
	# @param self
	###########################################################
	def playWonCredits(self):
		print("""                      ,____
                      |----|
              ___     |     `
             / .-\  ./=)
            |  |"|_/\/|         Well done %s, you ssssaved the town. Ssssadly, nothing comes without a price.
            ;  |-;| /_|
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /""" % self.player.getName())
		
		print("""\r\rSWOOOSHHHHH
               .""--..__             
              /[]       ``-.._       
             / /\__           `-._         You died anyways....
            / /    ```---..__     `-.
           / /               ``--._  `.
          / /                      `-. \\
         / /                          `.\\
        / /                            `\|

																		""")
		#credit:http://ascii.co.uk/art/scythe
		
	###########################################################
	# Prints the ending if the player lost
	#
	# @param self
	###########################################################
	def playLostCredits(self):
		print("""       ____
     ,'   Y`. 
    /	     \      The game was lost....
    \ ()  () /
     `. /\ ,'
 8====| "" |====8
      `LLLU'""")
	
	###################################################################
	# Here is the game engine where the player selects a house to fight
	#
	# @param self
	###################################################################
	def playGame(self):
		while (self.gameOver == "in-progress"):
			#For each house in the neighborhood
			for i in range(0, len(self.neighborhood.houses)):
				if(i % 5 != 0):
					#Prints a C for a completed house
						if(self.neighborhood.houses[i].monsters == 0):
							print("  %d.C  " % i, end = "")
						else:
							print("  %d.H  " % i, end = "")
				else:
					#Prints a C for a complete house but adds a newline
					if(self.neighborhood.houses[i].monsters == 0):
						print("\r  %d.C  " % i, end = "")
					else:
						print("\r  %d.H  " % i, end = "")
						
			#Attempting to take a user input for the house to attack
			try: 
				choice = int(input("\rPick a number of house to move to: "))
				if(choice >= 0 and choice < len(self.neighborhood.houses)):
					if(self.neighborhood.houses[int(choice)].monsters == 0):
						print("That house has no monsters in it! Your work there is done.")
					else:
						self.neighborhood.enterHouse(int(choice), self.player)
				else:
					print("Please enter a number in the range of 1 and 25.")
			except ValueError:
					print("Please enter a number in the range of 1 and 25")
					
			#Checks the players health to see if they lost then checks to see if all houses are beaten
			if(self.player.getHealth() <= 0):
				self.gameOver = "player lost"
			elif(self.neighborhood.getHousesLeft() == 0):
				self.gameOver = "player won"
			else:
				pass

		#Rolls appropriate ending scene
		if(self.getStatus() == "player won"):
			self.playWonCredits()
		else:
			self.playLostCredits()
			
###########################################################
# The neighborhood object holds houses 
###########################################################
class Neighborhood(Observer, Observable):
	
	###########################################################
	# Inicitates the Neighborhood object
	#
	# @param self
	###########################################################
	def __init__(self):
		Observable.__init__(self)
		self.rows = 5
		self.cols = 5
		self.houses = []
		for i in range(self.rows * self.cols):
			holder = House()
			Observable.add_observer(holder, self)
			self.houses.append(holder)
			
		self.housesLeft = len(self.houses)
		print(self.housesLeft)
		
	###########################################################
	# Returns how many houses are unbeaten
	#
	# @param self
	# @return self.housesLeft
	###########################################################
	def getHousesLeft(self):
		return self.housesLeft
			
	###########################################################
	# Calls the engageHouse method for the particular house
	#
	# @param self
	###########################################################
	def enterHouse(self, house, player):
		self.houses[house].engageHouse(player)
		
	###########################################################
	# Returns the total amount of houses
	#
	# @param self
	# @return self.house
	###########################################################
	def getHouses(self):
		return self.houses
	
	###########################################################
	# Reduced the housesLeft count when updated by 
	# a defeated house
	#
	# @param self
	# @param updater
	###########################################################
	def updateObserver(self, updater):
		self.housesLeft -= 1

###########################################################
# The house is responcible for holding monsters 
# and handling fights
###########################################################
class House(Observer, Observable):
	
	###########################################################
	# Iniciates the House object
	#
	# @param self
	###########################################################	
	def __init__(self):
		Observable.__init__(self)
		self.monsters = randint(0, 10)
		self.memberList = []
		self.userSelection = 1
		self.iniciateMemberList()
		
	###########################################################
	# Returns how many monsters are in the house
	#
	# @param self
	# @return self.monsters
	###########################################################
	def getMonsters(self):
		return self.monsters
	
	###########################################################
	# Returns the list of NPCs in the house
	#
	# @param self
	# @return self.memberList
	###########################################################
	def getMembers(self):
		return self.memberList
	
	###########################################################
	# Returns the userSelection for choice making
	#
	# @param self
	# @return self.userSelection
	###########################################################
	def getUserSelection(self):
		return self.userSelection

	###########################################################
	# Sets the userSelection
	#
	# @param self
	###########################################################
	def setUserSelection(self, value):
		self.userSelection = value
		
	###########################################################
	# Reduced the number of monsters by one
	#
	# @param self
	###########################################################
	def decrimentMonsters(self):
		self.monsters -= 1
				
	###########################################################
	# Iniciates the monsters in the house
	#
	# @param self
	###########################################################
	def iniciateMemberList(self):
		for i in range(self.monsters):
			choice = randint(0, 3)
			if(choice == 0):
				holder = Zombie()
				Observable.add_observer(holder, self)
				self.getMembers().append(holder)
			elif(choice == 1):
				holder = Vampire()
				Observable.add_observer(holder, self)
				self.getMembers().append(holder)
			elif(choice == 2):
				holder = Ghoul()
				Observable.add_observer(holder, self)
				self.getMembers().append(holder)
			elif(choice == 3):
				holder = Werewolf()
				Observable.add_observer(holder, self)
				self.getMembers().append(holder)

	###########################################################
	# Choice menu to run or fight, calls fight logic
	#
	# @param self
	# @param thePlayer
	###########################################################
	def engageHouse(self, thePlayer):
		while(self.getUserSelection() != 0 and self.getMonsters() != 0):
			print("\rYour health is: %s. " % thePlayer.getHealth(), end="")
			try:
				self.setUserSelection(int(input("""What will you do?
					0: Run			1: Fight"""))) 
				if(self.getUserSelection() == 0 or self.getUserSelection() == 1):
					if(self.getUserSelection() == 0):
						pass
					else:
						self.fight(thePlayer)
				else:
					print("Please enter in either 0 or 1.")
			except ValueError:
				print("Please enter in either 0 or 1.")
				
		
		if(self.getMonsters() == 0):
			Observable.updateObservable(self)
		self.setUserSelection(1)
				
	###########################################################
	# The fighting logic for the game
	#
	# @param self
	# @param thePlayer
	###########################################################
	def fight(self, thePlayer):
		
		#Runs until there is a valid input
		while True:
			if(self.pickTarget(thePlayer) != 1):
				pass
			else:
				break
		
		#Runs until there is a valid input
		while True:
			if(self.pickWeapon(thePlayer) != 1):
				pass
			else:
				break
		
		#Attacks the player targeted monster
		self.getMembers()[int(thePlayer.getTarget())].takeDamage(thePlayer.dealDamage(), thePlayer.getCurrentMod())
		
		#Monsters attack the player
		for i in self.getMembers():
			thePlayer.takeDamage(i.dealDamage(i.getMinDamage(), i.getMaxDamage()))
	
	###########################################################
	# Prints monsters healths and asks for a target
	#
	# @param self
	# @param thePlayer
	# @return returnVal - 1 if successful, 0 if out of bounds
	###########################################################
	def pickTarget(self, thePlayer):
		returnVal = 0
		for i in self.getMembers():
			if(self.getMembers().index(i) % 4 != 0):
				print("%d.%s: %d HP\t" % (self.getMembers().index(i), self.getMembers()[self.getMembers().index(i)].name, self.getMembers()[self.getMembers().index(i)].health))
			else:
				print("\r%d.%s: %d HP\t" % (self.getMembers().index(i), self.getMembers()[self.getMembers().index(i)].name, self.getMembers()[self.getMembers().index(i)].health), end="")
			
		try:
			holder = int(input("\r\rWho will you target?"))
			if(holder >= 0 and holder < len(self.getMembers())):
				thePlayer.setTarget(holder)
				returnVal = 1
			else:
				print("Please enter in a valid monster number.")
		except ValueError:
			print("Please enter in a valid monster number.")
			
		return returnVal
	
	###########################################################
	# Prints the player weapons and gets an input
	#
	# @param self
	# @param thePlayer
	# @return returnVal - 1 if successful or 0 if otherwise
	###########################################################
	def pickWeapon(self, thePlayer):
		returnVal = 0
		for j in thePlayer.getBackpack():
			if(thePlayer.getBackpack().index(j) % 4 != 0):
				print("%d.%s: %d uses left\t\t" % (thePlayer.getBackpack().index(j), thePlayer.getBackpack()[thePlayer.getBackpack().index(j)].name, thePlayer.getBackpack()[thePlayer.getBackpack().index(j)].uses), end="")
			else:
				print("\r%d.%s: %d uses left\t" % (thePlayer.getBackpack().index(j), thePlayer.getBackpack()[thePlayer.getBackpack().index(j)].name, thePlayer.getBackpack()[thePlayer.getBackpack().index(j)].uses), end="")
		
		try:
			holder = int(input("\rWhat weapon will you use?"))
			if(holder >= 0 and holder <= len(thePlayer.getBackpack())):
				thePlayer.setMod(thePlayer.getBackpack()[holder])
				returnVal = 1
			else:
				print("Please enter in a valid item number.")
		except ValueError:
			print("Please enter in a valid item number.")

		return returnVal
	
	###########################################################
	# Removes the dead monster, adds a person, 
	# decriments monsters, and updates observers
	#
	# @param self
	# @param updater
	###########################################################
	def updateObserver(self, updater):
		self.getMembers().remove(updater)
		self.getMembers().append(Person())
		self.decrimentMonsters()
		if(self.getMonsters() == 0):
			Observable.updateObservable(self)

###########################################################
# Parent class for the monsters
###########################################################
class NPC(Observable):

	###########################################################
	# Iniciates an NPC object 
	#
	# @param self
	# @param name
	# @param health
	# @param lowDmg
	# @param highDmg
	###########################################################
	def __init__(self, name, health, lowDmg, highDmg):
		Observable.__init__(self)
		self.name = name
		self.health = health
		self.lowDmg = lowDmg
		self.highDmg = highDmg
		
	###########################################################
	# Returns a random int between high and low damage
	#
	# @param self
	# @param lowDmg
	# @param highDmg
	# @return randint(lowDmg, highDmg)
	###########################################################
	def dealDamage(self, lowDmg, highDmg):
		return randint(lowDmg, highDmg)

	###########################################################
	# Applies damage to the NPC, lowers health
	#
	# @param self
	# @param damage
	# @param mod
	###########################################################
	def takeDamage(self, damage, mod):
		self.health -= damage

	###########################################################
	# Returns name
	#
	# @param self
	# @return self.name
	###########################################################
	def getName(self):
		return self.name
	
	###########################################################
	# Returns the NPC Health
	#
	# @param self
	# @return self.health
	###########################################################
	def getHealth(self):
		return self.health
	
	###########################################################
	# Returns the lowDmg bound of the NPC
	#
	# @param self
	# @return self.lowDmg
	###########################################################
	def getMinDamage(self):
		return self.lowDmg
	
	###########################################################
	# Returns the highDmg bound of the NPC
	#
	# @param self
	# @return self.highDmg
	###########################################################
	def getMaxDamage(self):
		return self.highDmg
		
###########################################################
# The person object logic and methods
###########################################################
class Person(NPC):

	###########################################################
	# Iniciates the Person object, call the super __init__ from 
	# NPC 
	#
	# @param self
	###########################################################
	def __init__(self):
		NPC.__init__(self, "Person", 100, -5, -5)
		
	###########################################################
	# Applies no damage, ever
	#
	# @param self
	# @param damage
	# @param mod
	###########################################################
	def takeDamage(self, damage, mod):
		self.health -= 0


###########################################################
# The Zombie object logic and methods
###########################################################
class Zombie(NPC):
	
	###########################################################
	# Iniciates the Zombie object, call the super __init__ from 
	# NPC 
	#
	# @param self
	###########################################################
	def __init__(self):
		NPC.__init__(self, "Zombie", randint(60, 73), 0, 10)
	
	###########################################################
	# Applies double damage for SourStraws mod and normal otherwise
	#
	# @param self
	# @param damage
	# @param mod
	###########################################################	
	def takeDamage(self, damage, mod):
		if(mod.name == "SourStraws"):
			self.health -= damage * 2
		else:
			self.health -= damage
			
		if(self.getHealth() <= 0):
			print("\rThe targeted Zombie has been defeated!")
			Observable.updateObservable(self)

###########################################################
# The Vampire object logic and methods
###########################################################			
class Vampire(NPC):

	###########################################################
	# Iniciates the Vampire object, call the super __init__ from 
	# NPC 
	#
	# @param self
	###########################################################
	def __init__(self):
		NPC.__init__(self, "Vampire", randint(66, 99), 10, 20)

	###########################################################
	# Immune to chocolatebars and normal damage otherwise
	#
	# @param self
	# @param damage
	# @param mod
	###########################################################	
	def takeDamage(self, damage, mod):
		if((mod.name == "ChocolateBars")):
			self.health -= 0
		else:
			self.health -= damage
			
		if(self.getHealth() <= 0):
			print("\rThe targeted Vampire has been defeated!")
			Observable.updateObservable(self)


###########################################################
# The Ghoul object logic and methods
###########################################################
class Ghoul(NPC):

	###########################################################
	# Iniciates the Ghoul object, call the super __init__ from 
	# NPC 
	#
	# @param self
	###########################################################
	def __init__(self):
		NPC.__init__(self, "Ghoul", randint(43, 63), 15, 30)

	###########################################################
	# Nerdbomb damage times 5, normal damage applied otherwise
	#
	# @param self
	# @param damage
	# @param mod
	###########################################################	
	def takeDamage(self, damage, mod):
		if(mod.name == "NerdBombs"):
			self.health -= damage * 5
		else:
			self.health -= damage
			
		if(self.getHealth() <= 0):
			print("\rThe targeted Ghoul has been defeated!")
			Observable.updateObservable(self)

###########################################################
# The Werewolf object logic and methods
###########################################################
class Werewolf(NPC):

	###########################################################
	# Iniciates the Werewolf object, call the super __init__ from 
	# NPC 
	#
	# @param self
	###########################################################
	def __init__(self):
		NPC.__init__(self, "Werewolf", 125, 0, 40)
		
	###########################################################
	# No damage for chocolatebars and sourstraws
	# normal damage otherwise
	#
	# @param self
	# @param damage
	# @param mod
	###########################################################	
	def takeDamage(self, damage, mod):
		if((mod.name == "ChocolateBars") or (mod.name == "SourStraws")):
			self.health -= 0
		else:
			self.health -= damage

		if(self.getHealth() <= 0):
			print("\rThe targeted Werewolf has been defeated!")
			Observable.updateObservable(self)


###########################################################
# The Weapon parent object logic and methods
###########################################################
class Weapon:

	###########################################################
	# Iniciates the weapon class
	#
	# @param self
	# @param name
	# @param minAtkMod
	# @param maxAtkMod
	# @param uses
	###########################################################	
	def __init__(self, name, minAtkMod, maxAtkMod, uses):
		self.name = name
		self.minAtkMod = minAtkMod
		self.maxAtkMod = maxAtkMod
		self.uses = uses
		
	###########################################################
	# Return uses of wepaon
	#
	# @param self
	# @return self.uses
	###########################################################	
	def getUses(self):
		return self.uses
	
	###########################################################
	# Decriments weapon uses
	#
	# @param self
	###########################################################	
	def useWeapon(self):
		self.uses -= 1



###########################################################
# The HersheyKiss object logic and methods
# Child class of Weapon
###########################################################
class HersheyKiss(Weapon):

	def __init__(self):
		Weapon.__init__(self, "HersheyKisses", 1, 1, 100000)


###########################################################
# The SourStraws object logic and methods
# Child class of Weapon
###########################################################
class SourStraws(Weapon):

	def __init__(self):
		Weapon.__init__(self, "SourStraws", 1, 1.75, 2)


###########################################################
# The ChocolateBars object logic and methods
# Child class of Weapon
###########################################################
class ChocolateBars(Weapon):

	def __init__(self):
		Weapon.__init__(self, "ChocolateBars", 2, 2.4, 4)


###########################################################
# The NerdBombs object logic and methods
# Child class of Weapon
###########################################################
class NerdBombs(Weapon):

	def __init__(self):
		Weapon.__init__(self, "NerdBombs", 3.5, 5, 1)


###########################################################
# The Player object logic and methods
###########################################################
class Player:

	def __init__(self, name):
		self.name = name
		self.backpack = []
		self.health = 400
		self.minAtk = 15
		self.maxAtk = 25
		self.target = 0
		self.currentMod = 0
		
		self.iniciateBackpack()
	
	def iniciateBackpack(self):
		for i in range(0, 9):
			choice = randint(1, 4)
			if(choice == 1):
				self.backpack.append(HersheyKiss())
			elif(choice == 2):
				self.backpack.append(SourStraws())
			elif(choice == 3):
				self.backpack.append(ChocolateBars())
			else:
				self.backpack.append(NerdBombs())
		
	def takeDamage(self, damage):
		self.health -= damage
	
	def dealDamage(self):
		self.currentMod.useWeapon()
		if(self.currentMod.getUses() == 0):
			self.backpack.remove(self.currentMod)
		return randint(self.minAtk, self.maxAtk) * uniform(self.currentMod.minAtkMod, self.currentMod.maxAtkMod)
		
	def getName(self):
		return self.name
	
	def getHealth(self):
		return self.health

	def getMinAtk(self):
		return self.minAtk
	
	def getMaxAtk(self):
		return self.maxAtk
	
	def getTarget(self):
		return self.target
	
	def getCurrentMod(self):
		return self.currentMod
	
	def getBackpack(self):
		return self.backpack
	
	def setTarget(self, value):
		self.target = value
		
	def setName(self, value):
		self.name = value
		
	def setMod(self, value):
		self.currentMod = value
		