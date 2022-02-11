import discord
from discord.ext import commands
import asyncio
import os
from listeners.rainbow_role import *

client = commands.Bot(command_prefix=',')

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

    # await change_rainbow_role_color()

    while True:
        # status
        await client.change_presence(activity=discord.Game(name=f"mit {str(len(client.guilds))} Servern"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="mit Kuappis Fischen"))
        await asyncio.sleep(10)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'commands.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')

for filename in os.listdir("./commands"):
	if filename.endswith(".py"):
		client.load_extension(f"commands.{filename[:-3]}")

client.run('ODUwODI5MDU5MjEwNzM5NzYz.YLvaTw.1eTl7oP9Mdu_hG7k6Kj9PNSYjAQ')
