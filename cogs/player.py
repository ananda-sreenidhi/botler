import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import urllib.request
import re


class Player(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Player is Online!')

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            embed = discord.Embed(title = f"Join a Voice Channel First!", color=0xffbf00)
            await ctx.send(embed=embed)

        channel = ctx.message.author.voice.channel
        if ctx.voice_client is None:
            vc = await channel.connect()
        else:
            await ctx.voice_client.move_to(channel)
            vc = ctx.voice_client
        embed = discord.Embed(title = f"Joined user Channel", color=0xffbf00)
        await ctx.send(embed=embed)

    @commands.command()
    async def leave(self, ctx):
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
        embed = discord.Embed(title = f"Left Voice Channel", color=0xffbf00)
        await ctx.send(embed=embed)

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            embed = discord.Embed(title = f"Paused", color=0xffbf00)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title = f"Currently no audio is playing", color=0xffbf00)
            await ctx.send(embed=embed)

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            embed = discord.Embed(title = f"Resumed", color=0xffbf00)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title = f"The audio is not paused.", color=0xffbf00)
            await ctx.send(embed=embed)

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()
        embed = discord.Embed(title = f"Stopped", color=0xffbf00)
        await ctx.send(embed=embed)

    @commands.command()
    async def play(self, ctx, *, name: str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            embed = discord.Embed(title = f"Wait for the current playing music to end or use the 'stop' command.", color=0xffbf00)
            await ctx.send(embed=embed)
            return

        if ctx.author.voice is None or ctx.author.voice.channel is None:
            embed = discord.Embed(title = f"Join a Voice Channel First!", color=0xffbf00)
            await ctx.send(embed=embed)

        channel = ctx.message.author.voice.channel
        if ctx.voice_client is None:
            vc = await channel.connect()
        else:
            await ctx.voice_client.move_to(channel)
            vc = ctx.voice_client

        voice = get(self.client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        if name.split()[0].startswith("http"):
            url = name
        else:
            #working on improving the search function.
            query = "+".join(name.split())
            html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = "https://www.youtube.com/watch?v=" + video_ids[0]

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                embed = discord.Embed(title = f"Playing {os.path.splitext(file)[0][:-12]}", color=0xffbf00)
                await ctx.send(embed=embed)
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))

def setup(client):
    client.add_cog(Player(client))
