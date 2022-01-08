import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):

        embed = discord.Embed(color=0x415fe6, title=f'Der User {member.name} wurde gekickt.')
        
        if reason == None:
            await member.kick(reason='Ein Administrator hatte sich entschieden, dich zu kicken.')
            await ctx.send(embed=embed)
            return
            
        await member.kick(reason=reason)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Kick(client))