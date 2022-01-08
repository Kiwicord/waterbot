import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason='Ein Team-Mitglied hatte sich entschieden, dich zu kicken.'):

        embed = discord.Embed(color=0x415fe6, title=f'<a:bewegendeszeichenlmao:920059343108452353> Kick!', description=f'Der User **{member}** wurde gekickt.')
        
        reason_none_embed = discord.Embed(color=0x415fe6, title=f'<a:bewegendeszeichenlmao:920059343108452353> Gekickt!', description=f'Du wurdest von Waterworld gekickt.\n<:waterworld_pfeil:920318666535469056> {reason}')
        await member.send(embed=reason_none_embed)
        await member.kick(reason=reason)
        await ctx.send(embed=embed)
            

def setup(client):
    client.add_cog(Kick(client))