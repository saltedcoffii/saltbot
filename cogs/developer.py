import discord
from discord.ext import commands

class DeveloperCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.is_owner()
    async def null():
        return None

def setup(client):
    client.add_cog(DeveloperCog(client))
