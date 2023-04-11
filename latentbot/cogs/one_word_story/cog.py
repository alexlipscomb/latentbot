import discord
from discord.commands.core import SlashCommandGroup
from discord.ext import bridge, commands


class OneWordStory(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    ows = SlashCommandGroup("ows")

    @ows.command()
    async def createstory(self, ctx: bridge.BridgeApplicationContext, length: discord.Option(int)):  # type: ignore
        """Create a story"""
        await ctx.respond("Command under construction", ephemeral=True)

    @ows.command()
    @discord.default_permissions(manage_channels=True)
    async def setchannel(
        self, ctx: bridge.BridgeApplicationContext, channel: discord.Option(discord.SlashCommandOptionType.channel)  # type: ignore
    ):
        """Set the channel that stories will be generated from"""
        await ctx.respond("Command under construction", ephemeral=True)
