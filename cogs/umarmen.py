import discord
from discord.ext import commands

class Hug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        await ctx.send(f'{ctx.author.mention} hat {member.mention} ganz doll lieb <a:umarmen:942767282508156968>')


def setup(client):
    client.add_cog(Hug(client))