import entity
import random

class Enemy(entity.Entity): # needs string name, along with allies, note enemies do not use multipliers
    
    #REPLACEME with actions functions. the creation of this dictionary should instantiate the proper objects. action.actions(move) i think? I can't think of a better way.
    intent = [] #notes all targets for the intent
    # intentTarget = "none"
    # intentEffect1 = "none"
    # intentNumber1 = 0
    # intentEffect2 = "none"
    # intentNumber2 = 0


    def __init__(self, name, maxHealth): # all enemy types will be subclasses of enemy?
        # self.level = 1 # this is the level to print the enemy for backliners and stuff
        # vvv works like a multiplier table. 0.5 is a 50% resistance. dictionary lookup is better here
        self.dmgInMult = {'all':1.0, 'physical':1.0, 'magical':1.0}
        self.conditions = [] #REPLACEME should just run down the entire list anytime anything happens
        super(Enemy, self).__init__(name, maxHealth)
        #dmgOut not needed since attacks are tailored (no items)

    def declareIntent(self, board, intentTarget, intentEffect1, intentNumber1, intentEffect2, intentNumber2): #NOTEME may make a version that is usable by all enemies declareSingleAttack or something
        temp = None
        match intentTarget:
            case "none":
                print(f"Error, no attackType assigned to {self.name}. No attack declared.")
            case "single simple player":
                pos = board.getPosition(self.name)
                temp = board.players
                target = temp[pos] # target the opposite side (the player on the same side as this enemy)
            case "self":
                temp = self
        self.intent.append({'target':target, 'intentEffect1': intentEffect1, 'intentNumber1': intentNumber1, 'intentEffect2' : intentEffect2, 'intentNumber2' : intentNumber2} )


    def __str__(self):
        return super().__str__()
    # def shortPrint(self):
    #     return super().shortPrint()

class Lobster(entity.Entity):
    enemyNumber = 1
    def __init__(self):
        self.intentType = "none"
        name = "Lobster " + str(Lobster.enemyNumber)
        Lobster.enemyNumber += 1
        maxHealth = random.randrange(4,8) #random is inclusive
        self.block = 4
        super(Lobster, self).__init__(name, maxHealth)
        
    def __str__(self):
        return super(Lobster, self).__str__()
    def declareIntent(self, board):
        decision = random.randrange(0,1)
        match decision:
            case 0: # attack decision
                intentTarget = "single simple player"
                intentEffect1 = "damage"
                intentNumber1 = random.randrange(3,5)
            case 1: # block
                intentTarget = "self"
                intentEffect1 = "block"
                intentNumber1 = random.randrange(4,7)
        intentEffect2 = "none"
        intentNumber2 = 0
        super(Lobster, self).declareIntent(board, intentTarget, intentEffect1, intentNumber1, intentEffect2, intentNumber2)