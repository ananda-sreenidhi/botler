import discord
from discord.ext import commands


class Tell(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Tell is Online!')

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content

    @commands.command()
    async def tell(self, ctx, *, arg=""):
        try:
            members = ctx.guild.members
            for member in members:
                if int(arg.split()[0].lower()[3:-1]) == member.id:
                    user = ctx.guild.get_member(member.id)
                    msg = str(ctx.message.author.name) + " said: " + " ".join(arg.split()[1:])
                    await user.send(msg)
            response = "Sent"
        except:
            response = "Error"
        await ctx.send(response)


def setup(client):
    client.add_cog(Tell(client))


