#!/usr/bin/env python3
import dotenv
import os
import sys
dotenv.load_dotenv(verbose=True)
TOKEN = os.getenv("TOKEN")

import time

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
print(f"Discord.py Version: {discord.__version__}")

#----------------------Header------------------------
client = commands.Bot(command_prefix = '&')
client.remove_command('help')
#----------------------Commands----------------------
# The commands in this section should, at some point, be moved to the appropriate cog.
@client.command()
async def ping(ctx):
    """Ping the bot"""
    await ctx.send(f"Pong :zany_face: **{round(client.latency * 1000)} ms**")
@client.event
async def on_message(message):
    """Responds to "stfu" with "no u" """
    if message.content.startswith("stfu") and message.content.endswith("stfu"):
        await message.channel.send("no u")
    await client.process_commands(message)
@client.event
async def on_message(message):
    """Reacts with a wave emote to hi or hello and stuff"""
    if message.content.startswith(("Hey ", "Hello ", "Hi ", "Sup ", "Oi ", "yo ", "hey ", "hello ", "hi ", "sup ", "oi ", "yo ")):
        await message.add_reaction("👋")
    await client.process_commands(message)
#----------------------Dying-------------------------
@client.command()
@commands.is_owner()
async def stop(ctx):
    """Stop the bot and start the manager"""
    try:
        await ctx.send("Informing manager...")
        print("Stopping bot...")
        time.sleep(1.23)
        await ctx.send("Recieved SIGTERM, dying.")
        print("Changing status...")
        await client.change_presence(status=discord.Status.idle) # Back to idle for manager. Move to manager script?
        sys.exit()
    except SystemExit:
        sys.exit()
    except:
        print("Unable to stop bot.")
        await ctx.send("Unable to stop bot.")
#----------------------Cogs--------------------------
extensions = [
    "developer", # non functioning atm, intended for developer only commands
    # "easter", # adds some easter eggs, although currently does nothing
    "info", # adds functions like "github" or "liscence"
    "util" #non functioning atm, intended for random utility commands
]
if __name__ == "__main__":
    print("\nLoading cogs:")
    for extension in extensions:
        #try:
        client.load_extension(f"cogs.{extension}")
        print(f"\tLoaded {extension}")
        #except:
        #    print(f"\tError loading {extension}")
    print("")
#----------------------Start-------------------------
@client.event
async def on_connect():
    print("Connected. Readying...")
@client.event
async def on_ready():
    print("Changing status...")
    time.sleep(0.5)
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="gay porn"))
    print(f"Ready. Logged in as {client.user.name}")
@client.event
async def on_disconnect():
    print("Disconnected.\a")
#----------------------Footer------------------------
client.run(TOKEN)
