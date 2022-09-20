import os

from logging.handlers import BufferingHandler
from time import strftime, localtime

from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from textual.app import App
from textual.widget import Widget
from textual.widgets import Header, Footer

import logging
import threading
import time

import constant

logging.basicConfig(filename="primrose.log", filemode="w", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
main_logger = logging.getLogger()
main_logger.setLevel(logging.DEBUG)

buffering_handler = BufferingHandler(capacity=constant.max_buffer)
main_logger.addHandler(buffering_handler)

logger = logging.getLogger("primrose")
buffering_handler.buffer.clear()


def log(log_type: str, message: str):
    for line in message.split('\n'):
        match log_type:
            case "info":
                logger.info(f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}")
            case "warning":
                logger.warning(f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}")
            case "error":
                logger.error(f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}")
            case "critical":
                logger.critical(f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}")
            case "debug":
                logger.debug(f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}")
            case _:
                logger.info(f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}")


def title(text):
    if os.name == "nt":
        os.system(f"title {text}")
    elif os.name == "posix":
        print(f"\33]0;{text}\a", end="", flush=True)


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
            log_messages = [logged.msg for logged in buffering_handler.buffer]
            time.sleep(0.25)
            return Panel(Align.left("\n".join(log_messages), style="white"))


def create_log_messages():
    for amount, _ in enumerate(range(30), start=1):
        time.sleep(1)
        log("info", f"logged {amount}")


threading.Thread(target=create_log_messages).start()


class MyApp(App):
    async def on_load(self) -> None:
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        await self.view.dock(Header(icon="🌹", tall=False, style="white"), edge="top")
        await self.view.dock(Footer(), edge="bottom")

        await self.view.dock(Ascii(), edge="left", size=28)
        await self.view.dock(Logo(), Logs(), edge="top")


def main():
    title("Primrose")
    MyApp.run(title="Primrose Selfbot", log="primrose.log")
