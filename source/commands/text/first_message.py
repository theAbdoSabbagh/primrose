from discord.ext import commands
import discord
from utility import message_builder


class FirstMessageCog(commands.Cog, name="first message commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="fmessage",
        usage="",
        description="Link to first message"
    )
    async def fmessage(self, ctx: commands.context, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
        await message_builder(ctx, message.jump_url)
