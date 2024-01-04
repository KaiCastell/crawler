#import discord
#from discord.ext import commands
#from dotenv import load_dotenv
from entityDir import playerlist, enemy
from structureDir import map


name = "featherjoe" #filler since its just me here, should be constant but im reusing code for convenience
players = playerlist.PlayerList()
testRoom = map.Room(0, "No description", "test small")

userInputString = input("Enter function: ")
args = userInputString.split()

while(args[0] != "end"):

    match(args[0]): #### please note that all args[x] will be one shift off of what the real main has

        # VIEW COMMANDS ########################################################
        case "view":
            match(args[1]):
                case "character":
                    try:
                        if(args[2] == "short"):
                            print(f"Viewing abridged version of {name}'s class:\n{players.viewClassShort(name)}")
                        else: #if you get here that should mean there is a args[1] but it wasn't short
                            print(f"This is not an available command. Try '>view commands' for help.")
                    except Exception as e:
                        print(e)
                        print(f"Viewing {name}'s class:\n{players.viewClass(name)}")
                case "commands":
                    pass # REPLACEME This is the help function
                case "players":
                    print(players.viewPlayers())
                case "classes":
                    pass # NOTEME Not necessary to fill here tbh, works on the main but the dropdown doesn't exist here
                    #print("View class for a detailed description: \n", view=classViewDropdownView())
                case "map":
                    print(testRoom.print())
                case "tile":
                    entity = testRoom.findTile(args[2])
                    if(entity == "NULL"):
                        print("The tile you are trying to view was not found. Please try again with this syntax: view tile [character]")
                    else:
                        print("The tile accessed is shown below:\n" + entity.shortPrint())
                case _:
                    print(f"This is not an available command. Try '>view commands' for help.")

        # CREATE COMMANDS #######################################################
        case "create":
            match(args[1]):
                case("character"):
                    players.addFromDropdown(name, args[2]) #NOTEME needs specific input of Doctor or Scientist atm
                case "entity":
                    match(args[2]):
                        case "self": #create self is the spawn player on map
                            testRoom.spawnEntity(players.getSelf(name)) 
                        case "testEnemy":
                            lobster = enemy.Lobster()
                            testRoom.spawnEntity(lobster)
                    print(testRoom.print())

        # ACTION COMMANDS #######################################################
        case "do":
            match(args[1]):
                case "commands":
                    pass #REPLACEME This is the help function
                case "move":
                    if args[2] == "admin":
                        print(testRoom.moveEntity(int(args[3]), int(args[4]), int(args[5]), int(args[6])))
                    else:
                        try:
                            print(players.getSelf(name).move(testRoom, int(args[2]), int(args[3])))
                        except Exception as e:
                            print(e)

        # OTHER COMMANDS ########################################################
        case "save":
            players.save()
            print(f"You have saved.")
        
        case "reset":
            players.reset()
            print("Players have been reset.")


    userInputString = input("Enter function: ")
    args = userInputString.split()