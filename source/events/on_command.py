from discord.ext import commands
from utility import log


class OnCommandCog(commands.Cog, name="on command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.context):
        await ctx.message.delete()
        log("command", f"{ctx.command.name}")
