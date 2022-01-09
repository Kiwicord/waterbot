import discord
from discord.ext import commands
import random
import asyncio

cooldown = 3600

class RainbowRoleListener(commands.Cog):
    def __init__(self, client):
        self.client = client
        print('rainbow role listener cog ready')

    @commands.command()
    async def change_rainbow_role_color(self, ctx):
        # rainbow rolle
        guild = self.client.get_guild(813039986545917965)

        rainbow_role_id = 850832485658787840
        rainbow_role = discord.utils.get(guild.roles, id=rainbow_role_id)

        await ctx.send(f'Rainbowrolle wird nun alle **{cooldown} Sekunden** geändert.')

        while True:
            await asyncio.sleep(cooldown)
            await rainbow_role.edit(color=discord.Color.random())

def setup(client):
    client.add_cog(RainbowRoleListener(client))