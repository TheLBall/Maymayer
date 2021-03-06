import discord
from discord.ext import commands
from .utils import checks
import sys

class General():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        '''Says pong. Used for tests.'''
        await ctx.send("Pong! :ping_pong:")

    #credits to NanoBot for a little bit of this
    @commands.command()
    async def info(self, ctx):
        '''Shows info about Maymayer.'''
        pyver = ""
        for x in sys.version_info[0:3]:
            if x == sys.version_info[2]:
                pyver += str(x)
            else:
                pyver += str(x) + "."
        if ctx.message.guild is not None:
            color = ctx.message.guild.me.color
        users = sum(1 for _ in self.bot.get_all_members())
        embed = discord.Embed(color=color, title="Maymayer Info", description="Created by Luki. Maintained by TheLBall.")
        embed.set_footer(text="wanna join my free giftcard giveaway?")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Stats: ", value="Servers: **{}** • Users: **{}**".format(len(self.bot.guilds), users))
        embed.add_field(name="Version: ", value="Maymayer: **2.0.1** • discord.py: **{}** • Python: **{}**".format(discord.__version__, pyver))
        embed.add_field(name="Other: ", value = "Discord: https://discord.gg/GzNH2sB")
        await ctx.send(embed=embed)

    @commands.command()
    async def server(self, ctx):
        '''Gives an invite to the official Maymayer server.'''
        await ctx.message.author.send("https://discord.gg/GzNH2sB")
        await ctx.send("**I sent an invite to my server in your DMs.**")

    @commands.command(name = "shutdown", hidden = True)
    @checks.is_owner()
    async def _shutdown(self, ctx):
        '''Shuts the bot down'''
        await ctx.send("RIP <@367072821160968194> 2017-2017")
        try:
            await self.bot.logout()
        except:
            log.warn("Maymayer couldn't die.")

    @commands.command()
    async def invite(self, ctx):
        '''Gives a bot invite.'''
        await ctx.message.author.send("https://discordapp.com/oauth2/authorize?client_id=367072821160968194&scope=bot&permissions=2146958591")

def setup(bot):
    bot.add_cog(General(bot))
