import discord
from discord.ext import commands
import random
import asyncio

cooldown = 3600

class RainbowRoleListener(commands.Cog):
    def __init__(self, client):
        self.client = client
        print('rainbow role listener cog ready')

    

def setup(client):
    client.add_cog(RainbowRoleListener(client))
