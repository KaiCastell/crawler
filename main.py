import discord
import os
import playerlist
import map
from discord.ext import commands
from dotenv import load_dotenv
# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='>', intents=intents)

#################################### OTHER INITIALIZATIONS ##############################################

players = playerlist.PlayerList()
testRoom = map.Room(0, "No description")
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
    players.save()
    print(f'Disconnected from {bot.user.name}')


# Admin Commands # # # # # # # # # # # # # # # # # # # #

@bot.command()
@commands.has_permissions(administrator=True) #only big hoss can do this
async def admin(ctx: commands.Context, *args):
    name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "create":
                match(args[1]):
                    case "entity":
                        match(args[2]):
                            case "self": #create self is the spawn player on map
                                testRoom.spawnEntity(players.getSelf(name)) 
                                await ctx.channel.send(testRoom.print())
            case _:
                await ctx.channel.send("Try again.")


# Non-Admin Commands # # # # # # # # # # # # # # # # # # # #

# Create Commands #

@bot.command()
async def create(ctx: commands.Context, arg):
    #name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(arg):
            case "character": # character creation
                await ctx.channel.send("Select class: \n", view=classSelectDropdownView()) #ctx.send is also valid
            case"commands":
                pass # REPLACEME with the help stuff
            case _:
                await ctx.channel.send(f"This is not an available command. Try '>choose commands' for help.")


# View Commands #

@bot.command()
async def view(ctx: commands.Context, *args): #all view commands, listed out into a switch case
    name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "character":
                try:
                    if(args[1] == "short"):
                        await ctx.channel.send(f"Viewing {name}'s class:\n{players.viewClassShort(name)}")
                    else: #if you get here that should mean there is a args[1] but it wasn't short
                        await ctx.channel.send(f"This is not an available command. Try '>view commands' for help.")
                except:
                    await ctx.channel.send(f"Viewing {name}'s class:\n{players.viewClass(name)}")
            case "commands":
                pass # REPLACEME This is the help function
            case "players":
                await ctx.channel.send(players.viewPlayers())
            case "classes":
                await ctx.channel.send("View class for a detailed description: \n", view=classViewDropdownView())
            case "map":
                await ctx.channel.send(testRoom.print())
            case _:
                await ctx.channel.send(f"This is not an available command. Try '>view commands' for help.")

# Do Commands #

@bot.command()
async def do(ctx: commands.Context, *args): #all view commands, listed out into a switch case
    name = ctx.author.name
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        match(args[0]):
            case "commands":
                pass #REPLACEME This is the help function
            case "move":
                await ctx.channel.send(players.getSelf(name).move(testRoom, int(args[1]), int(args[2])))
            case _:
                await ctx.channel.send(f"This is not an available command. Try '>map commands' for help.")




# Other Commands #

@bot.command()
async def save(ctx: commands.Context):
    if(ctx.channel.name == 'crawler'): #only respond to the command if it was in the crawler channel
        players.save()
        await ctx.channel.send(f"You have saved.") #NOTEME REPLACEME there isn't a map save on this function yet. only calls player save

@bot.command()
@commands.has_permissions(administrator=True) #only big hoss can do this
async def reset(ctx: commands.Context):
    if(ctx.channel.name == 'crawler'):
        players.reset()
        print("Players have been reset.")
        await ctx.channel.send(f"You have reset.") #NOTEME REPLACEME no map reset here yet. or the game reset for that matter
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

class classSelectDropdown(discord.ui.Select): # this is the dropdown selection, but not the view
    def __init__(self):
        options=[
            discord.SelectOption(label="Scientist", description = "Does the sciencing. Is that a word?"),
            discord.SelectOption(label="Doctor", description = "JETT REVIVE ME")        
        ]
        super().__init__(placeholder="Choose a class.", options = options, min_values=1, max_values=1)
    
    async def callback(self, interaction: discord.Interaction):
        name = interaction.user.name
        className = self.values[0]
        await interaction.response.send_message(players.addFromDropdown(name, className), ephemeral=True)
            #case _: this is the default
            
class classSelectDropdownView(discord.ui.View): #this is the dropdown viewing
    def __init__(self):
        super().__init__()
        self.add_item(classSelectDropdown())


# Class View #

class classViewDropdown(discord.ui.Select): # this is the dropdown selection, but not the view
    def __init__(self):
        options=[
            discord.SelectOption(label="Scientist", description = "Does the sciencing. Is that a word?"),
            discord.SelectOption(label="Doctor", description = "JETT REVIVE ME")        
        ]
        super().__init__(placeholder="View a class.", options = options, min_values=1, max_values=1)
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(playerlist.classDescription(self.values[0]), ephemeral=True)
            #case _: this is the default
            
class classViewDropdownView(discord.ui.View): #this is the dropdown viewing
    def __init__(self):
        super().__init__()
        self.add_item(classViewDropdown())


############################## BOT START ###########################################
# always at the end
# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))