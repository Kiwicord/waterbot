import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandError):

            embed = discord.Embed(title="Fehler!", color=0xff6961, description=f"```{error}```")
            embed.set_footer(text="Um den Fehler zu reporten, wende dich bitte an das Serverteam.")

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandErrorHandler(client)) 
