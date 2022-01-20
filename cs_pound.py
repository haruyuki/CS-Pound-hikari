import hikari
import tanjun
import os
import uvloop
from pathlib import Path
import logging

logger = logging.getLogger("cspound.main")

uvloop.install()


class Bot(hikari.GatewayBot):
    def __init__(self) -> None:
        super().__init__(
            token=os.environ.get("DISCORD"), logs="INFO", intents=hikari.Intents.ALL
        )

    def create_client(self) -> None:
        self.client = tanjun.Client.from_gateway_bot(
            self, declare_global_commands=409642350600781824
        )
        self.client.load_modules(*Path("./commands").glob("*.py"))
        self.client.add_prefix(",")

    def run(self: hikari.GatewayBot) -> None:
        self.create_client()

        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)
        self.event_manager.subscribe(hikari.StoppingEvent, self.on_stopping)

        super().run()

    async def on_starting(self, event: hikari.StartingEvent) -> None:
        logger.info("Bot is starting...")

    async def on_started(self, event: hikari.StartedEvent) -> None:
        await self.update_presence(
            activity=hikari.Activity(type=hikari.ActivityType.PLAYING, name="狗狗")
        )
        logger.info("Bot is loaded!")

    async def on_stopping(self, event: hikari.StoppingEvent) -> None:
        await self.client.close()
        logger.info("Bot has been shut down.")


bot = Bot()
bot.run()
