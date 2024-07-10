import discord
import os
from structureDir import game_module
from discord.ext import commands
from dotenv import load_dotenv
# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='>', intents=intents)

#################################### OTHER INITIALIZATIONS ##############################################

game = game_module.Game("saved")

# filing, note that, a is append, r is read, w is write, x creates a new file, second character t for text (default), b for binary

# Set the confirmation message when the bot is ready

#################################### ON READY AND DISCONNECT ###########################################

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # read in location/map

    # read in players (could be infinite? i guess?)
    
@bot.event
async def on_disconnect():
    game.save()
    print(f'Disconnected from {bot.user.name}')

# Admin Commands # # # # # # # # # # # # # # # # # # # # # # # # # #

@bot.command()
@commands.has_permissions(administrator=True) #only big hoss can do this
async def admin(ctx: commands.Context, *args):
    # name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "create":
                pass
            case "view":
                match(args[1]):    
                    case "board":
                        print("Board view called")
                        await send(ctx, game.viewBoard())
            case _:
                await send(ctx, "Try again.")
                
@bot.command()
@commands.has_permissions(administrator=True) #only big hoss can do this
async def reset(ctx: commands.Context):
    if(ctx.channel.name == 'crawler'):
        await send(ctx, game.reset()) #NOTEME REPLACEME no map reset here yet. or the game reset for that matter
        
@bot.command()
@commands.has_permissions(administrator=True) #only big hoss can do this
async def load(ctx: commands.Context):
    if(ctx.channel.name == 'crawler'):
        await send(ctx, game.load()) #NOTEME REPLACEME no map reset here yet. or the game reset for that matter

# Non-Admin Commands # # # # # # # # # # # # # # # # # # # # # # # # #

# Create Commands #

@bot.command()
async def create(ctx: commands.Context, *args):
    name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "character": # character creation
                await send(ctx, game.addPlayer(name, args[1]))
                #await send(ctx, "Select a class: \n", view=ClassSelectDropdownView()) #ctx.send is also valid
                pass
            case "commands":
                pass # REPLACEME with the help stuff
            case "test":
                temp = game.seed("test")
                temp +=  (f"\n{game.viewPlayers()}\n\n{game.viewBoard()}\n")
                temp += (f"It is {game.whosTurn().name}'s turn\nUse >view room to see your next actions")
                await send(ctx, temp)
            case "board":
                pass
            case _:
                await send(ctx, f"This is not an available command. Try '>choose commands' for help.")



# View Commands #

@bot.command()
async def view(ctx: commands.Context, *args): #all view commands, listed out into a switch case
    name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "self":
                await send(ctx, f"Viewing {name}:\n{str(game.getPlayer(name))}")
            case "commands":
                pass # REPLACEME This is the help function
            case "players":
                await send(ctx, game.viewPlayers())
            case "classes":
                #await send(ctx, "View class for a detailed description: \n", view=classViewDropdownView())
                pass
            case "room":
                await send(ctx, f"{game.viewRoom(name)}")
            case _: #REPLACEME to check another player's hand etc. use the defaults to check and then finally give help
                await send(ctx, f"This is not an available command. Try '>view commands' for help.")


# Move Commands #

@bot.command()
async def move(ctx: commands.Context, *args): #all view commands, listed out into a switch case
    name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "commands":
                pass #REPLACEME This is the help function
            case _:
                if(args[0] == "1" or args[0] == "2" or args[0] == "3" or args[0] == "4"):
                    await send(ctx, f"{game.movePlayer(name, args[0])}")
                else:
                    await send(ctx, f"This is not an available command. Try '>map commands' for help.")

# Other Commands #

@bot.command()
async def save(ctx: commands.Context):
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        game.save()
        await send(ctx, f"You have saved.") #NOTEME REPLACEME there isn't a map save on this function yet. only calls player save


@bot.event # exception handler for the missingPermissions
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        print("Admin command attempted by " + ctx.author.name)
        await send(ctx, "Sorry, you don't have permission to do that. You must be an admin.")

@bot.command(name = 'commands') 
async def commandResponse(ctx):
    await send(ctx, f"Current commands are view (for information), create (game start related commands), and do (character control)")
    #REPLACE ME with more fancy text later please

################################### DROPDOWN STUFF ######################################################
"""
# Class Select #

class ClassSelectDropdown(discord.ui.Select): # this is the dropdown selection, but not the view
    def __init__(self):
        options=[
            discord.SelectOption(label="Scientist", description = "Does the sciencing. Is that a word?"),
            discord.SelectOption(label="Doctor", description = "JETT REVIVE ME")        
        ]
        super().__init__(placeholder="Choose a class.", options = options, min_values=1, max_values=1)
    
    async def callback(self, interaction: discord.Interaction):
        name = interaction.user.name
        className = self.values[0]
        await interaction.response.send_message(game.addFromDropdown(name, className), ephemeral=True)
            #case _: this is the default
            
class ClassSelectDropdownView(discord.ui.View): #this is the dropdown viewing
    def __init__(self):
        super().__init__()
        self.add_item(ClassSelectDropdown())

# Class View #

class ClassViewDropdown(discord.ui.Select): # this is the dropdown view
    def __init__(self):
        options=[
            discord.SelectOption(label="Scientist", description = "Does the sciencing. Is that a word?"),
            discord.SelectOption(label="Doctor", description = "JETT REVIVE ME")        
        ]
        super().__init__(placeholder="View a class.", options = options, min_values=1, max_values=1)
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(game.classDescription(self.values[0]), ephemeral=True)
            #case _: this is the default
            
class classViewDropdownView(discord.ui.View): #this is the dropdown viewing
    def __init__(self):
        super().__init__()
        self.add_item(ClassViewDropdown())
"""
############################## UTILITY FUNCTIONS ###################################

async def send(ctx, string):
    temp = "```\n"
    temp += string
    temp += "\n```"
    await ctx.channel.send(temp)


############################## BOT START ###########################################
# always at the end
# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))