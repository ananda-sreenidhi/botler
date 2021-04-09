import discord
from discord.ext import commands
from cogs.modules.wikipedia import codesworth_wikipedia


class Wikipedia(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Wikipedia is Online!')

    @commands.command()
    async def wikipedia(self, ctx, *,  arg):
        response = codesworth_wikipedia(' '.join(arg.split()))
        if response[0] == 0:
            (a, b, c, d) = response[1:]
            embed = discord.Embed(title="Wikipedia article for \"{}\"".format(' '.join(arg.split())),
                                  url=c, color=0xffbf00)
            embed.add_field(name="{}".format(a), value=b, inline=False)
            embed.set_image(url=d)
            embed.set_footer(text="Click the title to read more.")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Wikipedia(client))


