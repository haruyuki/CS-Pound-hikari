import hikari
import tanjun
import os
from pathlib import Path
import logging

from constants import Tokens

logger = logging.getLogger("cspound.main")


# noqa | Code taken and modified from https://patchwork.systems/programming/hikari-discord-bot/introduction-and-basic-bot.html#tanjun-and-the-client
def build_bot() -> hikari.GatewayBot:
    discord_token = Tokens.discord_token
    bot = hikari.GatewayBot(discord_token)

    make_client(bot)

    return bot


def make_client(bot: hikari.GatewayBot) -> tanjun.Client:
    client = (
        tanjun.Client.from_gateway_bot(
            bot, mention_prefix=True, declare_global_commands=409642350600781824
        )
    ).add_prefix(",")

    client.load_modules(*Path("./commands").glob("*.py"))

    return client
