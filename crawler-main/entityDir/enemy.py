import entity
import random

class Enemy(entity.Entity): # needs string name, along with allies, note enemies do not use multipliers
    
    #REPLACEME with actions functions. the creation of this dictionary should instantiate the proper objects. action.actions(move) i think? I can't think of a better way.

    def __init__(self, name, maxHealth): # all enemy types will be subclasses of enemy?
        self.level = 1 # this is the level to print the enemy for backliners and stuff
        # vvv works like a multiplier table. 0.5 is a 50% resistance. dictionary lookup is better here
        self.dmgInMult = {'all':1.0, 'physical':1.0, 'magical':1.0}
        self.conditions = [] #REPLACEME should just run down the entire list anytime anything happens
        super(Enemy, self).__init__(name, maxHealth)
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
        maxHealth = random.randrange(4,8)
        self.block = 4
        super(Lobster, self).__init__(name, maxHealth)
        
    def __str__(self):
        return super(Lobster, self).__str__()
        
    def declareAttack(self):
        pass