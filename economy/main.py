import discord
from discord.ext import commands
import json
import random

async def open_account(user):
    users = await get_bank_data()
    
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0 # allgemeines geld auf der hand
        users[str(user.id)]['bank'] = 0 # geld in der bank

    with open('bank.json', 'w') as f:
        json.dump(users, f)
    return True

async def get_bank_data():
    with open('bank.json', 'r') as f:
        users = json.load(f)
    return users

class EconomyManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def balance(self, ctx):

        user = ctx.author

        await open_account(ctx.author)
        users = await get_bank_data()

        wallet_amt = users[str(user.id)]['wallet']
        bank_amt = users[str(user.id)]['bank']

        embed = discord.Embed(title=f'<a:bewegendeszeichenlmao:920059343108452353> Kontostand von {ctx.author}', color=0x415fe6)
        embed.add_field(name='Geld', value=f'**{wallet_amt}** 🐚', inline=False)
        embed.add_field(name='Bank', value=f'**{bank_amt}** 🐚', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def work(self, ctx):

        user = ctx.author

        await open_account(ctx.author)
        users = await get_bank_data()

        income = random.randint(1, 100)

        embed = discord.Embed(color=0x415fe6, title='<a:bewegendeszeichenlmao:920059343108452353> Gearbeitet!', description=f'Du hast für **{income}** 🐚 gearbeitet.')
        await ctx.send(embed=embed)
        wallet_amt = users[str(user.id)]['wallet']
        users[str(user.id)]['wallet'] += income



        with open('bank.json', 'w') as f:
            json.dump(users, f, indent=4)



def setup(client):
    client.add_cog(EconomyManager(client))