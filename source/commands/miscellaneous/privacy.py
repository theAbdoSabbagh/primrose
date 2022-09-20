import shutil

from discord.ext import commands
from utility import message_builder, log, get_prefix

privacy_toggle = False


class PrivacyCog(commands.Cog, name="privacy commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="privacy",
        usage="",
        description="Hide username in console"
    )
    async def privacy(self, ctx: commands.context):
        global privacy_toggle
        log("info", f"Privacy {'enabled' if privacy_toggle else 'disabled'}")
        await message_builder(ctx, f"Privacy {'enabled' if privacy_toggle else 'disabled'}")
