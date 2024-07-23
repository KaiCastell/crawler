

import entityDir.player_module as player_module

class PlayerList: #holds all current players. Reads and writes to file to save them
    def __init__(self): #on initiation takes information from files
        self.players = []
        PlayerList.load(self) #doesnt really need a seed like board so just directly load
    
    def save(self): # NOTEME This only saves players
        file = 'saves/players.txt'
        count = 1
        with open(file, 'wt') as playerFile:
            for x in self.players:
            #open up the file, closing as it exits while, opened in writing text mode
                playerFile.write(f"{x.__class__.__name__}\n{x.name}\n{x.currTime}\n{x.maxTime}\n{x.notice}\n{x.keys}\n")
                #need to save the mind later
                playerFile.write("playerend\n")
                #NOTEME after file end we should note changes not tied to mutations, xp and current health
                count+=1
        
        print("Players saved to file")
        
    def load(self):
        print("Players file read start")
        
        file = 'saves/players.txt'
        self.players = []
        count = 1
        
        try:
            with open(file, 'rt') as playerFile:
                while True: # read in all players
                    className = playerFile.readline().strip()
                    if(className == ""):
                        print("Reached end of player file")
                        break
                    print("Loading player " + str(count))
                    #start with the base class and then edit
                    
                    temp = self.addReturn(className)
                    
                    temp.name     = playerFile.readline().strip()
                    temp.currTime = playerFile.readline().strip()
                    temp.maxTime  = playerFile.readline().strip()
                    temp.notice   = playerFile.readline().strip()
                    temp.keys     = playerFile.readline().strip()
                    
                    line = playerFile.readline().strip() #save it and check if its not the end, start reading in the mutators.
                    while line != "playerend": #NOTEME need to equip all these mutators, will need an add mutator version that ignores "on equip" effects. this means it will only edit actions and conditions.
                        #if line == "": break #reached the end, likely unnecessary
                        line = playerFile.readline().strip()
                    
                    self.players.append(temp)
                        
        except: #Exception as e
            print("File cannot be reached, or does not exist\n")
        count+=1
            
    def getPlayer(self, name):
        for x in self.players:
            if(x.name == name):
                return x
    
    def getTurn(self, turn):
        return self.players[turn % len(self.players)]
    
    def viewPlayers(self):
        if(len(self.players) == 0):
            return "There are no current players."
        string = "Viewing current players: \n"
        for x in self.players:
            string += f"\t{x.name} as the {x.__class__.__name__}\n"
        return string
    
    def viewClass(self, name): # prints everything
        return str(self.getPlayer(name))
    
    def viewClassShort(self, name):
        x = self.getPlayer(name)
        return x.shortPrint()   
    
    def addPlayer(self, name, className):
        for x in self.players: # make sure they aren't already there
            if(x.name == name):
                return False # failed cuz there
        temp = self.addReturn(className)
        temp.name = name
        self.players.append(temp)
        #we now need to assign a unique letter to the player the tilePrint attribute
        
        return (f"{name} added as {temp.__class__.__name__}.") # as in success
        
    def addReturn(self, className):  # Add to here anytime you add a new class
        
        match className.lower():
            case "doctor":
                return player_module.Doctor()
            case "scientist":
                return player_module.Scientist()
            case _:
                print("No corresponding class found")
    
    def reset(self):
        self.players.clear()
        
def classDescription(className):
    string = f"You are viewing **{className}**:\n" # REPLACEME entity.Doctor with a description function, outside of classes (no object should be made) #
    match className:
        case "Doctor":
            string += "Doctor incomplete."
        case "Scientist":
            string += "Scientist incomplete."
    return string