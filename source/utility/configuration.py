import json
import os


def get_prefix():
    if not os.path.exists("config.json"):
        return "."
    with open("config.json", "r") as f:
        config = json.load(f)
        return config["prefix"]


def get_token():
    if not os.path.exists("config.json"):
        return ""
    with open("config.json", "r") as f:
        config = json.load(f)
        return config["token"]
