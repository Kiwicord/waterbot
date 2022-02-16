import discord
from discord.ext import commands
from emojis import Emojis

class WaterworldInfos(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def infos(self, ctx):
        info_banner = discord.Embed(
            color=0x415fe6,
        )
        info_banner.set_image(url='https://media.discordapp.net/attachments/734005704704131122/942727653885095976/informationen.png?width=1440&height=206')
        await ctx.send(embed=info_banner)

        info = discord.Embed(
            color=0x415fe6,
            title='Informationen',
            description=f'{Emojis.STRICH}\n\n{Emojis.KREUZ} Im folgenden findest du einige Informationen, welche für dich als  \nNutzer unseres Servers wichtig sind, damit du dich gut zurecht\nfindest. {Emojis.FISHAUFWISH}\n\n{Emojis.PFEIL} Hier gibt es Informationen zu:\n     {Emojis.PUNKT} Booster\n    {Emojis.PUNKT} Levelsystem\n\n{Emojis.STRICH}'
        )
        await ctx.send(embed=info)
        await ctx.message.delete()
    
    @commands.command()
    async def booster(self, ctx):
        booster_banner = discord.Embed(color=0x415fe6)
        booster_banner.set_image(url='https://cdn.discordapp.com/attachments/734005704704131122/942729624402677790/booster.png')

        booster_embed = discord.Embed(
            color=0x415fe6,
            title='Booster',
            description=f'{Emojis.STRICH}\n\n<a:nitroboost:858410542523744316> **1x Booster**\n{Emojis.KREUZ} 6 Monate Waterpass geschenkt\n{Emojis.KREUZ} Sprudelwasser Rolle (für immer)\n{Emojis.KREUZ} Eigene Rolle\n{Emojis.KREUZ} eigener Talk im Teambereich\n{Emojis.KREUZ} Server-Booster Rolle\n{Emojis.KREUZ} Alle Levelrollen Vorteile\n{Emojis.KREUZ} 60% Levelbooster für immer\n\n<a:boost:943447628052590642> **2x Booster**\n{Emojis.KREUZ} Alle Vorteil aus "1x Booster"\n{Emojis.KREUZ} Weitere 3 Monate Waterpass\n{Emojis.KREUZ} Schreibberechtigung in <#813533839804203038>\n{Emojis.KREUZ} Unterstützerrolle\n{Emojis.KREUZ} Geldzurückzahlung des Nitros nach 3 Wochen boosten\n{Emojis.KREUZ} Eigener Bot (Programmierung durch <@733403498766401554>)\n\n{Emojis.STRICH}'
        )
        await ctx.send(embed=booster_banner)
        await ctx.send(embed=booster_embed)
        await ctx.message.delete()

    @commands.command()
    async def level(self, ctx):
        level_banner = discord.Embed(
            color=0x415fe6,
        )
        level_banner.set_image(url='https://media.discordapp.net/attachments/734005704704131122/942730459337596968/level.png?width=1440&height=206')

        level_embed = discord.Embed(
            color=0x415fe6,
            title='Level',
            description=f'{Emojis.STRICH}\n\n<@&831253822194057276> - Level 5 - 1.5% mehr Punkte in Spiel und Spaß\n<@&831253820918988853> - Level 10 - 5% Levelbooster\n<@&831253821854187573> - Level 15 - 1 Monat Waterpass\n<@&831253820074885189> - Level 20 - Senden einer Umfrage\n<@&831253818636370011> - Level 25 - VIP Rang\n<@&831253818594426941> - Level 30 - +1 Level geschenkt\n<@&831253817286066196> - Level 35 - Eigene Rollfarbe\n<@&831253814832005130> - Level 40 - Absoluter Aktivitätsrang\n<@&831253817223938118> - Level 45 - VIP Commands\n<@&831253815822123008> - Level 50\n- Anfrage ins Team (14 Tage Testphase)\n- 1 Monat Nitro Classic\n- 3% mehr Punkte in Spiel und Spaß\n\n{Emojis.STRICH}\n\nDamit sollte alles geklärt sein\nWir wünschen dir viel Spaß auf den Server <:hug:835547333651464202>'
        )

        await ctx.send(embed=level_banner)
        await ctx.send(embed=level_embed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(WaterworldInfos(client))