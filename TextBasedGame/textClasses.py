from random import randint, uniform
import time

from observe import Observable
from observe import Observer


class Game(Observer):

	def __init__(self):
		self.neighborhood = Neighborhood()
		self.player = Player("Holder")
		self.gameOver = "in-progress"

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
	
	def getStatus(self):
		return self.gameOver
	
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
		
	def playLostCredits(self):
		print("""       ____
     ,'   Y`. 
    /	     \      The game was lost....
    \ ()  () /
     `. /\ ,'
 8====| "" |====8
      `LLLU'""")
			
	def playGame(self):
		while (self.gameOver == "in-progress"):
			for i in range(0, len(self.neighborhood.houses)):
				if(i % 5 != 0):
						if(self.neighborhood.houses[i].monsters == 0):
							print("  %d.C  " % i, end = "")
						else:
							print("  %d.H  " % i, end = "")
				else:
					if(self.neighborhood.houses[i].monsters == 0):
						print("\r  %d.C  " % i, end = "")
					else:
						print("\r  %d.H  " % i, end = "")
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
			
			if(self.player.getHealth() <= 0):
				self.gameOver = "player lost"
			elif(self.neighborhood.getHousesLeft() == 0):
				self.gameOver = "player won"
			else:
				pass

		if(self.getStatus() == "player won"):
			self.playWonCredits()
		else:
			self.playLostCredits()
class Neighborhood(Observer, Observable):
	
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
		
	def getHousesLeft(self):
		return self.housesLeft
			
	def enterHouse(self, house, player):
		self.houses[house].engageHouse(player)
		
	def getHouses(self):
		return self.houses
	
	def updateObserver(self, updater):
		print(self.housesLeft)
		self.housesLeft -= 1


class House(Observer, Observable):
		
	def __init__(self):
		Observable.__init__(self)
		self.monsters = randint(0, 10)
		self.memberList = []
		self.userSelection = 1
		self.iniciateMemberList()
		
	def getMonsters(self):
		return self.monsters
	
	def getMembers(self):
		return self.memberList
	
	def getUserSelection(self):
		return self.userSelection

	def setUserSelection(self, value):
		self.userSelection = value
		
	def decrimentMonsters(self):
		self.monsters -= 1
				
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
				
				
	def fight(self, thePlayer):
		
		while True:
			if(self.pickTarget(thePlayer) != 1):
				pass
			else:
				break
		
		while True:
			if(self.pickWeapon(thePlayer) != 1):
				pass
			else:
				break
		
		
		self.getMembers()[int(thePlayer.getTarget())].takeDamage(thePlayer.dealDamage(), thePlayer.getCurrentMod())
		
		for i in self.getMembers():
			thePlayer.takeDamage(i.dealDamage(i.getMinDamage(), i.getMaxDamage()))
	
	
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
	
	def updateObserver(self, updater):
		self.getMembers().remove(updater)
		self.getMembers().append(Person())
		self.decrimentMonsters()
		if(self.getMonsters() == 0):
			Observable.updateObservable(self)
	
class NPC(Observable):

	def __init__(self, name, health, lowDmg, highDmg):
		Observable.__init__(self)
		self.name = name
		self.health = health
		self.lowDmg = lowDmg
		self.highDmg = highDmg
		
	def dealDamage(self, lowDmg, highDmg):
		return randint(lowDmg, highDmg)

	def takeDamage(self, damage, mod):
		self.health -= damage

	def getName(self):
		return self.name
	
	def getHealth(self):
		return self.health
	
	def getMinDamage(self):
		return self.lowDmg
	
	def getMaxDamage(self):
		return self.highDmg
		

class Person(NPC):

	def __init__(self):
		NPC.__init__(self, "Person", 100, -5, -5)
		
	def takeDamage(self, damage, mod):
		self.health -= 0


class Zombie(NPC):

	def __init__(self):
		NPC.__init__(self, "Zombie", randint(60, 73), 0, 10)
		
	def takeDamage(self, damage, mod):
		if(mod.name == "SourStraws"):
			self.health -= damage * 2
		else:
			self.health -= damage
			
		if(self.getHealth() <= 0):
			print("\rThe targeted Zombie has been defeated!")
			Observable.updateObservable(self)
			
class Vampire(NPC):

	def __init__(self):
		NPC.__init__(self, "Vampire", randint(66, 99), 10, 20)

	def takeDamage(self, damage, mod):
		if((mod.name == "ChocolateBars")):
			self.health -= 0
		else:
			self.health -= damage
			
		if(self.getHealth() <= 0):
			print("\rThe targeted Vampire has been defeated!")
			Observable.updateObservable(self)

class Ghoul(NPC):

	def __init__(self):
		NPC.__init__(self, "Ghoul", randint(43, 63), 15, 30)

	def takeDamage(self, damage, mod):
		if(mod.name == "NerdBombs"):
			self.health -= damage * 5
		else:
			self.health -= damage
			
		if(self.getHealth() <= 0):
			print("\rThe targeted Ghoul has been defeated!")
			Observable.updateObservable(self)

class Werewolf(NPC):

	def __init__(self):
		NPC.__init__(self, "Werewolf", 125, 0, 40)
		
	def takeDamage(self, damage, mod):
		if((mod.name == "ChocolateBars") or (mod.name == "SourStraws")):
			self.health -= 0
		else:
			self.health -= damage

		if(self.getHealth() <= 0):
			print("\rThe targeted Werewolf has been defeated!")
			Observable.updateObservable(self)

class Weapon:

	def __init__(self, name, minAtkMod, maxAtkMod, uses):
		self.name = name
		self.minAtkMod = minAtkMod
		self.maxAtkMod = maxAtkMod
		self.uses = uses
		
	def getUses(self):
		return self.uses
	
	def useWeapon(self):
		self.uses -= 1


class HersheyKiss(Weapon):

	def __init__(self):
		Weapon.__init__(self, "HersheyKisses", 1, 1, 100000)


class SourStraws(Weapon):

	def __init__(self):
		Weapon.__init__(self, "SourStraws", 1, 1.75, 2)


class ChocolateBars(Weapon):

	def __init__(self):
		Weapon.__init__(self, "ChocolateBars", 2, 2.4, 4)


class NerdBombs(Weapon):

	def __init__(self):
		Weapon.__init__(self, "NerdBombs", 3.5, 5, 1)


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
		