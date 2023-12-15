import entity

class Enemy(entity.Entity): # needs string name, along with allies, note enemies do not use multipliers
    block = 0
    critChance = 0.05 # base is 5% but can change
    critDmgMult = 2.0 # base is a damage double
    # vvv works like a multiplier table. 0.5 is a 50% resistance. dictionary lookup is better here
    dmgInMult = {'all':1.0, 'bludgeoning':1.0, 'slashing':1.0, 'piercing':1.0}
    #dmgOut not needed since attacks are tailored
    
    #REPLACEME with actions functions. the creation of this dictionary should instantiate the proper objects. action.actions(move) i think? I can't think of a better way.
    conditions = [] #REPLACEME should just run down the entire list anytime anything happens

    def __init__(self): # all enemy types will be subclasses of enemy?
        pass

class Lobster(entity.Entity):
    maxHealth = 9
    health = maxHealth
    speed = 1

    def attack(self, targetName):
        pass