

import structureDir.room_module as room_module

class Board: #this is for the current game board"

    # extra board effects variable? like burning or idk stuff
    def __init__(self, seed):
        self.rooms = []
        self.seed(seed) # separate so it can just add
    
    def save(self):
        file = 'saves/board.txt'
        with open(file, 'wt') as boardFile:
            for x in self.rooms:
            #open up the file, closing as it exits while, opened in writing text mode
                boardFile.write(f"{x.id}\n{x.type}\n")
                if(x.pathways[0] == None): 
                    path0 = -1
                else: 
                    path0 = (x.pathways[0]).id
                
                if(x.pathways[1] == None): 
                    path1 = -1 
                else: 
                    path1 = (x.pathways[1]).id
                
                if(x.pathways[2] == None): 
                    path2 = -1 
                else: 
                    path2 = (x.pathways[2]).id
                
                if(x.pathways[3] == None): 
                    path3 = -1 
                else: 
                    path3 = (x.pathways[3]).id
                
                boardFile.write(f"{path0}\n{path1}\n{path2}\n{path3}\n")
                while(len(x.players) > 0):
                    temp = (x.players).pop()
                    boardFile.write(f"{temp.name}\n")
                #need to save the mind later
                boardFile.write("roomend\n")
                #NOTEME after file end we should note changes not tied to mutations, xp and current health
        
        print("Board saved to file")
    
    def load(self):
        print("Board file read start")
        
        file = 'saves/board.txt'
        self.rooms = []
        
        try:
            with open(file, 'rt') as boardFile:
                while True: # read in all players
                    
                    # READ IN SECTION
                    
                    roomID = boardFile.readline().strip()
                    if(roomID == ""):
                        print("Reached end of board file")
                        break
                    print("Loading room " + roomID)
                    #start with the base class and then edit
                    
                    temp = room_module.Room()
                    temp.id = int(roomID)
                    
                    temp.type = int(boardFile.readline().strip())
                    temp.pathways[0] = int(boardFile.readline().strip())
                    temp.pathways[1] = int(boardFile.readline().strip())
                    temp.pathways[2] = int(boardFile.readline().strip())
                    temp.pathways[3] = int(boardFile.readline().strip())
                    
                    line = boardFile.readline().strip() #save it and check if its not the end, start reading in the mutators.
                    while line != "roomend": # means there are players
                        #if line == "": break #reached the end, likely unnecessary
                        temp.players.append(line) # this should be the name. In the fixing section we will turn this into the object
                        line = boardFile.readline().strip()
                    
                    self.addRoom(temp)
        except: #Exception as e
            print("File cannot be reached, or does not exist\n")
            return
            # means we dont have a save
            
        self.boardFix()
        
    def boardFix(self):
        pass
    
    def seed(self, seed):
        print("Creating board... ", end = "")
        try:
            players = self.players
        except:
            return "Error: Board not connected to player list yet."
        
        if(len(players) == 0):
            print("Stopped; no players\n")
            return "Cannot create a game with no players"
        
        
        if(seed == "test"):
            print("mode: Test")
            print("Adding rooms...")
            room0 = room_module.Room()
            room1 = room_module.Room()
            room2 = room_module.Room()
            room3 = room_module.Room()
            
            self.addRoom(room0)
            self.connectNewRoom(room0, 1, room1, False)
            self.connectNewRoom(room0, 2, room2, False)
            self.connectNewRoom(room1, 1, room3, False)
            
            print("Adding players...")
            for x in players: # NOTEME currently not working
                (room0.players).append(x)
                print(f"Added {x.name}", end = "")
            print("")
            
        elif(seed == "saved"):
            print("mode: Saved")
            Board.load(self)
            if(len(self.rooms) == 0):
                return "Currently no board is saved."
            
        elif(seed == "random"):
            print("mode: Random")
         
        return("Board created successfully.")
    
    def getRoom(self, criteria): #given player name, return the room the player is in
        if isinstance(criteria, str): # if string look for names
            for x in self.rooms:
                for y in x.players:
                        if y != None and y.name == criteria: # we check if none first, with help of shortcircuit to avoid error
                            return x
        elif isinstance(criteria, int): # if int look for room IDs
            for x in self.rooms:
                if x.id == criteria:
                    return x
        else:
            print("Error occurred: incorrect criteria provided on getRoom() call")
            return
        
    def addRoom(self, room): #should be the first room only
        self.rooms.append(room)
    
    def connectNewRoom(self, oldRoom, direction, newRoom, oneway):
        self.rooms.append(newRoom)
        oldRoom.leadsTo(newRoom, direction, oneway)
        
    def movePlayer(self, player, decision): #unsure
        name = player.name
        decision = int(decision) # make direction
        newRoom = (self.getRoom(name).pathways)[decision-1] # determine room we are moving to NOTEME we need to not let em move if its locked
        if(newRoom == None):
            return "You cannot move to that room, it either does not exist or you are incapable."
        for x in self.getRoom(name).players: # first we get the players room
            if x.name == name: # the following is adding the player to new room and then removing from the old one
                self.getRoom(name).players = [x for x in self.getRoom(name).players if x.name != name] #returns the room list of players with the current player in it 
                (newRoom.players).append(player)
        return newRoom
    
    def viewRoom(self, name):
        return str(self.getRoom(name))
    
    def getPosition(self, name):
        pass
        
    def viewBoard(self): #prints the game state | should be an admin capability
        print("Attempting to print the board... ", end = "")
        strReturn = ""
        for x in self.rooms:
            strReturn += x.printDescription()
            strReturn += "\n"
        strReturn += ""
        print("Done")
        return strReturn
    
    
