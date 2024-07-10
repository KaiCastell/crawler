# game loop needs to not care about character action when there are no enemies and care when there are...
# needs to wait for input from the main. basically the response master

# does anything for the board state and game state

# also prints out the board and holds the entities

from structureDir.board_module import Board
from structureDir.playerlist_module import PlayerList

class Game(Board, PlayerList):
    def __init__(self, seed):
        PlayerList.__init__(self) # adds the player info needed for the board
        Board.__init__(self, self.players, seed)
        self.turn = 0
    def movePlayer(self, name, decision):
        return super().movePlayer(super().getPlayer(name), decision)
    def whosTurn(self):
        return self.getTurn(self.turn) #returns the player object
