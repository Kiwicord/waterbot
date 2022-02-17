import discord
from discord.ext import commands
from data.db import *
import asyncio

level = ['💙 » Neptun', '🐟 » Nemo', '🐡 » Kugelfisch', '🐠 » Goldfisch', '🦈 » Hecht', '🐡 » Molly', '🐋 » Blauwal', '🐟 » Forelle', '🐬 » Delfin', '🧜‍♂️ » Herrscher des Meeres']
levelnum = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

class LevelSystem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        stats = levelling.find_one({'_id': message.author.id})
        if not message.author.bot:
            if stats is None:
                newuser = {'_id': message.author.id, 'xp': 0}
                levelling.insert_one(newuser)
            else:
                increase = 5
                xp = stats['xp'] + increase
                levelling.update_one({'_id': message.author.id}, {'$set':{'xp': xp}})
                lvl = 0
                while True:
                    if xp < ((50*(lvl**2))+(50*(lvl-1))):
                        break
                    lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                if xp == increase:
                    if lvl == 1:
                        return
                    embed_levelup = discord.Embed(
                    color=0x415fe6,
                    title='<a:bewegendeszeichenlmao:943458842933600266> Neues Level!',
                    description=f'Du bist nun Level {lvl}!'
                    )
                    await message.channel.send(embed=embed_levelup)
                    for i in range(len(level)):
                        if lvl == levelnum[i]:
                            await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                            embed_levelup.description = f'Du hast die Rolle **{level[i]} freigeschaltet!**'
                            await message.channel.send(embed=embed_levelup)
                

    @commands.command()
    async def rank(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
        
        if not levelling.find_one({'_id': member.id}):
            levelling.insert_one({'_id': member.id, 'xp': 0})
        stats = levelling.find_one({'_id': member.id})

        xp = stats['xp']
        lvl = 0
        rank = 0

        while True:
            if xp < ((50*(lvl**2))+(50*(lvl-1))):
                break
            lvl += 1
        xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))

        boxes = int((xp/(200*((1/2) * lvl)))*20)
        rankings = levelling.find().sort('xp', -1)

        for x in rankings:
            rank += 1
            if stats['_id'] == x['_id']:
                break
        embed = discord.Embed(title=f'Level Statistiken von {member}', color=0x415fe6)
        embed.add_field(name='Name', value=member.mention, inline=True)
        embed.add_field(name='Level', value=f'{lvl}', inline=True)
        embed.add_field(name='XP', value=f'{xp}/{int(200*((1/2)*lvl))}', inline=True)
        embed.add_field(name='Platz', value=f'{rank}/{ctx.guild.member_count}', inline=True)
        embed.add_field(name='Level Fortschritt', value=boxes * ':blue_square:' + (20-boxes) * ':white_large_square:', inline=False)
        try:
            embed.set_thumbnail(url=member.avatar_url)
        except AttributeError:
            embed.set_thumbnail(url=member.default_avatar_url)
        await ctx.reply(embed=embed, mention_author=False)



def setup(client):
    client.add_cog(LevelSystem(client))
