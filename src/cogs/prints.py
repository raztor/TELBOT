from discord.ext import commands
from src.config import bot_config as b_config
class Prints(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(member):
        print(f'{member} Se Unio al Servidor')

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f'{member}Salió del servidor')


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != self.bot.user.id:
            print(f"{message.guild}/{message.channel}/{message.author.name}>{message.content}")
            if message.embeds:
                print(message.embeds[0].to_dict())

    @commands.Cog.listener()
    async def on_ready(self):
        if b_config.DEBUGGING == 1:
            print('Modo Debug')
            print('Usuario:', self.bot.user)
            print('ID:', self.bot.user.id)
            print('bot listo')
        if b_config.DEBUGGING == 0:
            print('Modo Produccion')
            print('Usuario:', self.bot.user)
            print('ID:', self.bot.user.id)
            print('bot listo')


async def setup(bot):
    await bot.add_cog(Prints(bot))