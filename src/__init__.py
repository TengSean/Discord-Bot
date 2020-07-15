import discord
from discord.ext import commands

import json, os

with open('setting.json', 'r', encoding='utf8') as jf:
    JSON_SETTING = json.load(jf)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")


MODULE_PATH = "./module"
for filename in os.listdir(MODULE_PATH):
    if filename.endswith('.py'):
        bot.load_extension(f'module.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(JSON_SETTING['TOKEN'])


