import discord
from discord.ext import commands
import asyncio
import youtube_dl
import pafy

class MusicPlayer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.song_queue = {}

        self.setup()
    
    def setup(self):
        for guild in self.client.guilds:
            self.song_queue[guild.id] = []
        
    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            ctx.voice_client.stop()
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)
        
    async def search_song(self, amount, song, get_url=False):
        info = await self.client.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({
            'format': 'bestaudio',
            'quiet': True}
        ).extract_info(f'ytsearch{amount}:{song}', download=False, ie_key='YoutubeSearch'))
        if len(info['entries']) == 0: return None

        return [entry['webpage_url'] for entry in info['entries']] if get_url else info
    
    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.client.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.volume = 0.5

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            embed1 = discord.Embed(color=0x415fe6, description='<a:bewegendeszeichenlmao:920059343108452353> Du bist nicht in einem VC!')
            return await ctx.send(embed=embed1)
        
        await ctx.author.voice.channel.connect()
    
    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.disconnect()

        embed = discord.Embed(color=0x415fe6, description='<a:bewegendeszeichenlmao:920059343108452353> Ich bin nicht in einem VC!')
        await ctx.send(embed=embed)

    @commands.command()
    async def play(self, ctx, *, song=None):
        if song is None:
            embed = discord.Embed(color=0x415fe6, description='<a:bewegendeszeichenlmao:920059343108452353> Bitte gebe den Namen deines Songs an!')
            return await ctx.send(embed=embed)
        
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()

        # wenn song kein link ist
        if not 'youtube.com/watch?' in song or 'https://youtu.be/' in song:
            embed1 = discord.Embed(color=0x415fe6, description='<a:laden:858410012690350141> Suche den Song...')
            await ctx.send(embed=embed1)

            result = await self.search_song(1, song, get_url=True)
        
            if result is None:
                embed2 = discord.Embed(color=0x415fe6, description='<a:bewegendeszeichenlmao:920059343108452353> Konnte den Song nicht finden!')
                return await ctx.send(embed=embed2)
            
            song = result[0]

        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()
            await self.play_song(ctx, song) # song starten
        
        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue[ctx.guild.id])

            if queue_len < 10:
                self.song_queue[ctx.guild.id].append(song)
                embed3 = discord.Embed(color=0x415fe6, description=f'<a:bewegendeszeichenlmao:920059343108452353> `{song}` wurde zur Warteschlange hinzugefügt!')
                return await ctx.send(embed=embed3)
            else:
                embed4 = discord.Embed(color=0x415fe6, description='<a:bewegendeszeichenlmao:920059343108452353> Ich kann nur maximal 10 Songs in der Warteschlange haben!')
                return await ctx.send(embed=embed4)

        await self.play_song(ctx, song)# song starten

        embed5 = discord.Embed(color=0x415fe6, description=f'<a:bewegendeszeichenlmao:920059343108452353> Jetzt spielt: `{song}`')


def setup(client):
    client.add_cog(MusicPlayer(client))        
