# entities for now include players and enemies and npcs


class Entity:
    conditions = [] # REPLACEME fill with lists of each condition
    critChance = 0.05
    critDmgMult = 2.0

    def __init__(self, name, position, maxHealth, health, speed, block, dmgInMult):
        self.name = name
        self.position = position
        self.maxHealth = maxHealth
        self.health = health
        self.speed = speed
        self.block = block
        #self.blockMult = blockMult
        #self.healingMult = healingMult
        self.dmgInMult = dmgInMult
        #self.dmgOutMult = dmgOutMult

    def __str__(self): #NOTEME dictionaries are cap sensitive so the print out is cringe rn, will need clean up later
        return (f"ID: {id(self)}\nName: {self.name}\nHealth: {self.health}/{self.maxHealth}\nBlock: "
                f"{self.block}\nCrit Chance: {self.critChance*100}%\nCrit Damage: {self.critDmgMult}\n"
                f"Damage Received Table: {self.dmgInMult}\n")
        #just an example, realistically this should never be printed? Or one for the enemy is unneeded and it actually just goes here
                
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
    
    def singleTarget(self, range, targetName): #two cases here. Melee effect, ranged effect. Ranged has to check for things in the way. This just returns whether it is legal or not
        if range == 1: #check everything in one space demonstrated below is range one
            # 
            #    # # #  indexes y-1 : (x-1) (x) (x+1)
            #    # A #          y   : (x-1)     (x+1)
            #    # # #          y+1 : (x-1) (x) (x+1)
            # 
            pass
        

class Ally(Entity):
    pass