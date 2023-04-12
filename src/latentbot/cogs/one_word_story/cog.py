import logging
import sqlite3
from pathlib import Path

import discord
from discord.channel import TextChannel
from discord.commands.core import SlashCommandGroup
from discord.ext import bridge, commands

from latentbot.cogs.one_word_story import db
from latentbot.common import USER_DATA_DIR
from latentbot.db_utils import init_db
from latentbot.log_config import configure_logger

LOG = logging.getLogger(__name__)
configure_logger(__name__, log_level=logging.DEBUG)


class OneWordStory(commands.Cog):
    """Commands for one word story"""

    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.db_path = USER_DATA_DIR / db.DB_NAME
        self.schema_path = Path(__file__).with_name(db.SCHEMA_NAME)

        init_db(USER_DATA_DIR / db.DB_NAME, self.schema_path)

    ows = SlashCommandGroup("ows")

    @ows.command()
    async def createstory(
        self, ctx: bridge.BridgeApplicationContext, length: discord.Option(int)  # type: ignore
    ):
        """Create a story"""
        await ctx.respond("Command under construction", ephemeral=True)

    @ows.command()
    @discord.default_permissions(manage_channels=True)
    async def setchannel(
        self, ctx: bridge.BridgeApplicationContext, channel: discord.Option(discord.SlashCommandOptionType.channel)  # type: ignore
    ):
        """Set the channel that stories will be generated from"""
        channel: TextChannel
        guild_id = ctx.guild_id

        if guild_id is None:
            await ctx.respond(
                "Error: can only use this command in a Guild", ephemeral=True
            )
            return

        with self.__get_conn() as conn:
            db.set_channel(conn, channel.id, guild_id)

        await ctx.respond(
            f"Set {channel.mention} as the one word story channel", ephemeral=True
        )

    def __get_conn(self) -> sqlite3.Connection:
        """Get a connection to the one word story database"""
        return sqlite3.connect(self.db_path)
