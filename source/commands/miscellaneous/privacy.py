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
        privacy_toggle = not privacy_toggle
        # this does nothing atm, i think config.json should have a new key for privacy and instead of changing the global var
        # the key would be changed when running the command between true and false
        # i think the TUI should then change the logs area and hide the username and tag if privacy was enabled
        # else it should reveal them
