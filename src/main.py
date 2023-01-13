from discord.ext import commands
import os
from config import bot_config as b_config
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

class DiscordClient(commands.Bot):

    def __init__(self,):
        commands.Bot.__init__(
            self,
            command_prefix='$',
            intents=discord.Intents.default())
        intents.members = True
        intents.presences = True
        intents.messages = True


    async def setup_hook(self):
            for f in os.listdir("./cogs"):
                if f.endswith(".py"):
                    await self.load_extension("cogs." + f[:-3])


bot = DiscordClient()
bot.run(b_config.token)