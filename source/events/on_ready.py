from discord.ext import commands
from utility import get_prefix, log


class OnReadyCog(commands.Cog, name="on ready"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log("info", f"Logged into {self.bot.user}\nPrefix: {get_prefix()}")
