import discord
from discord.ext import commands
import random

class Gay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gay(self, ctx, *, user):
        rate = random.randint(0, 100)

        embed = discord.Embed(color=0x415fe6, title=f'🏳️‍🌈 Wie schwul ist {user}?', description=f'**{user}** ist zu {rate}% schwul.')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Gay(client))