from nextcord.ext import commands
from nextcord import Intents
from os import listdir, system, environ
import asyncio

class bbot:
  def __init__(self, bot):
    self.bot = bot

  async def add(self, file):
    self.bot.load_extension(file)

  def run(self, token):
    self.bot.run(token)

async def main():
  bot = bbot(commands.Bot(command_prefix=['?'], intents=Intents.all(), help_command=None))
  tasks = []
  for fn in listdir('cogs'):
    if fn.endswith(".py"):
      tasks.append(asyncio.create_task(bot.add(f'cogs.{fn[:-3]}')))
  for i in tasks:
    await i
  bot.run(environ['token'])

asyncio.run(main())
