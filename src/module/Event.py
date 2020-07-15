import discord
from discord.ext import commands

from core.cog import cog_base

class Event(cog_base): 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(self.JSON_SETTING['MAIN_TEXT_CHANNEL']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(self.JSON_SETTING['MAIN_TEXT_CHANNEL']))
        await channel.send(f'{member} leave!')

    '''
    TODO 
    '''
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('echo') and msg.author != self.bot.user:
            await msg.channel.send('echo')

def setup(bot):
    bot.add_cog(Event(bot))