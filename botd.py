#!/usr/bin/env python3
import dotenv
import os
import sys
dotenv.load_dotenv(verbose=True)
TOKEN = os.getenv("TOKEN")

import time

import discord
from discord.ext import commands

#----------------------Header------------------------
client = commands.Bot(command_prefix = "&botd ")
client.remove_command('help')
#----------------------Commands----------------------
@client.command()
async def ping(ctx):
    """Ping the bot daemon"""
    await ctx.send(f"*The manager is online. **{round(client.latency * 1000)} ms**.*")
#----------------------Managing main.py--------------
@client.command()
@commands.is_owner()
async def start(ctx):
    """Start main.py"""
    try:
        print("Starting bot...")
        await ctx.send("*Starting bot...*")
        time.sleep(1.23)
        await ctx.send("*Bot started.*")
        os.system("python3 main.py")
        print("Bot stopped.")
        await ctx.send("*Bot stopped.*")
    except:
        print("Error starting main.py")
        await ctx.send("*Unable to start bot.*")
#----------------------Stopping---------------------
@client.command()
@commands.is_owner()
async def stop(ctx):
    """Stop the manager"""
    await ctx.send("*Stopping manager.*")
    sys.exit()
#----------------------Start-------------------------
@client.event
async def on_connect():
    print("Manager connected. Readying...")
@client.event
async def on_ready():
    print("Changing status...")
    await client.change_presence(status=discord.Status.idle)
    print(f"Manager online. Logged in as {client.user.name}")
@client.event
async def on_disconnect():
    print("Manager disconnected.\a")
#----------------------Footer------------------------
client.run(TOKEN)
