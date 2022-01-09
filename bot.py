import discord
from discord.ext import commands
import asyncio
import threading

from commands.test import Test
from commands.ban import Ban
from commands.kick import Kick
from commands.hack import Hack
from commands.gay import Gay
from commands.fisch import Fisch
from commands.levels import LevelSystem
from music.player_main import MusicPlayer
from economy.main import EconomyManager

from listeners.rainbow_role import RainbowRoleListener

client = commands.Bot(command_prefix='-')

intents = discord.Intents.default()
intents.members = True

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    while True:
        # status
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
    client.add_cog(RainbowRoleListener(client))
    client.add_cog(MusicPlayer(client))
    client.add_cog(EconomyManager(client))

client.loop.create_task(setup())
client.run('OTI5Mzg1ODE5NDAyMjk3NDQ2.Ydmj_g.op4sq36zQqAF_N5fhWES9Gi23hQ')
