import discord
from discord.commands.core import SlashCommand
from discord.ext import bridge, commands


class Spoil(commands.Cog):
    """Spoil every word in a sentence"""

    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @SlashCommand
    async def spoil(
        self,
        ctx: bridge.BridgeApplicationContext,
        message: discord.Option(
            discord.SlashCommandOptionType.string,
            description="Message to spoil",
            required=True,
        ),  # type: ignore
    ):
        await ctx.respond(spoil(message))


def spoil(s: str) -> str:
    """Surround each space-separated word with double pipes for spoilers"""

    return " ".join(f"||{x}||" for x in s.split(" "))
