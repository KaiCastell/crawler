class Entity:
    conditions = [] # REPLACEME fill with lists of each condition

    def __init__(self, name, maxHealth, health, speed, block, critChance, critDmgMult, dmgInMult, dmgOutMult):
        self.name = name
        self.maxHealth = maxHealth
        self.health = health
        self.speed = speed
        self.block = block
        #self.blockMult = blockMult
        self.critChance = critChance
        self.critDmgMult = critDmgMult
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
        for x in range(len(room.tileArray)):
            for y in range(len(room.tileArray[x])):
                currentEntity = room.tileArray[x][y].entity
                try: #try needed so that empty entity blocks in currentEntity can be tested without fail
                    if(self.name == currentEntity.name):
                        string += f"Found {self.name} at {x},{y}\n" #now that we have found the name, check if the new spot is empty
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
                            string += f"{self.name} successfully moved.\n"
                            string += room.print()
                        return string
                except Exception as e:
                    print(e)
                    #pass
                #if(room.tileArray[x][y].entity.name == name):
                #    return "Found name."
        string += f"{self.name} is not on the map."
        return string
    
    def attack(self, range, targetName): #checks if the attack is within range
        pass

class Ally(Entity):
    pass