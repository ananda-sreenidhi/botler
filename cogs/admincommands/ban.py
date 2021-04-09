import discord
from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ban is Online!')

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'Banned {member.mention}')
        await member.ban(reason=reason)



def setup(client):
    client.add_cog(Ban(client))


