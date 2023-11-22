class Entity:
    actions = [] 
    conditions = [] # REPLACEME fill with lists of each condition
    def __init__(self, name, maxHealth, health, speed, block, blockMult, critChance, critDmgMult, healingMult, dmgInMult, dmgOutMult):
        self.name = name
        self.maxHealth = maxHealth
        self.health = health
        self.speed = speed
        self.block = block
        self.blockMult = blockMult
        self.critChance = critChance
        self.critDmgMult = critDmgMult
        self.healingMult = healingMult
        self.dmgInMult = dmgInMult
        self.dmgOutMult = dmgOutMult
    def __str__(self):
        return (f"ID: {id(self)}\nName: {self.name}\nHealth: {self.health}/{self.maxHealth}\nBlock: {self.block}\nBlock Multiplier: {self.blockMult}\nCrit Chance: {self.critChance*100}%\n"
                f"Crit Damage: {self.critDmgMult}\nHealing Multiplier: {self.healingMult}\nDamage Received Table: {self.dmgInMult}\nDamage Dealt Table: {self.dmgOutMult}\n")
        #just an example, realistically this should never be printed? Or one for the enemy is unneeded and it actually just goes here

class Enemy(Entity): # needs string name, along with allies
    pass

class Ally(Entity):
    pass

