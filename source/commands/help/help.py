from discord.ext import commands
from utility import message_builder, get_prefix


class HelpCog(commands.Cog, name="help commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="help",
        usage="[command]",
        description="Help menu"
    )
    async def help(self, ctx: commands.context, command: str = None):
        if command is None:
            main_text = f"{len(self.bot.commands)} Total Commands\n<> = Needed | [] = Optional\n"
            for category in self.bot.cogs:
                if category.startswith("on"):
                    continue
                commands_list = [
                    (command.name, command.usage, command.description)
                    for command in self.bot.get_cog(category).get_commands()
                ]
                main_text += f"\n{category}:\n"
                main_text += "".join(
                    [f"{get_prefix()}{command[0]} {command[1]} - {command[2]}\n" for command in commands_list]
                )
            await message_builder(ctx, main_text)
        else:
            command = self.bot.get_command(command)
            await message_builder(ctx, f"Name: {command.name}\nUsage: {command.usage}\nDescription: {command.description}")
