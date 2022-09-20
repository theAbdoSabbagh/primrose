import logging
import os
import shutil
from time import strftime, localtime

import constant


def print_logo():
    for line in constant.logo.splitlines():
        print(line.center(shutil.get_terminal_size().columns))


def title(text):
    if os.name == "nt":
        os.system(f"title {text}")
    elif os.name == "posix":
        print(f"\33]0;{text}\a", end="", flush=True)


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


logs_buffer = []


def log(log_type: str, message: str):
    if logs_buffer.__len__() > constant.max_buffer:
        logs_buffer.clear()
    for line in message.split('\n'):
        logs_buffer.append(f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}")
