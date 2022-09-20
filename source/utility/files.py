import json
import os


def file_check():
    if not os.path.exists("config.json"):
        with open("config.json", "w") as f:
            json.dump({"token": "", "prefix": "."}, f, indent=4)
