# from entityDir import player
# from entityDir import enemy

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
    def __str__(self):
        match(self.getIdentity()):
            case "wall":
                return "# "
            case "empty":
                return "  "
            case "entity":
                temp = self.entity
                return temp.tilePrint
            case "interact":
                return "i "

class Room: #this is what fills the tileArray no matter what you put inside the __init__
    tileArray = [] #2D arrays need an immediate size, so once we have a chance the room needs to be randomized, here it has 5 rows and 5 columns
    entityList = [] #this is for faster finds n stuff
    
    
    def __init__(self, RoomID, description, shape): #initializing the room
        self.RoomID = RoomID
        self.description = description
        match shape:
            case "test small":
                rows = 8 #REPLACEME with randomization later
                cols = 8
                for x in range(rows): #attempts to iterate the array
                    row = []
                    for y in range(cols):
                        if(x == 0 or y == 0 or x == rows-1 or y == cols-1):
                            row.append(Tile(True, None, None)) #should print all walls
                        else:
                            row.append(Tile(False, None, None))
                    self.tileArray.append(row)

    def spawnEntity(self, entity): #REPLACEME later on make this fit for any shaped room right now just finds first legal spot
        
        
        
        tPrint = entity.name #tPrint is for our tile print
        tPrint = tPrint.split()
        if(len(tPrint) > 1):
            tPrint[len(tPrint)-1] = "" #we take everything but the last word if its longer than one. Players are always only one word so this is for entities, who come with numbers. e.g. lobster 1
        tPrint = " ".join(tPrint)
        
        foundMatch = False
        # here we try to assign the same letter as similar entities
        # for x in self.entityList:
        #     temp = x.name
        #     temp = temp.split()
        #     if(len(temp) > 1):
        #         temp[len(temp)-1] = ""
        #     temp = " ".join(temp) #we do the same thing to the current entity
        #     if(temp == tPrint): #if they are the same, that means we have the same 
        #         entity.tilePrint = temp.tilePrint
        #         foundMatch = True
        #         break
        #         #we found a match so we don't need to go through the other loops to make a tile print
        
        tempTilePrint = tPrint[0:1]
        if(not foundMatch):
            # we need to assign the new entity a legal tile print "ID"
            count = 0
            while(True):
                noCopies = True #checks to see if we made changes
                for x in self.entityList:
                    checking = x.tilePrint
                    try:    
                        checking = checking[count:count+1]
                        tempTilePrint = tPrint[count:count+1]
                    except:
                        noCopies = False #means we made changes so we have to check again to make sure there's no copies
                        break 
                    if(tempTilePrint == checking): #means we need a new identity
                        count += 1
                        noCopies = False #means we made changes so we have to check again to make sure there's no copies
                        break
                if(count+1 > len(entity.name)): #we also leave if we went through the whole name without finding a free letter (I hope this never happens)
                    print(f"No free tile found for {entity.name}.")
                    break
                if(noCopies): #we didnt make changes means we didnt find a replicant and we don't need to repeat
                    break
            print(f"{entity.name} assigned letter {tempTilePrint}")
            entity.assignTilePrint(tempTilePrint + " ") #NOTEME may need to have reserved letters later for particular entities (chest etc)
            # finally uppercase it and we are done looking (players are always uppercased)
        
        for x in range(len(self.tileArray)):
            for y in range(len(self.tileArray[x])):
                if self.tileArray[x][y].getIdentity() == "empty":
                    entity.position = [x, y]
                    self.tileArray[x][y].occupied = True
                    self.tileArray[x][y].entity = entity
                    self.entityList.append(entity)
                    print(f"Added {entity.name} to map.")
                    return
        print("Failed to find an empty space to add player to map")
        return
    
    def findTile(self, string):
        findString = string[:1].lower() #isolate to first letter lowercase
        for x in range(len(self.tileArray)):
            for y in range(len(self.tileArray[x])):
                try:
                    entity = self.tileArray[x][y].entity
                    entityTilePrint = entity.tilePrint[:1]
                    if(entityTilePrint.lower() == findString):
                        return entity
                except:
                    pass
        return "NULL"
        
    
    def print(self): #just iterates the array to print based on identity
        string = "```\n  "
        for x in range(len(self.tileArray)): #top row of numbers
            string += (str(int(x)) + " ")
        string += "\n"
        for x in range(len(self.tileArray)):
            string += f"{x} " #left row of numbers
            for y in range(len(self.tileArray[x])):
                string += str(self.tileArray[x][y])
            string += "\n"
        string += "```"
        return string

#room = Room(0, "No description")
#print(room.print())