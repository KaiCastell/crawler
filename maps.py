import entity
import player

class Tile:
    occupied = False
    entity = None
    interact = None
    def __init__(self):
        self.occupied = False
        self.entity = None
        self.interact = None
    def __init__(self, occupied, entity, interact):
        self.occupied = occupied
        self.entity = entity
        self.interact = interact
    def getIdentity(self):
        if(self.occupied):
            if(self.entity != None):
                return "entity"
            elif(self.interact != None):
                return "interact"
            else:
                return "wall"
        else:
            return "empty"

class Room: #this is what fills the tileArray no matter what you put inside the __init__
    tileArray = [] #2D arrays need an immediate size, so once we have a chance the room needs to be randomized, here it has 5 rows and 5 columns
    rows = 5 #REPLACEME with randomization later
    cols = 5
    for x in range(rows): #attempts to iterate the array
        row = []
        for y in range(cols):
            if(x == 0 or y == 0 or x == rows-1 or y == cols-1):
                row.append(Tile(True, None, None)) #should print all walls
            else:
                row.append(Tile(False, None, None))
        tileArray.append(row)
    
    def __init__(self, RoomID, description): #initializing the room
        self.RoomID = RoomID
        self.description = description

    def spawnPlayer(self, player): #REPLACEME later on make this fit for any shaped room
        for x in range(len(self.tileArray)):
            for y in range(len(self.tileArray[x])):
                if self.tileArray[x][y].getIdentity() == "empty":
                    self.tileArray[x][y].occupied = True
                    self.tileArray[x][y].entity = player
                    print("Added player to map.")
                    return
        print("Failed to find an empty space to add player to map")
        return
    
    def print(self): #just iterates the array to print based on identity
        string = "```\n"
        for x in range(len(self.tileArray)):
            for y in range(len(self.tileArray[x])):
                match(self.tileArray[x][y].getIdentity()):
                    case "wall":
                        string += "# "
                    case "empty":
                        string += "  "
                    case "entity":
                        string += "e "
                    case "interact":
                        string += "i "
            string += "\n"
        string += "```"
        return string

#room = Room(0, "No description")
#print(room.print())