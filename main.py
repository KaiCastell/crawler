import discord
import os
from discord.ext import commands
from dotenv import load_dotenv



#################################### OTHER INITIALIZATIONS ##############################################

# nearby function imports

from mainCalls import call


# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=',', intents=intents)


# command example
"""@bot.command()
#@commands.has_permissions(administrator=True) #only big hoss can do this
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
                await send(ctx, "Try again.")"""

#################################### EVENTS ###########################################

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
@bot.event
async def on_disconnect():
    print(f'Disconnected from {bot.user.name}')
    
@bot.event # exception handler for the missingPermissions
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Command not found. Probably a typo.")

################################ ######## ###########################################################
################################ COMMANDS ###########################################################
################################ ######## ###########################################################

@bot.command()
async def roll(ctx:commands.Context, *args):
    arguments = ' '.join(args)
    await ctx.send(call.roll(arguments))
    

############################## UTILITY FUNCTIONS ###################################

"""async def send(ctx, string): # not good apparently
    temp = "```\n"
    if isinstance(string, str):
        temp += string
    else:
        temp += await string  # await the coroutine to get its result
    temp += "\n```"
    await ctx.channel.send(temp)"""


############################## BOT START ###########################################
# always at the end
# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))