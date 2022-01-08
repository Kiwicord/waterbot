import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            
            embed1 = discord.Embed(title='Fehler!', color=0xff6961, description='Du hast keine Berechtigungen um diesen Befehl auszuführen!')
            await ctx.send(embed=embed1)

        if isinstance(error, commands.CommandNotFound):
                    
            embed = discord.Embed(title="Fehler!", color=0xff6961, description=f'Der Befehl wurde nicht gefunden!')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandErrorHandler(client))