import logging
import os
from pathlib import Path

from discord.ext import bridge, commands

from latentbot.bot_utils import load_discord_token
from latentbot.cog_utils import load_cogs

LOG = logging.getLogger(__name__)

TOKEN = load_discord_token()

bot = bridge.Bot(
    command_prefix=commands.when_mentioned_or("%"),
)

print("starting bot")


@bot.command("frig")
async def frig(ctx):
    ctx.send("frig")


@bot.event
async def on_ready():
    print(f"{bot.user} is online")


if __name__ == "__main__":
    load_cogs(bot, Path(os.path.dirname(__file__)))
    bot.run(TOKEN, reconnect=True)
