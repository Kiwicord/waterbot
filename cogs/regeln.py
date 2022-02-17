import discord
from discord.ext import commands
from emojis import Emojis

class Regelwerk(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def regeln(self, ctx):
        banner = discord.Embed(color=0x415fe6)
        banner.set_image(url='https://media.discordapp.net/attachments/734005704704131122/942730746391588934/regeln.png?width=1440&height=206')

        regel = discord.Embed(
            color=0x415fe6,
            title='Regeln',
            description=f'Folgendes ist zu beachten\n\n{Emojis.KREUZ} Seid freundlich zueinander!\n{Emojis.KREUZ} Respektiert andere so, wie ihr behandelt respektiert werden wollt!\n{Emojis.KREUZ} Nachrichten sind bitte NUR in ihren vorgegebenen Channel zu posten. Verhältnismäßig nicht zu dem Channel passende Nachrichten werden überprüft und gelöscht.\n{Emojis.STRICH}\nWas nicht gerne gesehen ist:\n{Emojis.KREUZ} Bitte keine Channel oder sonstige Kanäle zuspammen, es sei denn, es findet in dafür vorgesehene Channel statt.\n{Emojis.KREUZ} Auf gar keinen Fall andere beleidigen oder beschuldigen, für was sie nicht getan haben!\n{Emojis.KREUZ} Das verschicken von nationalistischen oder sexistischen Inhalten ist untersagt!\n{Emojis.STRICH}\nWas dich bei Missachtung erwartet:\n\n{Emojis.KREUZ} In Zweifelsfällen obliegt es den Moderatoren angemessene Entscheidungen zu treffen.\n{Emojis.KREUZ} Die Entscheidungen der Moderatoren sind zu respektieren.\n{Emojis.KREUZ} Solltet ihr euch ungerecht behandelt fühlen, wendet euch über einen privaten (!) Chat an einen anderen Moderator und erläutert die Situation. Eine Diskussion in den öffentlichen Kanälen ist nicht erwünscht\n{Emojis.STRICH}\n(Außerdem gelten auch die offiziellen Discord Guidelines: https://discordapp.com/guidelines)'
        )
        await ctx.send(embed=banner)
        await ctx.send(embed=regel)
        await ctx.message.delete()

def setup(client):
    client.add_cog(Regelwerk(client))