# game loop needs to not care about character action when there are no enemies and care when there are...
# needs to wait for input from the main. basically the response master

# does anything for the board state and game state

# also prints out the board and holds the entities

import os
import sys

#this here is a generic solution to importing within the same folder issues
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


from structureDir.board_module import Board
from structureDir.playerlist_module import PlayerList

class Game(Board, PlayerList):
    def __init__(self, seed):
        PlayerList.__init__(self) # adds the player info needed for the board
        Board.__init__(self, seed)  
        self.turn = 0
        
    def movePlayer(self, name, decision):
        return super().movePlayer(super().getPlayer(name), decision)
    
    def whosTurn(self):
        return self.getTurn(self.turn) #returns the player object
    
    def save(self):
        PlayerList.save(self)
        Board.save(self)
        return "You have saved the current game."
        
    def load(self):
        PlayerList.load(self)
        Board.load(self)
        return "You have loaded a previous game."
        
    def reset(self):
        self.players = []
        self.rooms = []
        return "You have reset the game. The save is still preserved."
        
    def boardFix(self): # only use to fix the load for board, should overwrite the empty one in board_module
        try:
            if(len(self.rooms) == 0):
                raise Exception
            for x in self.rooms:
                for i in range(len(x.pathways)):
                    if x.pathways[i] == -1:
                        x.pathways[i] = None
                    else:
                        x.pathways[i] = self.getRoom(x.pathways[i])
                for i in range(len(x.players)):
                    x.players[i] = self.getPlayer(x.players[i])
            print("Board fixed\n")
        except: #Exception as e: 
            # means there was no board made so oh well
            #print(e)
            print("No board to fix\n")
            return
    
    def addPlayer(self, name, className): # override so that we can check is the board already exists
        if(len(self.rooms) == 0):
            return ("You cannot create a character if the game has already started.")
        return PlayerList.addPlayer(self, name, className)