# entities for now include players and enemies and npcs


class Entity:
    conditions = [] # REPLACEME fill with lists of each condition
    critChance = 0.05
    critDmgMult = 2.0
    tilePrint = ""
    dmgInMult = {'all':1.0, 'physical':1.0, 'magical':1.0}
    position = [-1,-1]

    def __init__(self, name, maxHealth, health, speed, block):
        self.name = name
        self.maxHealth = maxHealth
        self.health = health
        self.speed = speed
        self.block = block
        #self.blockMult = blockMult
        #self.healingMult = healingMult
        
        #self.dmgOutMult = dmgOutMult

    def __str__(self): #NOTEME dictionaries are cap sensitive so the print out is cringe rn, will need clean up later
        return (f"ID: {id(self)}\nName: {self.name}\nHealth: {self.health}/{self.maxHealth}\nBlock: "
                f"{self.block}\nCrit Chance: {self.critChance*100}%\nCrit Damage: {self.critDmgMult}\n"
                f"Damage Received Table: {self.dmgInMult}\n")
        #just an example, realistically this should never be printed? Or one for the enemy is unneeded and it actually just goes here
    
    def assignTilePrint(self, string):
        self.tilePrint = string.lower()
    
    def shortPrint(self):
        return f"Name: {self.name}\nHealth: {self.health}/{self.maxHealth}Block: {self.block}"
    
    def move(self, room, newX, newY):
        #print(f"Made it to {newX},{newY}")
        string = ""
        x = self.position[0]
        y = self.position[1]
        currentEntity = room.tileArray[x][y].entity
        
        if(x == newX and y == newY):
            string += "New position is the same. Nothing done.\n"
        elif(room.tileArray[newX][newY].occupied): #REPLACEME get more specific and say what it is occupied by
            string += "New position is occupied. Nothing done.\n"
        elif(abs(x-newX) > currentEntity.speed or abs(y-newY) > currentEntity.speed):
            string += f"New position is farther than speed. Current speed is {currentEntity.speed}."
        else:
            room.tileArray[x][y].occupied = False
            room.tileArray[newX][newY].occupied = True
            room.tileArray[newX][newY].entity = room.tileArray[x][y].entity
            room.tileArray[x][y].entity = None
            self.position = [x, y]
            string += f"{self.name} successfully moved.\n"
            string += room.print()
        
        return string   
    
    def singleTarget(self, room, range, targetName): # two cases here. Melee effect, ranged effect. Ranged has to check for things in the way.
        # returns the entity if legal, returns false otherwise I think
        target = False 
        # NOTEME need to check for allies and enemies at some point, doesn't verify whether the target is "legal". May not need to.
        # if they want to heal an enemy why not
        for x in room.entityList: # go through
                if x.name == targetName: # found match
                    target = x # assign the guy
        if target == False:
            print("Single target attempted. Target name not found")
            return False
        if range == 1: #check everything in one space demonstrated below is range one
            # 
            #    # # #  indexes y-1 : (x-1) (x) (x+1)
            #    # A #          y   : (x-1)     (x+1)
            #    # # #          y+1 : (x-1) (x) (x+1)
            # 
            # should be legal as long as it isn't a corner with walls on both sides, but that shouldn't happen NOTEME
            # notice that we aren't checking the actual grid so we don't need to watch out for an out-of-bounds
            if target.position[1] - 1 == self.position[1]: # y position up match
                if target.position[0] - 1 == self.position[0]: # x position left match
                    return target # good to go
                if target.position[0] == self.position[0]:
                    return target
                if target.position[0] + 1 == self.position[0]: # x pos right
                    return target
            if target.position[1] == self.position[1]: #y position middle match
                if target.position[0] - 1 == self.position[0]: # x position left match
                    return target # good to go
                if target.position[0] + 1 == self.position[0]: # middle spot is self btw
                    return target
            if target.position[1] + 1 == self.position[1]: #y position down match
                if target.position[0] - 1 == self.position[0]: # x position left match
                    return target # good to go
                if target.position[0] == self.position[0]:
                    return target
                if target.position[0] + 1 == self.position[0]:
                    return target
            print("Single target attempted. Not in range for melee. Failed.")
            return False
        elif range > 1: # this is for higher ranges, need to check for line of sight.
            pass
        else: # means that range is lower than 1...
            print(f"Single target attack attemped. Illegal range stated: {range}.")
            return False

class Ally(Entity):
    pass