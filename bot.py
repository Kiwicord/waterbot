import discord
from discord.ext import commands
import asyncio
import os
from cogs.rainbow_role import *

client = commands.Bot(command_prefix='-')

intents = discord.Intents.default()
intents.members = True

async def change_rainbow_role_color():
    # rainbow rolle
    guild = client.get_guild(813039986545917965)
    rainbow_role_id = 850832485658787840
    rainbow_role = discord.utils.get(guild.roles, id=rainbow_role_id)
    while True:
        await rainbow_role.edit(color=discord.Color.random())
        await asyncio.sleep(cooldown)

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    await change_rainbow_role_color()

    while True:
        # status
        await client.change_presence(activity=discord.Game(name=f"mit {str(len(client.guilds))} Servern"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="mit Kuappis Fischen"))
        await asyncio.sleep(10)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

client.run('OTI5Mzg1ODE5NDAyMjk3NDQ2.Ydmj_g.dRq7A_qeC-XY0X3E43-DzZ1EGQw')
