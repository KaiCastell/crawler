class Action: #note that mutators will use actions
    def __init__(self):
        self.name = __class__.__name__ #seems redundant but may be necessary later? do actions need to be an object at all? NOTEME

def move(name, room, newX, newY):
    #print(f"Made it to {newX},{newY}")
    string = ""
    for x in range(len(room.tileArray)):
        for y in range(len(room.tileArray[x])):
            currentEntity = room.tileArray[x][y].entity
            try: #try needed so that empty entity blocks in currentEntity can be tested without fail
                if(name == currentEntity.name):
                    string += f"Found {name} at {x},{y}\n" #now that we have found the name, check if the new spot is empty
                    if(currentEntity.hasAction("move") == False):
                        string += f"{name} does not have the move action."
                    elif(x == newX and y == newY):
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
                        string += f"Player successfully moved.\n"
                        string += room.print()
                    return string
            except Exception as e:
                #print(e)
                pass
            #if(room.tileArray[x][y].entity.name == name):
            #    return "Found name."
    string += f"{name} is not on the map."
    return string
    