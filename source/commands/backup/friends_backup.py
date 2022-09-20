from discord.ext import commands
import os
from utility import message_builder


class BackupCog(commands.Cog, name="backup commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="fbackup",
        usage="",
        description="Backup friends"
    )
    async def fbackup(self, ctx: commands.context):
        os.mkdir("backup")
        friends_amount = 0
        blocked_amount = 0
        for friend in self.bot.user.friends:
            with open("backup/friends.txt", "a") as friends:
                friends.write(f"{friend.name}#{friend.discriminator}\n")
                friends_amount += 1
        for block in self.bot.user.blocked:
            with open("backup/blocked.txt", "a") as blocked:
                blocked.write(f"{block.name}#{block.discriminator}\n")
                blocked_amount += 1
        await message_builder(ctx, f"Backed up {friends_amount} friends and {blocked_amount} blocked users")
