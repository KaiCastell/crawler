import player
import os

class playerList:
    def __init__(self):
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
                    user = playerFile.readline().strip()
                    self.add(user, className)
                    self.players[count-1].health = int(playerFile.readline())
                    self.players[count-1].maxHealth = int(playerFile.readline())
                    self.players[count-1].speed = int(playerFile.readline())
                    self.players[count-1].xp = int(playerFile.readline())
                    self.players[count-1].xpMult = float(playerFile.readline())
                    self.players[count-1].block = int(playerFile.readline())
                    self.players[count-1].blockMult = float(playerFile.readline())
                    self.players[count-1].critChance = float(playerFile.readline())
                    self.players[count-1].critDmgMult = float(playerFile.readline())
                    self.players[count-1].healingMult = float(playerFile.readline())
                    #Dmg In Table
                    self.players[count-1].dmgInMult.update({'all':float(playerFile.readline())})
                    self.players[count-1].dmgInMult.update({'bludgeoning':float(playerFile.readline())})
                    self.players[count-1].dmgInMult.update({'slashing':float(playerFile.readline())})
                    self.players[count-1].dmgInMult.update({'piercing':float(playerFile.readline())})
                    self.players[count-1].dmgInMult.update({'magic':float(playerFile.readline())})
                    self.players[count-1].dmgInMult.update({'fire':float(playerFile.readline())})
                    self.players[count-1].dmgInMult.update({'cold':float(playerFile.readline())})
                    self.players[count-1].dmgInMult.update({'electric':float(playerFile.readline())})
                    self.players[count-1].dmgInMult.update({'poison':float(playerFile.readline())})
                    #Dmg Out Table
                    self.players[count-1].dmgOutMult.update({'all':float(playerFile.readline())})
                    self.players[count-1].dmgOutMult.update({'bludgeoning':float(playerFile.readline())})
                    self.players[count-1].dmgOutMult.update({'slashing':float(playerFile.readline())})
                    self.players[count-1].dmgOutMult.update({'piercing':float(playerFile.readline())})
                    self.players[count-1].dmgOutMult.update({'magic':float(playerFile.readline())})
                    self.players[count-1].dmgOutMult.update({'fire':float(playerFile.readline())})
                    self.players[count-1].dmgOutMult.update({'cold':float(playerFile.readline())})
                    self.players[count-1].dmgOutMult.update({'electric':float(playerFile.readline())})
                    self.players[count-1].dmgOutMult.update({'poison':float(playerFile.readline())})
                    #luck table
                    self.players[count-1].luck.update({'common':float(playerFile.readline())})
                    self.players[count-1].luck.update({'uncommon':float(playerFile.readline())})
                    self.players[count-1].luck.update({'rare':float(playerFile.readline())})
                    self.players[count-1].luck.update({'epic':float(playerFile.readline())})
                    self.players[count-1].luck.update({'legendary':float(playerFile.readline())})
                    playerFile.readline() # eat up the actions line, now read in actions
                    line = playerFile.readline().strip() #save it and check if its not the next set of stuff
                    while line != "conditions":
                        line = playerFile.readline().strip()
                    while line != "equipment":
                        line = playerFile.readline().strip() # REPLACEME here if it wasn't equipment then you would start reading, so if an action took 5 lines to represent we want 5 readlines then go back to the top, ending with a line = playerFile, 
                        #note that the first read in would actually be action.attribute = line                    
                    while line != "traits":
                        line = playerFile.readline().strip()
                    while line != "relics":
                        line = playerFile.readline().strip()
            except Exception as e:
                print(e)
                loop = False # we no longer found a file so we break out
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
                    playerFile.write(f"{x.__class__.__name__}\n{x.user}\n{x.health}\n{x.maxHealth}\n{x.speed}\n")
                    playerFile.write(f"{x.xp}\n{x.xpMult}\n{x.block}\n{x.blockMult}\n{x.critChance}\n{x.critDmgMult}\n{x.healingMult}\n")
                    for key in x.dmgInMult.keys():
                        playerFile.write(str(x.dmgInMult[key]) + "\n")
                    
                    for key in x.dmgOutMult.keys():
                        playerFile.write(str(x.dmgOutMult[key]) + "\n")
                    
                    for key in x.luck.keys():
                        playerFile.write(str(x.luck[key]) + "\n")
                        
                    playerFile.write("actions\n") # NOTEME may be able to only read in the items, class and ignore xpMult, actions, etc since they could be automatically calculated? that may be harder though
                    for y in range(len(x.actions)): # NOTEME actions should be giving out strings may need str()
                        playerFile.write(x.actions[y] + "\n")
                    
                    playerFile.write("conditions\n") # NOTEME conditions is likely a 2D array
                    for y in range(len(x.actions)):
                        playerFile.write(x.actions[y] + "\n")
                        
                    playerFile.write("equipment\n") # REPLACEME still need to do relics and such  
                    for y in range(len(x.equipment)):
                        playerFile.write(x.equipment[y] + "\n")
                    
                    playerFile.write("traits\n")
                    for y in range(len(x.traits)):
                        playerFile.write(x.traits[y] + "\n")
                        
                    playerFile.write("relics\n")
                    for y in range(len(x.relics)):
                        playerFile.write(x.relics[y] + "\n")
                count+=1
        print("Players saved to file")
        
    def viewPlayers(self):
        if(len(self.players) == 0):
            return "There are no current players."
        string = "Viewing current players:\n"
        for x in self.players:
            string += f"\t{x.user} as the **{x.__class__.__name__}**\n"
        return string
    def viewClass(self, user): # prints everything
        for x in self.players:
            if(x.user == user):
                return str(x)
    def viewClassShort(self, user):
        for x in self.players:
            if(x.user == user):
                return f"**{x.__class__.__name__}**\nPlayer: {x.user}\nHealth: {x.health}/{x.maxHealth}\nSpeed: {x.speed}\nXP: {x.xp}\nActions:\n{x.actions}"  
    def add(self, user, className):
        for x in self.players:
            if(x.user == user):
                return False
        match className:
            case "Doctor":
                self.players.append(player.Doctor(user))
            case "Scientist":
                self.players.append(player.Scientist(user))
            case _:
                print("No corresponding class found")
        return True
    def addFromDropdown(self, user, className): # Add to here anytime you add a new class
        if(self.add(user, className)):
            print(f"{className} assigned to {user}")
            return f"You have been assigned **{className}**."
        else:
            print(f"{className} attempted to be assigned to {user}. Failed.")
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