import maps
import player

class Action: #note that mutators will use actions
    pass

def move(user, room, newX, newY):
    print("Made it")
    for x in range(len(room.tileArray)):
        for y in range(len(room.tileArray[x])):
            if(room.tileArray[x][y].entity.user == user):
                return "Found user."
    return "Did not find user."
    