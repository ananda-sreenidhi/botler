import discord
from discord.ext import commands
from cogs.modules.lenny import codesworth_lenny


class Lenny(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Lenny is Online!')

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content

    @commands.command()
    async def lenny(self, ctx, arg):
        response = codesworth_lenny(arg)
        await ctx.send(response)


def setup(client):
    client.add_cog(Lenny(client))


