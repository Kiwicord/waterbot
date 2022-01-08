import discord
from discord.ext import commands
import random
import asyncio

NAMES = ['Kevin', 'Thomas', 'Marc', 'Jonas', 'Lukas', 'Niklas', 'Anne', 'Josefine', 'Ivana', 'Petra', 'Ines', 'Lars', 'Tim', 'Maximilian', 'Angelina', 'Reijan', 'Torsten', 'Patrick', 'Joris']
SURNAMES = ['Ewers', 'Steinthal', 'Schneider', 'Schleicher', 'Maria-Reich', 'Naune', 'Amthor', 'Tellerschmidt', 'Schaade', 'Baguette', 'Koch', 'Westphal', 'Pfosten', 'Stieler', 'Franz']
IPS = ['25.39.130.162', '17.122.74.36', '188.102.31.164', '187.36.196.138', '45.201.137.226', '212.102.57.142']
STREET = ['Am Sonnenweg 21', 'Forstgasse 4', 'Mannheimerstraße 5', 'Geibelstraße 6', 'Ginsterweg 3', 'Karl-Jaspers-Str. 41c', 'Brandenburger Str. 30b']
CITY = ['Mannheim', 'Zella-Mehlis', 'Leipzig', 'Ludwigsburg', 'Frankfurt', 'Berlin']
EMAIL = ['limoessen@gmail.com', 'klappbettbüro@gmail.com', 'ines.schneider@schule.thueringen.de', 'romkinemail@gmail.com', 'contact.moyaiugriefing@gmail.com']
PASSWORDS = ['ficken123', 'passwort123', 'htg6gS2k', 'steinthal', 'vplan', 'schueler123@', 'fK%/6kC/8#>ev', 'passwort', 'rbleipzig69']

class Hack(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hack(self, ctx, *, user):
        vorname = random.choice(NAMES)
        nachname = random.choice(SURNAMES)
        ip = random.choice(IPS)
        wohnort = random.choice(CITY)
        street = random.choice(STREET)
        email = random.choice(EMAIL)
        password = random.choice(PASSWORDS)

        
        

        

        embed1 = discord.Embed(color=0x415fe6, title=f'<a:laden:858410012690350141> Hacke {user}...')
        msg = await ctx.send(embed=embed1)
        await asyncio.sleep(2)
        embed2 = discord.Embed(color=0x415fe6, title=f'<a:laden:858410012690350141> Extrahiere Datenbank-Parameter von {user}...')
        msg2 = await msg.edit(embed=embed2)
        await asyncio.sleep(2)
        embed = discord.Embed(color=0x77dd77, title=f'Daten von {user}')

        embed.add_field(name='Name', value=f'{vorname} {nachname}', inline=False)
        embed.add_field(name='IP-Adresse', value=ip, inline=False)
        embed.add_field(name='Wohnort', value=wohnort, inline=False)
        embed.add_field(name='Straße und Hausnummer', value=street, inline=False)
        embed.add_field(name='E-Mail Adresse', value=email, inline=False)
        embed.add_field(name='Passwort', value=password, inline=False)

        embed.set_footer(text='Dies sollte nicht ernst genommen werden da diese Daten zufällig generiert werden!')
        await msg2.edit('Erfolgreich!', embed=embed)


    
def setup(client):
    client.add_cog(Hack(client))