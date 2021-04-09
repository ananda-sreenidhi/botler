import discord
from discord.ext import commands
from cogs.modules.currency import codesworth_currency


class Currency(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Currency is Online!')

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content

    @commands.command()
    async def currency(self, ctx, amt, fr, to):
        response = codesworth_currency(amt, fr, to)
        await ctx.send(response)


def setup(client):
    client.add_cog(Currency(client))


