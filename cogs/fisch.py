import discord
from discord.ext import commands
from fische import Fische
import random


class Fisch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fisch(self, ctx):
        fisch_url = random.choice(Fische.FISCHE)
        embed = discord.Embed(color=0x415fe6, title='Blubb... 🐟✨')
        embed.set_image(url=fisch_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fisch(client))