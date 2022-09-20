from discord.ext import commands
from utility import log, get_prefix, print_logo, clear


class PrefixCog(commands.Cog, name="prefix"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="prefix",
        usage="<prefix>",
        description="Change the prefix"
    )
    async def prefix(self, ctx: commands.context, prefix: str):
        if len(prefix) > 1:
            await ctx.send("Prefix must be one character")
            return
        self.bot.command_prefix = prefix
        await ctx.send(f"Prefix changed to {prefix}")
        clear()
        print_logo()
        print(f"User: {self.bot.user}\nPrefix: {get_prefix()}\n")
        log("info", f"Prefix changed to {prefix}")
