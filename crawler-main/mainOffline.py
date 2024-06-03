# Minor random gaining for roguelike but high strategy (die face movement determines effect or cards or something?)
# Hidden map and the goal is to find the exit with everyone else
# Simplify the combat system into some way (try to have reduced complexity and reduced randomness)
# combat comes in the form of a resource cost (health, mana, time ?)
# abilities, passives, and directional effects. no cards

#import discord
#from discord.ext import commands
#from dotenv import load_dotenv
from entityDir import playerlist
from structureDir import gameLoop

name = "featherjoe" #filler since its just me here, should be constant but im reusing code for convenience
playerList = playerlist.PlayerList()
board = None

userInputString = input("Enter function: ")
args = userInputString.split()

while(args[0] != "end"):

    match(args[0]): #### please note that all args[x] will be one shift off of what the real main has

        # VIEW COMMANDS ########################################################
        case "view":
            match(args[1]):
                case "self":
                    themself = playerList.getPlayer(name)
                    try:
                        if(args[2] == "short"):
                            print(f"Viewing abridged version of {name}'s class:\n{playerList.viewClassShort(name)}")
                        elif(args[2] == "hand"):
                            print(f"Viewing {name}'s hand:\n{themself.hand}")
                        elif(args[2] == "deck"):
                            print(f"Viewing {name}'s hand:\n{themself.deck}")
                        else: #if you get here that should mean there is a args[1] but it wasn't short
                            print(f"This is not an available command. Try '>view commands' for help.")
                    except Exception as e:
                        print(e)
                        print(f"Viewing {name}'s class:\n{playerList.viewClass(name)}")
                case "commands":
                    pass # REPLACEME This is the help function
                case "players":
                    print(playerList.viewPlayers())
                case "classes":
                    pass # NOTEME Not necessary to fill here tbh, works on the main but the dropdown doesn't exist here
                    #print("View class for a detailed description: \n", view=classViewDropdownView())
                case "board":
                    print(board)
                case "room":
                    print(f"{game.viewRoom(name)}")
                case _:
                    print(f"This is not an available command. Try '>view commands' for help.")

        # CREATE COMMANDS #######################################################
        case "create":
            match(args[1]):
                case("character"):
                    playerList.addFromDropdown(name, args[2]) #NOTEME needs specific input of Doctor or Scientist atm
                case "entity":
                    match(args[2]):
                        case "self": #create self is the spawn player on map
                            pass
                        case "testEnemy":
                            pass
                case "board":
                    game = gameLoop.game(playerList, "test")
                    print(board)

        # ACTION COMMANDS #######################################################
        case "do":
            match(args[1]):
                case "commands":
                    pass #REPLACEME This is the help function

        # OTHER COMMANDS ########################################################
        case "save":
            playerList.save()
            print(f"You have saved.")
        
        case "reset":
            playerList.reset()
            print("Players have been reset.")


    userInputString = input("Enter function: ")
    args = userInputString.split()