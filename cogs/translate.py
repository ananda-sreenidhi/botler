import discord
from discord.ext import commands
from cogs.modules.translate import translate


class Translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Translator is Online!')

    @commands.command()
    async def translate(self, ctx, *, arg=""):
        if arg == "":
            Channel = ctx.message.channel
            msg = await Channel.history(limit=2).flatten()
            translated = translate(msg[1].content)
        else:
            translated = translate(arg)

        if len(translated[0])>1:
            # i am so fucking proud of this elegant solution to this problem without having to check if the returned type is a string or list
            # bow before me, bitch
            (txt, src, dest) = translated
            embed = discord.Embed(title=f"{txt}", color=0xffbf00)
            # embed.add_field(name="Translated from", value = src, inline=True)
            # embed.add_field(name="Translated to", value = dest, inline=True)
            # embed.add_field(name=f"{txt}", value = "abc, this is why i fucking told you not to mess", inline=False)
            embed.set_footer(text=f"Translated from {src} to {dest}")
        else:
            txt = translated
            embed = discord.Embed(title="Translation", color=0xffbf00)
            embed.add_field(name="Error!", value = translated, inline=False)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Translate(client))