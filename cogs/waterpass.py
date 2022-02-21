import discord
from discord.ext import commands
from emojis import Emojis, Waterworld

class Waterpass(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def waterpass(self, ctx):
        banner = discord.Embed(color=Waterworld.BLUE)
        banner.set_image(url='https://media.discordapp.net/attachments/734005704704131122/943530182113894400/waterpass.png?width=1440&height=206')
        
        embed = discord.Embed(
            color=Waterworld.BLUE,
            title='💙 Der Waterpass 💙',
            description=f'Vielen Dank für den Kauf des Waterpass!\n\n{Emojis.PFEIL} Den Waterpass behälst du jetzt genau 1 Monat nachdem du den Waterpass gekauft hast.\n{Emojis.PFEIL} Dannach musst du erneut **50.000**🥝 oder **50.000 Dank Memer Coins** uns überweisen __**oder**__ die Waterpass Mitgliedchaft kündigen.\n\n{Emojis.KREUZ} Du fragst dich sicherlich, was du jetzt alles für Vorteile mit dem Waterpass hast\n{Emojis.KREUZ} **Daher hast du hier eine Liste an Vorteilen:**\n\n{Emojis.STRICH}\n\n{Emojis.KREUZ} Ein VIP Chat ohne Slow-Modus\n{Emojis.KREUZ} Ein VIP Talk mit 128kbps (Normale Talks haben nur 69kbps)\n{Emojis.KREUZ} Ein Spamchat (Erlaubt bei Aktivitätevents um Nachrichten zu sammeln)\n{Emojis.KREUZ} Ein  24/7 Entspannungsmusik Talk\n{Emojis.KREUZ} VIP Gewinnspiele (Auch Nitro)\n{Emojis.KREUZ} 2% mehr Punkte in <#834338745451806780> Events\n{Emojis.KREUZ} Ihr könnt eine Umfrage pro Tag stellen (<#813533839804203038>)\n{Emojis.KREUZ} Schnellere Anfertigung von Bannern in <#943623287186010122>\n{Emojis.KREUZ} Ihr seid direkt unter dem Team gelistet\n{Emojis.KREUZ} Zugriff auf mehr Farben als normale Mitglieder\n{Emojis.KREUZ} Events ein paar Tage früher schauen\n{Emojis.KREUZ} Rainbowrolle\n\n{Emojis.STRICH}\n\n{Emojis.PUNKT} Bei Fragen zum Waterpass steht das Team gerne zur Verfügung: **waterpasswaterworld@gmail.com**\n\n__**Wir wünschen euch viel Spaß mit dem Waterpass**__'

        ) 
        await ctx.send(embed=banner)
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(Waterpass(client))