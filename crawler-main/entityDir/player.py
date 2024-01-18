import entity
#import systemsDir.cards as cards #alternate import method
from systemsDir import cards

class Player(entity.Entity): #different is xp, xpmult, luck
    mutators = [] #includes traits, relics, equipments
    conditions = [] #REPLACEME should just run down the entire list anytime anything happens
    #REPLACEME Conditions 2D List?

    xpMult = 1.0
    blockMult = 1.0
    healingMult = 1.0
    dmgInMult = {'all':1.0, 'physical':1.0, 'magical':1.0} #works like a multiplier table. 0.5 is a 50% resistance
    dmgOutMult = {'all':1.0, 'physical':1.0, 'magical':1.0} #NOTEME much shorter for now, add more later
    luck = {'common':0.60, 'uncommon':0.30, 'rare':0.10} # REPLACEME this is a placeholder. should involve a table for all interactions
    
    xp = 0
    block = 0
    maxHealth = 1
    health = 0 #current health. Should almost always initialize to = max health
    drawDie = []
    energyDie = []
    energy = 0
    hand = [] #replace later with actual hand
    incomingDamage = 0
    
    def __init__(self,name):
        self.name = name
    
    def shortPrint(self):
        return f"**{self.__class__.__name__}**\nPlayer: {self.name}\nHealth: {self.health}/{self.maxHealth}\nSpeed: {self.speed}\nXP: {self.xp}\n"  
    
    def __str__(self):
        equipment = []
        relics = []
        traits = []
        #REPLACEME, iterate through mutators to populate equipment relics and traits, Doesn't print actions anymore
        return (f"Player: {self.name}\n"+ super(Player, self).__str__() + f"Damage Dealt Table: {self.dmgOutMult}\n"
               f"Block Multiplier: {self.blockMult}\nHealing Multiplier: {self.healingMult}\nLuck:\n{self.luck}\nXP: {self.xp}\n"
               f"XP Multiplier: {self.xpMult}\nEquipment:\n{equipment}\nTraits:\n{traits}\nRelics:\n{relics}\n")

class Doctor(Player): #NOTEME only scientist finished atm
    maxHealth = 24
    health = maxHealth
    def __init__(self, name):
        super().__init__(name)
        # add doctor equipment and traits once that's a thing. adding these will automatically affect actions and stats? 
    def __str__(self):
        return "**Doctor**\n" + super(Doctor, self).__str__()

class Scientist(Player):
    maxHealth = 20
    health = maxHealth
    def __init__(self, name):
        super().__init__(name) # just different values for now just for sake's sake
        self.drawDie = [3,3,3,6,6,6]
        self.energyDie = [2,2,2,4,4,4]
        # add doctor equipment and traits once that's a thing. adding these will automatically affect actions and stats?
    def __str__(self):
        return "**Scientist**\n" + super(Scientist, self).__str__()