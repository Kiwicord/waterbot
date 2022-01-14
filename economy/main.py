import discord
from discord.ext import commands
from database_connector import *
import random

class EconomyManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):

        await check_account(str(ctx.author.id))

        info = await select_from_database(ctx.author.id)

        user_id = info[0]
        wallet = info[1]
        bank = info[2]
        await ctx.send(f'Kontostand für <@{user_id}>\nGeld: {wallet}\nBank: {bank}')

    @commands.command()
    async def work(self, ctx):
        await check_account(ctx.author.id)
        income = random.randint(1, 1000)
        await update_wallet(ctx.author.id, income)
        await ctx.send(f'Du hast für {income}€ gearbeitet')

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, amount=None):
        await check_account(ctx.author.id)
        info = await select_from_database(ctx.author.id)
        wallet = info[1]
        if amount == None:
            await ctx.send('Der Betrag darf nicht leer sein')
            return
        if wallet <= 0:
            await ctx.send('Du hast nicht genügend Geld')
            return
        if amount == 'all':
            await deposit_amount(ctx.author.id, amount=wallet)
            await ctx.send(f'Du hast {wallet}€ auf dein Konto überwiesen.')
            return
        await deposit_amount(ctx.author.id, amount=amount)
        await ctx.send(f'Du hast {amount}€ auf dein Konto überwiesen.')

    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, amount):
        await check_account(ctx.author.id)
        info = await select_from_database(ctx.author.id)
        bank = info[2]
        if amount == None:
            await ctx.send('Der Betrag darf nicht leer sein')
            return
        if bank <= 0:
            await ctx.send('Du hast nicht genügend Geld auf der Bank')
            return
        if amount == 'all':
            await withdraw_amount(ctx.author.id, amount=bank)
            await ctx.send(f'Du hast {bank}€ abgehoben.')
            return
        await withdraw_amount(ctx.author.id, amount=amount)
        await ctx.send(f'Du hast {amount}€ abgehoben.')

def setup(client):
    client.add_cog(EconomyManager(client))