from .cog import OneWordStory


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(OneWordStory(bot))  # add the cog to the bot
