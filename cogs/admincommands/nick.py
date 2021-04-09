import discord
from discord.ext import commands


class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Kick is Online!')

    @commands.command()
    async def nick(self, ctx, member: discord.Member, *, new_name):
        await member.edit(nick=new_name)
        await ctx.send(f"{member.mention}'s nickname has been modified")


def setup(client):
    client.add_cog(Kick(client))