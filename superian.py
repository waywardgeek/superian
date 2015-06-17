from copy import copy

class Stats:
    def __init__(self, sanity, speed, attack, defense, hp):
        self.sanity = sanity
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.hp = hp

    def printStats(self):
        print "sanity:", self.sanity
        print "speed:", self.speed
        print "attack:", self.attack
        print "defense:", self.defense
        print "hp:", self.hp

class Class:

    def __init__(self, name, sanity, speed, attack, defense, hp):
        self.name = name
        self.stats = Stats(sanity, speed, attack, defense, hp)

class Player:

    def __init__(self, name, playerClass):
        self.name = name
        self.playerClass = playerClass
        self.stats = copy(playerClass.stats)

    def printPlayer(self):
        print "Name:", self.name, "    Class:", self.playerClass.name
        self.stats.printStats()

classes = {}
classes["adventurer"] = Class("adventurer", 75.0, 5.0, 5.0, 5.0, 50.0)
classes["warrior"] = Class("warrior", 75.0, 3.0, 6.0, 6.0, 50.0)
classes["tank"] = Class("tank", 75.0, 3.0, 5.0, 6.0, 60.0)
classes["ranger"] = Class("ranger", 75.0, 6.0, 5.0, 5.0, 40.0)

blorg = Player("blorg", classes["warrior"])
blorg.printPlayer()
