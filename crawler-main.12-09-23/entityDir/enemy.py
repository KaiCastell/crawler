import entity
import random



class Enemy(entity.Entity): # needs string name, along with allies, note enemies do not use multipliers
    
    #REPLACEME with actions functions. the creation of this dictionary should instantiate the proper objects. action.actions(move) i think? I can't think of a better way.

    def __init__(self): # all enemy types will be subclasses of enemy?
        self.critChance = 0.05 # base is 5% but can change
        self.critDmgMult = 2.0 # base is a damage double
        
        # vvv works like a multiplier table. 0.5 is a 50% resistance. dictionary lookup is better here
        self.dmgInMult = {'all':1.0, 'physical':1.0, 'magical':1.0}
        self.conditions = [] #REPLACEME should just run down the entire list anytime anything happens
        
        #dmgOut not needed since attacks are tailored (no items)
    def __str__(self):
        return super().__str__()
    # def shortPrint(self):
    #     return super().shortPrint()

class Lobster(entity.Entity):
    enemyNumber = 1
    def __init__(self):
        name = "Lobster " + str(Lobster.enemyNumber)
        Lobster.enemyNumber += 1
        maxHealth = random.randrange(7,13)
        health = maxHealth
        speed = 1
        block = 4
        super(Lobster, self).__init__(name, maxHealth, health, speed, block)
        
    def __str__(self):
        return super(Lobster, self).__str__()
        
    def attack(self):
        pass