import discord
from discord.ext import commands


class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mute is Online!')

    @commands.command()
    async def mute(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted")

        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
            await member.edit(roles=[role])
            await ctx.send(f"{member.name} was muted.")
            for channel in guild.channels:
                await channel.set_permissions(role, send_messages=False, speak=False)
        else:
            await member.add_roles(role)
            for channel in guild.channels:
                await channel.set_permissions(role, send_messages=False, speak=False)
            await ctx.send(f"{member.mention} was muted.")


def setup(client):
    client.add_cog(Mute(client))


