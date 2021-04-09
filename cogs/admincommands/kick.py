import discord
from discord.ext import commands


class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Kick is Online!')

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'Kicked {member.mention}')
        await member.kick(reason=reason)


def setup(client):
    client.add_cog(Kick(client))


