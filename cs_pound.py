import os

from bot import build_bot

# noqa | Code taken and modified from https://patchwork.systems/programming/hikari-discord-bot/introduction-and-basic-bot.html#tanjun-and-the-client
if os.name != "nt":
    import uvloop

    uvloop.install()

if __name__ == "__main__":
    build_bot().run()
