import discord
from discord.ext import commands

class InfoCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def github(self, ctx):
        await ctx.send("https://github.com/saltedcoffii/saltbot")
        await ctx.send("Have fun and send patches!!")
        print(f"{ctx.message.author} requested the bot's github.")

    @commands.command()
    async def license(self, ctx):
        embed=discord.Embed(title="GNU Affero General Public License v3.0", description="Permissions of this strongest copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. When a modified version is used to provide a service over a network, the complete source code of the modified version must be made available.", color=0xffffff)
        embed.set_thumbnail(url="https://www.clipartmax.com/png/middle/231-2314001_legal-center-or-law-advocate-icon-with-symbol-of-justice-weighing-scale.png")
        embed.add_field(name="Permissions", value="✅ Commercial\n✅ Modification\n✅ Distribution\n✅ Patent Use\n✅ Private Use", inline=True)
        embed.add_field(name="Limitations", value="❌ Liability\n❌ Warranty", inline=True)
        embed.add_field(name="Conditions", value="ℹ License and copyright notice\nℹ State changes\nℹ Disclose source\nℹ Network use is distrobution\nℹ Same license", inline=True)
        embed.set_footer(text="This is not legal advice. The full license may be found within the bot's source code.")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(InfoCog(client))
