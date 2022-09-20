from discord.ext import commands
from utility import log


class OnCommandErrorCog(commands.Cog, name="on command error"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.context, error: commands.errors):
        log("error", f"{error}")
        await ctx.send(f"Error: {error}")
