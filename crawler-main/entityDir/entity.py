# entities for now include players and enemies and npcs


class Entity:
    conditions = [] # REPLACEME fill with lists of each condition
    dmgInMult = {'all':1.0, 'physical':1.0, 'magical':1.0}
    block = 0

    def __init__(self, name, maxHealth):
        self.name = name
        self.maxHealth = maxHealth
        self.health = maxHealth
        
        #self.blockMult = blockMult
        #self.healingMult = healingMult
        
        #self.dmgOutMult = dmgOutMult

    def __str__(self): #NOTEME dictionaries are cap sensitive so the print out is cringe rn, will need clean up later
        return (f"ID: {id(self)}\nName: {self.name}\nHealth: {self.health}/{self.maxHealth}\nBlock: "
                f"{self.block}\nDamage Received Table: {self.dmgInMult}\n")
        #just an example, realistically this should never be printed? Or one for the enemy is unneeded and it actually just goes here
    
    def shortPrint(self):
        return f"Name: {self.name}\nHealth: {self.health}/{self.maxHealth}Block: {self.block}"

class Ally(Entity):
    pass