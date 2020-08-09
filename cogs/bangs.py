import aiohttp
from discord.ext import commands
import time

class Bangs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.CommandNotFound):
            if ctx.message.content.startswith(f"{ctx.prefix}!"):
                ctx.timer = time.time()
                ctx.iscallback = True
                ctx.command = self.client.get_command("!")
                await ctx.command.callback(self, ctx)

    async def resolve_bang(self, ctx, bang, args):
        async with aiohttp.ClientSession() as session:
            params = {"q": "!" + bang + " " + args, "format": "json", "no_redirect": 1}
            url = "https://api.duckduckgo.com"
            async with session.get(url, params=params) as response:
                data = await response.json(content_type=None)
                location = data.get("Redirect")
                if location == "":
                    return await ctx.send(":warning: Unknown bang or found nothing!")

                while location:
                    response = await session.get(location)
                    location = response.headers.get("location")

                await ctx.send(response.url)

    @commands.command(name="!")
    async def bang(self, ctx):
        if not hasattr(ctx, "iscallback"):
            return await ctx.send_help(ctx.command)

        await ctx.trigger_typing()
        try:
            bang, args = ctx.message.content[len(ctx.prefix) + 1 :].split(" ", 1)
            if len(bang) != 0:
                await self.resolve_bang(ctx, bang, args)
        except ValueError:
            await ctx.send("Please search something! If you aren't sure how to use duckduckgo bangs, check out this link: https://duckduckgo.com/bangs")

def setup(client):
    client.add_cog(Bangs(client))
