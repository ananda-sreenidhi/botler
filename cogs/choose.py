import discord
from discord.ext import commands
from random import choice


class Choose(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Choose is Online!')

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content

    @commands.command()
    async def choose(self, ctx, *, arg=""):

        try:
            response = choice(arg.split())
        except:
            response("Error")
        await ctx.send(response)


def setup(client):
    client.add_cog(Choose(client))


