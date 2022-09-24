import threading

from imported_cogs import *
from discord import *

from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from textual.app import App
from textual.widget import Widget
from textual.widgets import Header, Footer

from utility import get_prefix, token_info, file_check, check_token
from utility.printing import log, logs_buffer, title, print_logo
from secrets import compare_digest

import time

import constant

print_logo()


def wizard():
    with open("config.json", "r") as f:
        config = json.load(f)
        token = config["token"]
        if not compare_digest(token, ""):
            login_thread()
            return
    print("Please enter your token below.")
    token = input("> ")
    print("Checking token...")
    if check_token(token):
        with open("config.json", "w") as f:
            json.dump({"token": token, "prefix": "."}, f, indent=4)
        print("Token saved!")
        login_thread()
    else:
        print("Invalid token!")
        wizard()


def bot_login():
    with open("config.json", "r") as f:
        config = json.load(f)
        token = config["token"]
    r = token_info(token)
    log("event", f"Logging into {r['username']}#{r['discriminator']}...")
    bot.run(token)


bot = commands.Bot(
    command_prefix=get_prefix(),
    self_bot=True,
    help_command=None,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    strip_after_prefix = True,
    status = discord.Status.dnd
)

bot.add_cog(HelpCog(bot))
bot.add_cog(PrivacyCog(bot))
bot.add_cog(PrefixCog(bot))
bot.add_cog(ProfileCog(bot))
bot.add_cog(CodeblockCog(bot))
bot.add_cog(BackupCog(bot))
bot.add_cog(FirstMessageCog(bot))
bot.add_cog(ClapCog(bot))

bot.add_cog(OnReadyCog(bot))
bot.add_cog(OnCommandCog(bot))
bot.add_cog(OnCommandErrorCog(bot))

# I think commands dont need their own cog, this can be improved


def login_thread():
    debugger_thread = threading.Thread(target=bot_login)
    debugger_thread.daemon = True
    debugger_thread.start()


class Ascii(Widget):
    def render(self) -> Panel:
        text = Text(constant.ascii_logo)
        text.stylize("red", 0, 98)
        text.stylize("green", 98, 300)
        return Panel(Align.center(text, style="white", vertical="middle"), title="V0.0.1")


class Logo(Widget):
    def render(self) -> Panel:
        text = Text(constant.logo)
        text.highlight_words(["═", "║", "╔", "╗", "╚", "╝"], "red")
        return Panel(Align.center(text, style="white", vertical="middle"))


class Logs(Widget):
    def render(self) -> Panel:
        while True:
            self.refresh()
            time.sleep(0.25)
            return Panel(Align.left("\n".join(logs_buffer), style="white"))


class MyApp(App):
    async def on_load(self) -> None:
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        await self.view.dock(Header(tall=False, style="white"), edge="top")
        await self.view.dock(Footer(), edge="bottom")

        await self.view.dock(Ascii(), edge="left", size=28)
        await self.view.dock(Logo(), Logs(), edge="top")


def main():
    title("Primrose")
    file_check()
    wizard()
    MyApp.run(title="Primrose Selfbot", log="primrose.log")
