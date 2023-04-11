import logging
import os
from pathlib import Path

from discord.ext import bridge

from latentbot.bot_utils import load_discord_token
from latentbot.log_config import configure_logger

LOG = logging.getLogger(__name__)

TOKEN = load_discord_token()

bot = bridge.Bot()

LOG_LEVEL = os.getenv("LOG_LEVEL")
if not LOG_LEVEL:
    LOG_LEVEL = "DEBUG"

LOG_LEVEL_INT = getattr(logging, LOG_LEVEL.upper())


@bot.event
async def on_ready():
    LOG.info(f"{bot.user} is online")


def load_extensions():
    cogs_path = Path(os.path.dirname(__file__)) / "cogs"

    for cog_dir in cogs_path.iterdir():
        if cog_dir.is_dir():
            init_file = cog_dir / "__init__.py"
            if init_file.exists():
                cog_name = f"latentbot.cogs.{cog_dir.name}"
                LOG.info(f"Loading cog '{cog_name}'")
                bot.load_extension(cog_name)


if __name__ == "__main__":
    configure_logger(__name__, log_level=logging.DEBUG)

    load_extensions()
    bot.run(TOKEN, reconnect=True)
