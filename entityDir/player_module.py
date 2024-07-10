import entityDir.mind_module as mind_module

class Entity:
    conditions = [] # REPLACEME fill with lists of each condition

    def __init__(self):
        pass
        
        #self.blockMult = blockMult
        #self.healingMult = healingMult
        
        #self.dmgOutMult = dmgOutMult

    def __str__(self): #NOTEME dictionaries are cap sensitive so the print out is cringe rn, will need clean up later
        return (f"ID: {id(self)}\nName: {self.name}\n")
        #just an example, realistically this should never be printed? Or one for the enemy is unneeded and it actually just goes here

class Ally(Entity):
    pass

class Player(Entity): #different is xp, xpmult, luck
    #REPLACEME Conditions 2D List?
    
    def __init__(self):
        self.maxTime = 10 # predetermined number
        self.currTime = 10
        self.notice = 0 # for conspicuity / how easily noticed. 0 means u very sneaky
        self.keys = 1 # start with one key
        self.mind = mind_module.Mind("Blank")
    
    def __str__(self):
        strReturn = f"Name: {self.name}\nTime: {self.currTime}/{self.maxTime}\nNotice: {self.notice}\nKeys: {self.keys}\n\n"
        strReturn += str(self.mind)
        return strReturn

class Doctor(Player): #NOTEME only scientist finished atm
    def __init__(self):
        super().__init__()
        #self.mind = mind_module.Mind("Doctor")
    def __str__(self):
        return "**Doctor**\n" + super(Doctor, self).__str__()

class Scientist(Player):
    def __init__(self):
        super().__init__() 
        self.mind = mind_module.Mind("Scientist")
    def __str__(self):
        return "**Scientist**\n" + super(Scientist, self).__str__()