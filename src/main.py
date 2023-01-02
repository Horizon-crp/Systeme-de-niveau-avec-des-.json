from nextcord.ext import commands
from nextcord import Intents
from os import listdir, system, environ

bot = commands.Bot(command_prefix=['?'], intents=Intents.all(), help_command=None)
for fn in listdir('cogs'):
  if fn.endswith(".py"):
    tasks.append(asyncio.create_task(bot.add(f'cogs.{fn[:-3]}')))
bot.run(environ['token'])
