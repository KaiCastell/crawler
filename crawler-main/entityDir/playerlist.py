import os
import sys
#this here is a generic solution to importing within the same folder issues
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import player

class PlayerList: #holds all current players. Reads and writes to file to save them
    def __init__(self): #on initiation takes information from files
        print("File read start")
        self.players = []
        count = 1
        loop = True
        while loop: # read in all players
            try:
                with open('player' + str(count) + '.txt', 'rt') as playerFile:
                    print("Opening player" + str(count) + ".txt")
                    #start with the base class and then edit
                    className = playerFile.readline().strip()
                    name = playerFile.readline().strip()
                    self.add(name, className)
                    line = playerFile.readline().strip() #save it and check if its not the end, start reading in the mutators.
                    while line != "fileend": #NOTEME need to equip all these mutators, will need an add mutator version that ignores "on equip" effects. this means it will only edit actions and conditions.
                        #I anticipate a bug here where the conditions get added and applied, double applying some effects. how to prevent? putting in notes
                        line = playerFile.readline().strip() # REPLACEME here if it wasn't equipment then you would start reading, so if an action took 5 lines to represent we want 5 readlines then go back to the top, ending with a line = playerFile, 
                        #note that the first read in would actually be action.attribute = line
            except: #Exception as e
                #print(e) UNCOMMENT IF YOU WANT TO KNOW THE ERROR, alongside code up one line
                loop = False # we no longer found a file so we break out, kinda beats a dead horse if i understand things correctly
                print("File read end")
                break
            count+=1
        
    def save(self): # NOTEME This only saves players
        count = 1
        if(len(self.players) == 0):
            file = 'player' + str(count) + '.txt'
            while(os.path.exists(file)):
                os.remove(file)
                count+=1
                file = 'player' + str(count) + '.txt'
        else:
            for x in self.players:
                with open('player' + str(count) + '.txt', 'wt') as playerFile: #open up the file, closing as it exits while, opened in writing text mode
                    playerFile.write(f"{x.__class__.__name__}\n{x.name}\n")
                    # NOTEME mutators are anything that change the actions and conditions of a player: relics, equipment, traits
                    for y in range(len(x.mutators)):
                        playerFile.write(x.mutators[y] + "\n")
                    playerFile.write("fileend")
                    #NOTEME after file end we should note changes not tied to mutations, xp and current health
                count+=1
        
        print("Players saved to file")
    
    def getPlayer(self, name):
        for x in self.players:
            if(x.name == name):
                return x
    def viewPlayers(self):
        if(len(self.players) == 0):
            return "There are no current players."
        string = "Viewing current players:\n"
        for x in self.players:
            string += f"\t{x.name} as the **{x.__class__.__name__}**\n"
        return string
    
    def viewClass(self, name): # prints everything
        return str(self.getPlayer(name))
    
    def viewClassShort(self, name):
        x = self.getPlayer(name)
        return x.shortPrint()
        
    def add(self, name, className):
        for x in self.players:
            if(x.name == name):
                return False
        match className:
            case "Doctor":
                self.players.append(player.Doctor(name))
            case "Scientist":
                self.players.append(player.Scientist(name))
            case _:
                print("No corresponding class found")
        #we now need to assign a unique letter to the player the tilePrint attribute            
        
        return True
    
    def addFromDropdown(self, name, className): # Add to here anytime you add a new class
        if(self.add(name, className)):
            print(f"{className} assigned to {name}")
            return f"You have been assigned **{className}**."
        else:
            print(f"{className} attempted to be assigned to {name}. Failed.")
            return f"You already chose a class. If you want a new class, call the delete function."
        
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