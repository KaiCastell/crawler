

class Decision:
    pass

class Room:
    idCounter = 0
    
    def __init__(self):
        self.pathways = [None, None, None, None]
        self.decisions = [None, None, None, None] # while this matches up with each pathway, there could possibly be other decisions that can be made
        self.players = [] # theoretically only needs to hold the names?
        self.id = Room.idCounter
        Room.idCounter += 1
        #    0
        #  3   1
        #    2
        
        # 1 as the room is blocked
        
    def printDescription(self):
        strReturn = ""
        strReturn += (f"ID : {self.id}\n")
        strReturn += (f"Paths : [ ")
        for x in self.pathways:
            if x is not None:
                strReturn += (f"{x.id} ")
            else:
                strReturn += "~ "
        strReturn += "]\n"
        return strReturn
        
        
    def __str__(self):
        
        # FIX ME add in a case for no players

        # player printing # # # # # # # # #
        strEnd = ""
        strNames = ""
        strHealth = ""
        strBlock = ""
        strReturn = ""
        # note each block should be "* 13-characters *"
        for x in self.players: # end piece
            strEnd += "* * * * * * * * *  " 
        for x in self.players: # name
            strNames += "* " + self.adjustName(x.name, False) + " *  " # up to 4 player max
        for x in self.players: # health
            temp = f"{x.health}/{x.maxHealth}"
            temp = "{:^13}".format(temp)
            temp = "* " + temp + " *  "
            strHealth += temp
        for x in self.players: # current block
            temp = "{:^13}".format(x.block)
            temp = "* " + temp + " *  "
            strBlock += temp
        strReturn += f"{strNames}\n{strHealth}\n{strBlock}\n{strEnd}\n\n\n" # name printing complete
        
        
        # exit printing # # # # # # # # # #
        
        strTop = ""
        strMid1 = ""
        strMid2 = ""
        strMid3 = ""
        strEnd = ""
        
        count = 1
        
        for x in self.pathways:
            
            strTop +=      "* * * * * *      "
            strMid1 += f"*    {count}    *      "
            strMid2 +=     "*         *      "
            if x is None:
                strMid3 += "* Blocked *      "
            else:
                strMid3 += "*   Open  *      "
            strEnd +=  "* * * * * *      "
            count += 1
                
        strReturn += f"\n\n{strTop}\n{strMid1}\n{strMid2}\n{strMid3}\n{strEnd}\n"
        
        
        return strReturn
    
    def adjustName(self, name, isEnemy): #returns the name in 12 character max form for printing
        if(len(name) > 12):
            if(isEnemy):
                end = name[len(name)-1:]
                return name[:10] + ".." + end
            else:
                end = name[len(name)-3:]
                return name[:8] + ".." + end
        else:
            return f"{name:^13}"

    def leadsTo(self, nextRoom, direction, oneway):
        self.pathways[direction] = nextRoom
        if(oneway == False):
            set = self
        else:
            set = 1 # blocked
        match(direction): # setting the way back
            case 0:
                nextRoom.pathways[2] = set
            case 1:
                nextRoom.pathways[3] = set
            case 2:
                nextRoom.pathways[0] = set
            case 3:
                nextRoom.pathways[1] = set


class Board: #this is for the current game board"

    
    # extra board effects variable? like burning or idk stuff
    def __init__(self, players, seed):
        self.rooms = []
        print("A board is being created... ", end = "")
        
        if(seed == "test"):
            print("mode: Test")
            print("Adding rooms...")
            room0 = Room()
            room1 = Room()
            room2 = Room()
            room3 = Room()
            
            self.addRoom(room0)
            self.connectNewRoom(room0, 1, room1, False)
            self.connectNewRoom(room0, 2, room2, False)
            self.connectNewRoom(room1, 3, room3, False)
            
            print("Adding players...")
            for x in players.players: # NOTEME currently not working
                (room0.players).append(x)
                print(f"Added {x.name}", end = "")
            print("")

        elif(seed == "random"):
            print("mode: Random\n")
            pass
    
    def getRoom(self, name): #given player name
        for x in self.rooms:
            for y in x.players:
                if y.name == name:
                    return x
    def getRoomID(self, ID):
        for x in self.rooms:
            if x.id == ID:
                return x
    def addRoom(self, room): #should be the first room only
        self.rooms.append(room)
    
    def connectNewRoom(self, oldRoom, direction, newRoom, oneway):
        self.rooms.append(newRoom)
        oldRoom.leadsTo(newRoom, direction, oneway)
    def movePlayer(self, name, decision): #unsure
        
        decision = int(decision)
        newRoom = (self.getRoom(name).pathways)[decision-1]
        count = 0
        for x in self.getRoom(name).players:
            if x.name == name:
                newRoom.players = x
                (self.getRoom(name).players)[count] = None
            count += 1
                
        newRoom.players.append(name)
        return newRoom
                
    
    def getPosition(self, name):
        pass
        
    def __str__(self): #prints the game state | should be an admin capability
        print("Attempting to print the board... ", end = "")
        strReturn = ""
        for x in self.rooms:
            strReturn += x.printDescription()
            strReturn += "\n"
        strReturn += ""
        return strReturn

