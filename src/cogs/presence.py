import discord
from discord.ext import commands
class presencia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity = discord.Game(name='$ayuda | TelBot by Raztor'))
async def setup(bot):
    await bot.add_cog(presencia(bot))