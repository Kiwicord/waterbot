import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):

        embed = discord.Embed(color=0x415fe6, title=f'Der User {member.name} wurde gebannt.')
        
        if reason == None:
            await member.ban(reason='Ein Administrator hatte sich entschieden, dich zu bannen.')
            await ctx.send(embed=embed)
            return
            
        await member.ban(reason=reason)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ban(client))