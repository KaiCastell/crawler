# game loop needs to not care about character action when there are no enemies and care when there are...
# needs to wait for input from the main. basically the response master

# does anything for the board state and game state

# also prints out the board and holds the entities

from entityDir import playerlist, enemy

class board: #this is for the current game board
    turn = 1
    # extra board effects variable? like burning or idk stuff
    def __init__(self, playerList, allyList, difficulty):
        self.playerList = playerList
        self.allyList = allyList
        self.enemyList = []
        if(difficulty == 0): #there should never be difficulty 0, hence this is for a test board
            lobster = enemy.Lobster()
            self.enemyList.append(lobster)
        else: # this is where you create a board based on the difficulty number provided
            pass

    def declareIntents(self):
        pass

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
        
    def __str__(self): #prints the game state / the board . try not to exceed 70 characters
        # enemy printing # # # # # # # # #
        strNames = ""
        strHealth = ""
        strBlock = ""
        strIntent = ""
        strEnd = ""
        for x in self.enemyList:
            strEnd += "* * * * * * * * *  "
        for x in self.enemyList:
            strNames += "* " + self.adjustName(x.name, False) + " *  " # NOTEME adjust for up to 4 on a row max 
        for x in self.enemyList:
            temp = f"{x.health}/{x.maxHealth}"
            temp = "{:^13}".format(temp)
            temp = "* " + temp + " *  "
            strHealth += temp
        for x in self.enemyList:
            temp = "{:^13}".format(x.block)
            temp = "* " + temp + " *  "
            strBlock += temp
        strReturn = f"```{strNames}\n{strHealth}\n{strBlock}\n{strEnd}\n\n\n"

        # player printing # # # # # # # # #
        strEnd = ""
        strNames = ""
        strHealth = ""
        strBlock = ""
        # note each block should be "* 13-characters *"
        for x in self.playerList:
            strEnd += "* * * * * * * * *  "
        for x in self.playerList:
            strNames += "* " + self.adjustName(x.name, False) + " *  " # up to 4 player max
        for x in self.playerList:
            temp = f"{x.health}/{x.maxHealth}"
            temp = "{:^13}".format(temp)
            temp = "* " + temp + " *  "
            strHealth += temp
        for x in self.playerList:
            temp = "{:^13}".format(x.block)
            temp = "* " + temp + " *  "
            strBlock += temp
        strReturn += f"{strEnd}\n{strNames}\n{strHealth}\n{strBlock}```"
        return strReturn