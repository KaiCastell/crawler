import entity

class Player(entity.Entity): #different is xp, xpmult, luck
    mutators = [] #includes traits, relics, equipments
    #REPLACEME Conditions 2D List?
    xp = 0
    xpMult = 1.0
    block = 0
    blockMult = 1.0
    critChance = 0.05 # base is 5% but can change
    critDmgMult = 2.0 # base is a damage double
    healingMult = 1.0
    dmgInMult = {'all':1.0, 'bludgeoning':1.0, 'slashing':1.0, 'piercing':1.0} #works like a multiplier table. 0.5 is a 50% resistance
    dmgOutMult = {'all':1.0, 'bludgeoning':1.0, 'slashing':1.0, 'piercing':1.0} #NOTEME much shorter for now, add more later
    luck = {'common':0.60, 'uncommon':0.30, 'rare':0.10} # REPLACEME this is a placeholder. should involve a table for all interactions
    #REPLACEME. Actions are now functions that get overridden. the creation of this dictionary should instantiate the proper objects.
    conditions = [] #REPLACEME should just run down the entire list anytime anything happens
    
    def __init__(self,name, maxHealth, health, speed):
        self.name = name
        self.maxHealth = maxHealth
        self.health = health #current health. Should almost always initialize to = max health
        self.speed = speed
    def __str__(self):
        equipment = []
        relics = []
        traits = []
        #REPLACEME, iterate through mutators to populate equipment relics and traits, Doesn't print actions anymore
        return (f"Player: {self.name}\n"+ super(Player, self).__str__() + f"Damage Dealt Table: {self.dmgOutMult}\n"
               f"Block Multiplier: {self.blockMult}\nHealing Multiplier: {self.healingMult}\nLuck:\n{self.luck}\nXP: {self.xp}\n"
               f"XP Multiplier: {self.xpMult}\nEquipment:\n{equipment}\nTraits:\n{traits}\nRelics:\n{relics}\n")

class Doctor(Player):
    def __init__(self, name):
        super().__init__(name, 65, 65, 3)
        # add doctor equipment and traits once that's a thing. adding these will automatically affect actions and stats? 
    def __str__(self):
        return "**Doctor**\n" + super(Doctor, self).__str__()
    
class Scientist(Player):
    def __init__(self, name):
        super().__init__(name, 60, 60, 2) # just different values for now just for sake's sake
        # add doctor equipment and traits once that's a thing. adding these will automatically affect actions and stats?
    def __str__(self):
        return "**Scientist**\n" + super(Scientist, self).__str__()