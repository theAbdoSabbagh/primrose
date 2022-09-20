import json

import requests
from discord.ext import commands

import constant
from utility import log, get_prefix, header, get_token


class ProfileCog(commands.Cog, name="profile commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="status",
        usage="<text>",
        description="Change custom status"
    )
    async def status(self, ctx: commands.context, *, text: str):
        requests.patch(
            f"https://discord.com/api/{constant.api_version}/users/@me/settings",
            headers=header(get_token()),
            json={"custom_status": {"text": text}}
        )
        await ctx.send(f"Status changed to {text}")
        log("info", f"Status changed to {text}")

    @commands.command(
        name="cstatus",
        usage="",
        description="Clear custom status"
    )
    async def cstatus(self, ctx: commands.context):
        requests.patch(
            f"https://discord.com/api/{constant.api_version}/users/@me/settings",
            headers=header(get_token()),
            json={"custom_status": {"text": ""}}
        )
        await ctx.send("Cleared status")
        log("info", "Cleared status")

    @commands.command(
        name="about",
        usage="<text>",
        description="Change about me"
    )
    async def about(self, ctx: commands.context, *, text: str):
        requests.patch(
            f"https://discord.com/api/{constant.api_version}/users/@me/settings",
            headers=header(get_token()),
            json={"bio": {"text": text}}
        )
        await ctx.send(f"About me changed to {text}")
        log("info", f"About me changed to {text}")

    @commands.command(
        name="cabout",
        usage="",
        description="Clear about me"
    )
    async def cabout(self, ctx: commands.context):
        requests.patch(
            f"https://discord.com/api/{constant.api_version}/users/@me/settings",
            headers=header(get_token()),
            json={"bio": {"text": ""}}
        )
        await ctx.send("Cleared about me")
        log("info", "Cleared about me")
