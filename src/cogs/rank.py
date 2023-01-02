from nextcord.ext import commands
import nextcord
from data import get_xp
class Rank(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "rank", description = "voir le rank de quelqu'un ou de toi")
  async def rank_slash(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(name="membre", description="Le membre que tu veux voir le rank", required=False), ephemeral: bool = nextcord.SlashOption(name="ephemeral", description="Est ce que tout le monde doit voir la reponse?", required=False)):
    if member is None:
      member = interaction.user
    xp, level, max = get_xp(member.id)
    await interaction.response.send_message(embed=nextcord.Embed(title=f'Rank de {member.name}', description=f"**Niveau**\n{level}\n\n**Xp**\n\n{xp}/{max}", color=0x2ecc71), ephemeral=ephemeral is True)

def setup(bot):
  bot.add_cog(Rank(bot))
