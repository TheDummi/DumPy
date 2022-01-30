import discord
from discord.ext import commands


class Moderation(commands.Cog):
    """optional description to show on the help command. Remove this line for no description."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def foo(self, ctx):
        await ctx.send("Foo!")


def setup(bot):
    bot.add_cog(Moderation(bot))
