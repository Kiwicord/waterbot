import discord
from discord.ext import commands
from emojis import Emojis

class Eingang(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def eingang(self, ctx):
        banner = discord.Embed(
            color=0x415fe6,
        )
        banner.set_image(url='https://media.discordapp.net/attachments/734005704704131122/942487344844529684/ww_template_2.png?width=1440&height=206')

        willkommen = discord.Embed(
            color=0x415fe6,
            title='1. Willkommen',
            description=f'{Emojis.FISHAUFWISH} Willkommen bei uns! Dein Platz für gute Laune! {Emojis.FISHAUFWISH}\n{Emojis.PFEIL} Die Waterworld!\n\n{Emojis.STRICH}\nAuf unserem Server bieten wir dir:\n{Emojis.KREUZ} VIP Pass (Waterpass)\n{Emojis.KREUZ} Viele Giveaways & Events\n{Emojis.KREUZ} Ein Großes Serverteam das dir bei Sorgen und Problemen weiterhilft\n{Emojis.KREUZ} Eine komplexe Serverhilfe!\n\nUnd noch vieles weitere!\n{Emojis.STRICH}                                                                         '
        )
        channel = discord.Embed(
            color=0x415fe6,
            title='2. Channel',
            description=f'Hier gibt es eine Erklärung für die wichtigsten Channel!\n\n<#813039986999558156> - Chat zum Schreiben\n<#813042366750392340> - Finde Leute zum spielen verschiedener Games\n<#813042407989575720> - Alle Bilder und Videos\n<#813042687393529857> - Hier könnt ihr euch vorstellen.\n<#813042590206525460> - Für Alle Bot Befehle\n\n{Emojis.STRICH}'
        )
        team = discord.Embed(
            color=0x415fe6,
            title='3. Team',
            description=f'Wir stehen euch mit Rat und Tat zur Seite!\nHier findest du ein kleinen Überblick auf unser Serverteam\n{Emojis.STRICH}\nUnd jetzt kannst du dich selbst von unserem Server überzeugen lassen! <a:ente:899332240876666960>'
        )
        team.set_image(url='https://cdn.discordapp.com/attachments/942465654261440592/942512168849514566/ok.png')
        await ctx.send(embed=banner)
        await ctx.send(embed=willkommen)
        await ctx.send(embed=channel)
        await ctx.send(embed=team)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Eingang(client))