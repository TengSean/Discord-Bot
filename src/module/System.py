import discord
from discord.ext import commands
from datetime import datetime as dt

from core.cog import cog_base

class System(cog_base):

    @commands.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'module.{extension}')
        await ctx.send(f'Load {extension} sucessfully!')

    @commands.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'module.{extension}')
        await ctx.send(f'Unload {extension} sucessfully!')

    @commands.command()
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'module.{extension}')
        await ctx.send(f'Reload {extension} sucessfully!')


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)} (ms)')


    @commands.command()
    async def date(self, ctx):
        await ctx.send(f'{dt.today().strftime("%Y-%m-%d %H:%M:%S")}')

    @commands.command()
    async def version(self, ctx):
        await ctx.send(f'Author: {self.JSON_SETTING["AUTHOR"]}\n\
    Version: {self.JSON_SETTING["VERSION"]}\n\
    Repo link: {self.JSON_SETTING["REPO"]}')

    @commands.command()
    async def TODO(self, ctx):
        todo = '''
        TODO
        last update: 2020/07/15
        Something basic:
            [ ] Background service sample: https://github.com/Rapptz/discord.py/blob/async/examples/background_task.py
            [ ] auto push message
            [ ] audio function sample & tutorial : https://github.com/Rapptz/discord.py/blob/async/examples/playlist.py, https://www.youtube.com/watch?v=X1DEos_9dJo
        The following are advanced api function:
            [ ]Add crawler (eg: taiwan stock, image , news, etc...)
                    Other function:
                    imgur upoloader/downloader
            [ ]anything else...
        '''
        await ctx.send(todo)


def setup(bot):
    bot.add_cog(System(bot))