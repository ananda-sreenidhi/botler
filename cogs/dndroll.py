import discord
from discord.ext import commands
from random import randint


class Roll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Roll is Online!')

    @commands.command()
    # Add the modifier thing eventually when time :D
    async def roll(self, ctx, *, arg=""):
        details = arg.lower().split('d')
        embed = discord.Embed(title=f"{details[0]}d{details[1]} Roll Summary", color=0xffbf00)
        try:
            if int(details[0])>20: details[0] = 20
            l = [randint(1, int(details[1])) for i in range(int(details[0]))]
            embed.add_field(name=f"Sum", value = sum(l), inline=False)
            for i in range(len(l)):
                embed.add_field(name=f"Roll#{i+1}", value = l[i], inline=True)
            
        except:
            embed.add_field(name=f"An error occurred, please try again!", value = " ", inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Roll(client))


