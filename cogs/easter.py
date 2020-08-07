import discord
from discord.ext import commands

class EasterCog(commands.Cog):
    def __init__(self, client):
        self.client = client
# FIXME
    @client.event
    async def on_message(message):
        if message.content.startswith("stfu") and message.content.endswith("stfu"):
            await message.channel.send("no u")
        await client.process_commands(message)

def setup(client):
    client.add_cog(EasterCog(client))
