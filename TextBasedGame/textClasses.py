from random import randint, uniform
import time

from observe import Observable
from observe import Observer


class Game(Observer):

	def __init__(self):
		self.neighborhood = Neighborhood()
		self.player = Player("Holder")
		self.gameOver = False

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
		
	def playGame(self):
		while (self.gameOver != True):
			for i in self.neighborhood.houses:
				if(self.neighborhood.houses.index(i) % 6 != 0):
						if(i.monsters == 0):
							print("  %d.C  " % self.neighborhood.houses.index(i), end=""),
						else:
							print("  %d.H  " % self.neighborhood.houses.index(i), end=""),
				else:
					print("")
			try: 
				choice = int(input("\rPick a number of house to move to: "))
				if(choice >= 0 and choice <= len(self.neighborhood.houses)):
					if(self.neighborhood.houses[int(choice)].monsters == 0):
						print("That house has no monsters in it! Your work there is done.")
					else:
						self.neighborhood.enterHouse(int(choice), self.player)
				else:
					print("Please enter a number in the range of 1 and 25.")
			except ValueError:
					print("Please enter a number in the range of 1 and 25")


class Neighborhood(Observer, Observable):
	
	def __init__(self):
		Observable.__init__(self)
		self.rows = 5
		self.cols = 5
		self.houses = []
		for i in range(self.rows * self.cols):
			self.houses.append(House())
			
	def enterHouse(self, house, player):
		self.houses[house].engageHouse(player)
		
	def getHouses(self):
		return self.houses


class House(Observer, Observable):
		
	def __init__(self):
		Observable.__init__(self)
		self.monsters = randint(0, 10)
		self.memberList = []
		self.userSelection = 0
		self.iniciateMemberList()
		
	def getMonsters(self):
		return self.monsters
	
	def getMembers(self):
		return self.memberList
	
	def getUserSelection(self):
		return self.userSelection

	def setUserSelection(self, value):
		self.userSelection = value
				
	def iniciateMemberList(self):
		for i in range(self.monsters):
			choice = randint(0, 3)
			if(choice == 0):
				self.getMembers().append(Zombie())
			elif(choice == 1):
				self.getMembers().append(Vampire())
			elif(choice == 2):
				self.getMembers().append(Ghoul())
			elif(choice == 3):
				self.getMembers().append(Werewolf())

	def engageHouse(self, thePlayer):
		while(self.getUserSelection() != -1 or self.getMonsters() == 0):
			print("\rYour health is: %s. " % thePlayer.getHealth(), end="")
			try:
				self.userSelection = int(input("""What will you do?
					0: Run			1: Fight
					"""))
				if(self.getUserSelection() == 0 or self.getUserSelection() == 1):
					if(self.getUserSelection() == 0):
						self.setUserSelection(-1)
					else:
						self.fight(thePlayer)
				else:
					print("Please enter in either 0 or 1.")
			except ValueError:
				print("Please enter in either 0 or 1.")
				
				
				
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
				print("%d.%s: %d HP\t" % (self.getMembers().index(i), self.getMembers()[self.getMembers().index(i)].name, self.getMembers()[self.getMembers().index(i)].health), end="")
			else:
				print("\r%d.%s: %d HP\t" % (self.getMembers().index(i), self.getMembers()[self.getMembers().index(i)].name, self.getMembers()[self.getMembers().index(i)].health), end="")
			
		try:
			holder = int(input("\r\rWho will you target?"))
			if(holder >= 0 and holder <= len(self.getMembers())):
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
		NPC.__init__(self, "Person", 100, -1, -1)
		
	def takeDamage(self, damage):
		self.health -= 0


class Zombie(NPC):

	def __init__(self):
		NPC.__init__(self, "Zombie", randint(50, 100), 0, 10)
		
	def takeDamage(self, damage, mod):
		if(mod.name == "SourStraws"):
			self.health -= damage * 2
		else:
			self.health -= damage

			
class Vampire(NPC):

	def __init__(self):
		NPC.__init__(self, "Vampire", randint(100, 200), 10, 20)

	def takeDamage(self, damage, mod):
		if((mod.name == "ChocolateBars")):
			self.health -= 0
		else:
			self.health -= damage


class Ghoul(NPC):

	def __init__(self):
		NPC.__init__(self, "Ghoul", randint(40, 80), 15, 30)

	def takeDamage(self, damage, mod):
		if(mod.name == "NerdBombs"):
			self.health -= damage * 5
		else:
			self.health -= damage


class Werewolf(NPC):

	def __init__(self):
		NPC.__init__(self, "Werewolf", 200, 0, 40)
		
	def takeDamage(self, damage, mod):
		if((mod.name == "ChocolateBars") or (mod.name == "SourStraws")):
			self.health -= 0
		else:
			self.health -= damage


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
		self.minAtk = 10
		self.maxAtk = 20
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
			elif(choice == 4):
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
		

