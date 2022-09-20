import requests
import constant


def header(token=None):
    return {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': token} if token else {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json'
    }


def check_token(token):
    r = requests.get(
        f"https://discord.com/api/{constant.api_version}/users/@me/library", headers=header(token)
    )
    return r.status_code == 200


def token_info(token):
    r = requests.get(
        f"https://discord.com/api/{constant.api_version}/users/@me", headers=header(token)
    )
    return r.json()
