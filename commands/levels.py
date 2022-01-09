import discord
from discord import File
from discord.ext import commands
from typing import Optional
from easy_pil import Editor, load_image_async, Font
import json
import random

level = [
    '💙 » Neptun', 
    '🐟 » Nemo', 
    '🐡 » Kugelfisch', 
    '🐠 » Goldfisch', 
    '🦈 » Hecht', 
    '🐡 » Kugelfisch', 
    '🐋 » Blauwal', 
    '🐟 » Forelle', 
    '🐬 » Delfin', 
    '🧜‍♂️ » Herrscher des Meeres'
]

level_num = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


class LevelSystem(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Level-System wurde erfolgreich geladen')
    
    # erhöht xp
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.content.startswith('-'):
            if not message.author.bot:
                with open('levels.json', 'r') as f:
                    data = json.load(f)
                
                if str(message.author.id) in data:
                    xp = data[str(message.author.id)]['xp']
                    lvl = data[str(message.author.id)]['level']
                    
                    amt = random.randint(0, 10)

                    increased_xp = xp + amt
                    new_level = int(increased_xp/100)

                    data[str(message.author.id)]['xp'] = increased_xp

                    with open('levels.json', 'w') as f:
                        json.dump(data, f, indent=4)
                    
                    if new_level > lvl:
                        new_level_embed = discord.Embed(color=0x415fe6, title='<a:bewegendeszeichenlmao:920059343108452353> Level aufgestiegen!', description=f'{message.author.mention} ist nun Level **{new_level}**!')
                        await message.channel.send(embed=new_level_embed)
                        data[str(message.author.id)]['level'] = new_level
                        data[str(message.author.id)]['xp'] = 0

                        with open('levels.json', 'w') as f:
                            json.dump(data, f, indent=4)

                        for i in range(len(level)):
                            if new_level == level_num[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))

                                new_role_embed = discord.Embed(color=0x415fe6, description=f'{message.author.mention} hat die Rolle **{level[i]}** freigeschaltet!')
                                await message.channel.send(embed=new_role_embed)
                else:
                    data[str(message.author.id)] = {}
                    data[str(message.author.id)]['xp'] = 0
                    data[str(message.author.id)]['level'] = 1

                    with open('levels.json', 'w') as f:
                        json.dump(data, f, indent=4)
    @commands.command(aliases=['level'])
    async def rank(self, ctx, user : Optional[discord.Member]):
        member = user or ctx.author

        with open('levels.json', 'r') as f:
            data = json.load(f)
        
        xp = data[str(member.id)]['xp']
        lvl = data[str(member.id)]['level']

        next_level_up_xp = (lvl+1)*100
        xp_needed = next_level_up_xp
        xp_have = data[str(member.id)]['xp']

        percentage = int(((xp_have*100)/xp_needed))

        background = Editor('zIMAGE.png')
        profile = await load_image_async(str(member.avatar_url))
        profile = Editor(profile).resize((150, 150)).circle_image()

        poppins = Font.poppins(size=40)
        poppins_small = Font.poppins(size=30)

        #you can skip this part, I'm adding this because the text is difficult to read in my selected image
        ima = Editor("zBLACK.png")
        background.blend(image=ima, alpha=.5, on_top=False)

        background.paste(profile.image, (30, 30))

        background.rectangle((30, 220), width=650, height=40, fill="#fff", radius=20)
        background.bar(
            (30, 220),
            max_width=650,
            height=40,
            percentage=percentage,
            fill="#ff9933",
            radius=20,
        )
        background.text((200, 40), str(member.name), font=poppins, color="#ff9933")

        background.rectangle((200, 100), width=350, height=2, fill="#ff9933")
        background.text(
            (200, 130),
            f"Level: {lvl}   "
            + f" XP: {xp} / {(lvl+1) * 100}",
            font=poppins_small,
            color="#ff9933",
        )

        card = File(fp=background.image_bytes, filename='zCARD.png')
        await ctx.send(file=card)
    
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def setlevel(self, ctx, member : discord.Member, new_level : int):
        with open('levels.json', 'r') as f:
            data = json.load(f)
        
        level = data[str(member.id)]['level']
        data[str(member.id)]['level'] = new_level

        with open('levels.json', 'w') as f:
            json.dump(data, f, indent=4)

        embed = discord.Embed(color=0x415fe6, title='<a:bewegendeszeichenlmao:920059343108452353> Level gesetzt!', description=f'{member.mention} ist nun **Level {new_level}**.')
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(LevelSystem(client))


