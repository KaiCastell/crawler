# game loop needs to not care about character action when there are no enemies and care when there are...
# needs to wait for input from the main. basically the response master

# does anything for the board state and game state

# also prints out the board and holds the entities

from structureDir import board as boardfile
from entityDir import playerlist

class game:
    def __init__(self, players, seed):
        self.turn = 0
        self.players = players # this is the actual [] list, not the object.
        self.board = boardfile.Board(players, seed)

    def viewRoom(self, name):
        return str((self.board).getRoom(name))
    def viewBoard(self):
        return str(self.board)
    def whosTurn(self):
        return self.players.getTurn(self.turn) #returns the player object
    def movePlayer(self, name, decision):
        return str((self.board).movePlayer(name, decision))
