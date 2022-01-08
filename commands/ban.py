import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason='Kein Grund angegeben.'):

        embed = discord.Embed(color=0x415fe6, title=f'<a:bewegendeszeichenlmao:920059343108452353> Ban!', description=f'Der User **{member}** wurde gebannt.')
        
        reason_none_embed = discord.Embed(color=0x415fe6, title=f'<a:bewegendeszeichenlmao:920059343108452353> Gebannt!', description=f'Du wurdest von Waterworld gebannt.\n<:waterworld_pfeil:920318666535469056> **{reason}**')
        await member.send(embed=reason_none_embed)
        await member.ban(reason=reason)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ban(client))