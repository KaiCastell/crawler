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

game = None
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
                        await ctx.channel.send(game.viewBoard())
            case _:
                await ctx.channel.send("Try again.")
                
@bot.command()
@commands.has_permissions(administrator=True) #only big hoss can do this
async def reset(ctx: commands.Context):
    if(ctx.channel.name == 'crawler'):
        game.reset()
        print("Players have been reset.")
        await ctx.channel.send(f"You have reset.") #NOTEME REPLACEME no map reset here yet. or the game reset for that matter

# Non-Admin Commands # # # # # # # # # # # # # # # # # # # # # # # # #

# Create Commands #

@bot.command()
async def create(ctx: commands.Context, arg):
    #name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(arg):
            case "character": # character creation
                await ctx.channel.send("Select a class: \n", view=ClassSelectDropdownView()) #ctx.send is also valid
            case "commands":
                pass # REPLACEME with the help stuff
            case "testg":
                global game # a necessary evil apparently, because otherwise python will bind this locally
                print("Creating test game")
                game = game_module.Game("test")
                print("Game created.")
                send = f"```Test game created with:\n{game.viewPlayers()}\n\n{game.viewBoard()}\nIt is {game.whosTurn().name}'s turn\nUse >view room to see your next actions```"
                await ctx.channel.send(send)
                print("Game created successfully")
            case "board":
                pass
            case _:
                await ctx.channel.send(f"This is not an available command. Try '>choose commands' for help.")



# View Commands #

@bot.command()
async def view(ctx: commands.Context, *args): #all view commands, listed out into a switch case
    name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "self":
                await ctx.channel.send(f"Viewing {name}:\n{str(game.getPlayer(name))}")
            case "commands":
                pass # REPLACEME This is the help function
            case "players":
                string = "Viewing current players:\n"
                string += game.viewPlayers()
                await ctx.channel.send(string)
            case "classes":
                await ctx.channel.send("View class for a detailed description: \n", view=classViewDropdownView())
                pass
            case "room":
                await ctx.channel.send(f"```{game.viewRoom(name)}```")
            case _: #REPLACEME to check another player's hand etc. use the defaults to check and then finally give help
                await ctx.channel.send(f"This is not an available command. Try '>view commands' for help.")


# Do Commands #

@bot.command()
async def do(ctx: commands.Context, *args): #all view commands, listed out into a switch case
    name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "commands":
                pass #REPLACEME This is the help function
            case _:
                await ctx.channel.send(f"This is not an available command. Try '>map commands' for help.")

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
                    await ctx.channel.send(f"```{game.movePlayer(name, args[0])}```")
                else:
                    await ctx.channel.send(f"This is not an available command. Try '>map commands' for help.")

# Other Commands #

@bot.command()
async def save(ctx: commands.Context):
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        game.save()
        await ctx.channel.send(f"You have saved.") #NOTEME REPLACEME there isn't a map save on this function yet. only calls player save


@bot.event # exception handler for the missingPermissions
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        print("Admin command attempted by " + ctx.author.name)
        await ctx.send("Sorry, you don't have permission to do that. You must be an admin.")

@bot.command(name = 'commands') 
async def commandResponse(ctx):
    await ctx.send(f"Current commands are view (for information), create (game start related commands), and do (character control)")
    #REPLACE ME with more fancy text later please

################################### DROPDOWN STUFF ######################################################

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

############################## BOT START ###########################################
# always at the end
# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))