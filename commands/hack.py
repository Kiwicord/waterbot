import discord
from discord.ext import commands
import random
import asyncio

NAMES = ['Kevin', 'Thomas', 'Marc', 'Jonas', 'Lukas', 'Niklas', 'Anne', 'Josefine', 'Ivana', 'Petra', 'Ines', 'Lars', 'Tim', 'Maximilian', 'Angelina', 'Reijan', 'Torsten', 'Patrick', 'Joris']
SURNAMES = ['Ewers', 'Steinthal', 'Schneider', 'Schleicher', 'Maria-Reich', 'Naune', 'Amthor', 'Tellerschmidt', 'Schaade', 'Baguette', 'Koch', 'Westphal', 'Pfosten', 'Stieler', 'Franz']
STREET = ['Am Sonnenweg 21', 'Forstgasse 4', 'Mannheimerstraße 5', 'Geibelstraße 6', 'Ginsterweg 3', 'Karl-Jaspers-Str. 41c', 'Brandenburger Str. 30b']
CITY = ['Mannheim', 'Zella-Mehlis', 'Leipzig', 'Ludwigsburg', 'Frankfurt', 'Berlin']
EMAIL = ['limoessen@gmail.com', 'klappbettbüro@gmail.com', 'ines.schneider@schule.thueringen.de', 'romkinemail@gmail.com', 'contact.moyaiugriefing@gmail.com']
PASSWORDS = ['ficken123', 'passwort123', 'htg6gS2k', 'steinthal', 'vplan', 'schueler123@', 'fK%/6kC/8#>ev', 'passwort', 'rbleipzig69']

CHANCE = ['TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE', 'FALSE']

class Hack(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hack(self, ctx, *, user):
        vorname = random.choice(NAMES)
        nachname = random.choice(SURNAMES)
        #######
        ip1 = random.randint(0, 255)
        ip2 = random.randint(0, 255)
        ip3 = random.randint(0, 255)
        ip4 = random.randint(0, 255)
        #######
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
        embed_fail = discord.Embed(color=0xff6961, title='Hack gescheitert! Der User hat eine VPN an!')

        prob = random.choice(CHANCE)

        embed.add_field(name='🎫 » Name', value=f'*{vorname} {nachname}*', inline=False)
        embed.add_field(name='🖥️ » IP-Adresse', value=f'*{ip1}.{ip2}.{ip3}.{ip4}*', inline=False)
        embed.add_field(name='📌 » Wohnort', value=f'*{wohnort}*', inline=False)
        embed.add_field(name='🏠 » Straße und Hausnummer', value=f'*{street}*', inline=False)
        embed.add_field(name='✉️ » E-Mail Adresse', value=f'*{email}*', inline=False)
        embed.add_field(name='⚙️ » Passwort', value=f'*{password}*', inline=False)

        embed.set_footer(text='Dies sollte nicht ernst genommen werden da diese Daten zufällig generiert werden!')

        if prob == 'TRUE':
            await msg2.edit('Erfolgreich!', embed=embed)
        elif prob == 'FALSE':
            await msg2.edit(embed=embed_fail)



    
def setup(client):
    client.add_cog(Hack(client))