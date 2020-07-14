import discord
from discord.ext import commands
import json


class cog_base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('setting.json', 'r', encoding='utf8') as jf:
            self.JSON_SETTING = json.load(jf)