import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

from commands.test import Test
from commands.ban import Ban
from commands.kick import Kick

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def setup():
    await client.wait_until_ready()
    client.add_cog(Test(client))
    client.add_cog(Ban(client))
    client.add_cog(Kick(client))


load_dotenv()
client.loop.create_task(setup())
client.run(getenv('TOKEN'))