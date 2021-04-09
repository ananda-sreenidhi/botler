import discord
from discord.ext import commands
from cogs.modules.weather import codesworth_weather


class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Weather is Online!')

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content

    @commands.command()
    async def weather(self, ctx, arg=""):
        (a, x, y, z, w) = codesworth_weather(arg)
        embed = discord.Embed(title="Weather information for {}".format(a), color=0xffbf00)
        embed.add_field(name="Temperature", value=str(x) + "°C", inline=True)
        embed.add_field(name="Pressure", value=str(y) + " hPa", inline=True)
        embed.add_field(name="Humidity", value=str(z) + "%", inline=True)
        embed.add_field(name="Description", value=str(w).capitalize(), inline=True)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Weather(client))


