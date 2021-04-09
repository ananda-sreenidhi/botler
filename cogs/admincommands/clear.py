import discord
from discord.ext import commands


class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Clear is Online!')

    @commands.command()
    async def clear(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"```Messages Deleted from Channel```", delete_after=1)


def setup(client):
    client.add_cog(Clear(client))


