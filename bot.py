import discord
from discord.ext import commands
import os

token = open("tokens.txt", "r").readlines()[0]

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('./cogs/admincommands'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.admincommands.{filename[:-3]}')

client.run(token)