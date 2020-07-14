import discord
from discord.ext import commands

from core.cog import cog_base

class react(cog_base): 
    @commands.command()
    async def justice(self, ctx):
        await ctx.send(self.JSON_SETTING['JUSTICE_DANCE'])

    @commands.command()
    async def eddy(self, ctx):
        await ctx.send(self.JSON_SETTING['EDDY_WALLY'])


def setup(bot):
    bot.add_cog(react(bot))