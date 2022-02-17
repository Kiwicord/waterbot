import discord
from discord.ext import commands
from emojis import Emojis, Waterworld

class Bannerecke(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def bannerecke(self, ctx):
        banner = discord.Embed(color=Waterworld.BLUE)
        banner.set_image(url='https://media.discordapp.net/attachments/734005704704131122/943529789489311744/bannerecke.png?width=1440&height=206')

        embed = discord.Embed(
            color=Waterworld.BLUE,
            title='Bannerecke',
            description=f'{Emojis.STRICH}\n\n{Emojis.PFEIL} Herzlichen Willkommen in unserer  kleinen Bannerecke!\n\nWir fertigen an:\n{Emojis.KREUZ} Banner\n{Emojis.KREUZ} Animierte Banner\n{Emojis.KREUZ} Serverlogos\n{Emojis.KREUZ} Emojis\n{Emojis.KREUZ} Auf Anfrage auch was anderes\n\n{Emojis.STRICH}\n\n**Unsere Bannermaker:**\n\n{Emojis.KREUZ} <@448838374468485123>\n{Emojis.KREUZ} <@689558970796343380>\n{Emojis.KREUZ} <@696710421004025907>\n{Emojis.KREUZ} <@733403498766401554>\n\nAlle Banneranfragen können in <#943867821044154478> gestellt werden und werden rechtzeitig bearbeitet.'

        )
        await ctx.send(embed=banner)
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(Bannerecke(client))