import discord
from discord.ext import commands
from .modules.sarcdet import predict

class Sarcasm(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('SarcasmDetection is online!')

    @commands.command()
    async def detect(self, ctx, *, arg=""):
        if arg == "":
            Channel = ctx.message.channel
            msg = await Channel.history(limit=2).flatten()
            x = predict(msg[1].content)
        else: 
            x = predict(arg)
        embed = discord.Embed(title = f"{x}", color=0xffbf00)
        await ctx.send(embed=embed)
 
def setup(client):
    client.add_cog(Sarcasm(client))
    
