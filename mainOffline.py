# Minor random gaining for roguelike but high strategy (die face movement determines effect or cards or something?)
# Hidden map and the goal is to find the exit with everyone else
# Simplify the combat system into some way (try to have reduced complexity and reduced randomness)
# combat comes in the form of a resource cost (health, mana, time ?)
# abilities, passives, and directional effects. no cards

#import discord
#from discord.ext import commands
#from dotenv import load_dotenv
from structureDir import game_module

name = "featherjoe" #filler since its just me here, should be constant but im reusing code for convenience
board = None

userInputString = input("Enter function: ")
args = userInputString.split()

while(args[0] != "end"):

    match(args[0]): #### please note that all args[x] will be one shift off of what the real main has

        # VIEW COMMANDS ########################################################
        case "view":
            match(args[1]):
                case "self":
                    themself = game.getPlayer(name)
                    try:
                        if(args[2] == "short"):
                            print(f"Viewing abridged version of {name}'s class:\n{game.viewClassShort(name)}")
                        else: #if you get here that should mean there is a args[1] but it wasn't short
                            print(f"This is not an available command. Try '>view commands' for help.")
                    except Exception as e:
                        print(e)
                        print(f"Viewing {name}'s class:\n{game.viewClass(name)}")
                case "commands":
                    pass # REPLACEME This is the help function
                case "players":
                    print(game.viewPlayers())
                case "classes":
                    pass # NOTEME Not necessary to fill here tbh, works on the main but the dropdown doesn't exist here
                    #print("View class for a detailed description: \n", view=classViewDropdownView())
                case "board":
                    print(game.viewBoard())
                case "room":
                    print(f"{game.viewRoom(name)}")
                case _:
                    print(f"This is not an available command. Try '>view commands' for help.")

        # CREATE COMMANDS #######################################################
        case "create":
            match(args[1]):
                case("character"):
                    game.addFromDropdown(name, args[2]) #NOTEME needs specific input of Doctor or Scientist atm
                case "entity":
                    match(args[2]):
                        case "self": #create self is the spawn player on map
                            pass
                        case "testEnemy":
                            pass
                case "game":
                    game = game_module.Game("test")
                    print(game.viewBoard())

        # ACTION COMMANDS #######################################################
        case "do":
            match(args[1]):
                case "commands":
                    pass #REPLACEME This is the help function
        case "move":
            match(args[1]):
                case "commands":
                    pass #REPLACEME This is the help function
                case _:
                    if(args[1] == "1" or args[1] == "2" or args[1] == "3" or args[1] == "4"):
                        print(game.movePlayer(name, args[1]))
                    else:
                        print(f"This is not an available command. Try '>map commands' for help.")

        # OTHER COMMANDS ########################################################
        case "save":
            game.save()
            print(f"You have saved.")
        
        case "reset":
            game.reset()
            print("Players have been reset.")


    userInputString = input("Enter function: ")
    args = userInputString.split()