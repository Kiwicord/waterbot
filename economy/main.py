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

async def update_bank(user, change=0, mode='wallet'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change

    with open('bank.json', 'r') as f:
        json.dump(users, f)

    bal = [users[str(user.id)]['wallet'], users[str(user.id)]['bank']]
    return bal

class EconomyManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):

        user = ctx.author

        await open_account(ctx.author)
        users = await get_bank_data()

        wallet_amt = users[str(user.id)]['wallet']
        bank_amt = users[str(user.id)]['bank']

        embed = discord.Embed(title=f'<a:bewegendeszeichenlmao:920059343108452353> Kontostand von {ctx.author}', color=0x415fe6)
        embed.add_field(name='Geld', value=f'**{wallet_amt}**🐚', inline=False)
        embed.add_field(name='Bank', value=f'**{bank_amt}**🐚', inline=False)
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
    
    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, amount=None):

        await open_account(ctx.author)

        if amount == None:
            embed = discord.Embed(color=0x415fe6, description='<a:bewegendeszeichenlmao:920059343108452353> Bitte gib einen Betrag an, der von deiner Bank abgehoben werden soll.')
            await ctx.send(embed=embed)
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)

        if amount > bal[1]:
            embed1 = discord.Embed(color=0x415fe6, description='<a:bewegendeszeichenlmao:920059343108452353> Du hast nicht genügend Geld auf der Bank.')
            await ctx.send(embed=embed1)
            return
        
        if amount < 0:
            embed2 = discord.Embed(color=0x415fe6, description='<a:bewegendeszeichenlmao:920059343108452353> Du kannst keinen negativen Betrag abheben.')
            await ctx.send(embed=embed2)
            return
        
        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1*amount, 'bank')

        embed3 = discord.Embed(color=0x415fe6, title='<a:bewegendeszeichenlmao:920059343108452353> Erfolgreich abgehoben!', description=f'Du hast erfolgreich **{amount}**🐚 von deiner Bank abgehoben.')
        await ctx.send(embed=embed3)

def setup(client):
    client.add_cog(EconomyManager(client))