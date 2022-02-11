import discord
from discord.ext import commands
from data.db import *
import random

class Work(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def work(self, ctx):
        income = random.randint(10, 500)
        embed = discord.Embed(color=0x415FE6, title='<a:bewegendeszeichenlmao:929793908723052624> Gute Arbeit!', description=f'Du hast für **{int(income):,}**🐚 gearbeitet!')
        await update_wallet(ctx.author.id, income)
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Work(client))