import discord
from discord.ext import commands

class UtilCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx, *, arg):
        await ctx.send(f"{arg}")

def setup(client):
    client.add_cog(UtilCog(client))
