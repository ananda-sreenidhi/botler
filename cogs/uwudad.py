import discord
from discord.ext import commands
from random import randint, choice


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is Online!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
      
    @commands.Cog.listener()
    async def on_message(self, message):
        # uwu! 
        listuwu = ["uwu", "owo", "hewwo"]
        if not message.author.bot:
            if message.content.lower() in listuwu:
                await message.channel.send(f"{choice(listuwu)}!")

        # dadbot
        # this isn't the most effective way to do it but i can't be arsed to write it properly as it is 2 am and i am terribly the fuck stressed
        listset = set(["I'm", "i'm", "im", "Im"])
        if not message.author.bot:
            msg = message.content.split()
            if len(listset.intersection(set(msg))):
                if randint(1, 22) <= 7:
                    # works with a probability of 1/pi because why the heck not, chaos time
                    index = msg.index(list(listset.intersection(set(msg)))[0]) + 1
                    im = " ".join(msg[index:])
                    await message.channel.send(f"Hi {im} I'm Dad!")


def setup(client):
    client.add_cog(Example(client))