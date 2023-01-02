from nextcord.ext import commands
from data import get_xp, save
from random import randint
class Level(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def add(self, message):
    if message.author.bot: return
    xp, level, max = get_xp(message.author.id)
    xp += randint(3, 15)
    if xp > max:
      await self.bot.get_channel(1009428753434288143).send(f'Bravo {message.author.name}, tu es maintenant niveau {level + 1}')
    save(xp, message.author.id)

def setup(bot):
  bot.add_cog(Level(bot))
