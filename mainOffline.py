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
game = game_module.Game("saved") # need one at the start so characters can be created at any time

userInputString = input("Enter function: ")
args = userInputString.split()

while(args[0] != "end"):

    match(args[0]): #### please note that all args[x] will be one shift off of what the real main has

        # VIEW COMMANDS ########################################################
        case "view":
            match(args[1]):
                case "self":
                    print(str(game.getPlayer(name)))
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
                    print(game.addPlayer(name, args[2])) #NOTEME needs specific input of Doctor or Scientist atm
                case "test":
                    temp = game.seed("test")
                    temp += (f"\n{game.viewPlayers()}\n\n{game.viewBoard()}\n")
                    temp += (f"It is {game.whosTurn().name}'s turn\nUse >view room to see your next actions")
                    print(temp)
                case "game":
                    print(game.seed("random"))

        # ACTION COMMANDS #######################################################
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
            print(game.save())
        
        case "reset":
            print(game.reset())
            
        case "load":
            print(game.load())


    userInputString = input("Enter function: ")
    args = userInputString.split()