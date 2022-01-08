import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import asyncio

from commands.test import Test
from commands.ban import Ban
from commands.kick import Kick
from commands.hack import Hack
from commands.gay import Gay
from commands.fisch import Fisch
from commands.levels import LevelSystem
from error import CommandErrorHandler

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    while True:
        await client.change_presence(activity=discord.Game(name=f"mit {str(len(client.guilds))} Servern"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="mit Kuappis Fischen"))
        await asyncio.sleep(10)

async def setup():
    await client.wait_until_ready()
    client.add_cog(Test(client))
    client.add_cog(Ban(client))
    client.add_cog(Kick(client))
    client.add_cog(Hack(client))
    client.add_cog(Gay(client))
    client.add_cog(Fisch(client))
    client.add_cog(LevelSystem(client))
    client.add_cog(CommandErrorHandler(client))


load_dotenv()
client.loop.create_task(setup())
client.run(getenv('TOKEN'))