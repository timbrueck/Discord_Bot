import discord
from discord.ext import commands, tasks
import random
import os  
from itertools import cycle


bot = commands.Bot(command_prefix = '<')

newUserMessage = "Hey"

status = cycle(['mit deiner Mutter', 'mit euren Gefühlen', 'kein Fortnite weil das scheiße ist', 'kein PokemonGo', 'nur Trinkspiele'])

#Events
@bot.event
async def on_ready():
    status_change.start()
    print("The bot is ready")


#Change bot's status
@tasks.loop(seconds=10)
async def status_change():
    await bot.change_presence(activity=discord.Game(next(status)))




#Commands
@bot.command()
async def helppp(ctx):
    await ctx.send(f'Hier eine Liste mit Commands: \n <ping - zeigt dir deinen Ping \n <8ball - Ich beantworte dir eine Frage \n <insult - Ich beleidige jemanden xD \n Liste mit Commands für Admins: \n <kick \n <ban / <unban \n <clear - löscht Nachrichten aus dem Chat') 

@bot.command()
async def ping(ctx):
    await ctx.send(f'Dein Ping ist: {round(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Ja safe', 'Ne bruda', 'Versuche es später nochmal grad kein Bock zu reden', 'Ja klar Diggah', 'Meine Antwort ist ne', 'Ich denk schon', 'Frag doch jemand anderen']
    await ctx.send(f'Frage: {question}\nAntwort: {random.choice(responses)}')

@bot.command(aliases=['Beleidige'])
async def insult(ctx, member : discord.Member):
    insults = ['Du siehst scheiße aus ', 'Du stinkst', 'Dein pp: 8=>\n Mein pp: 8===============>']
    await ctx.send(f'{random.choice(insults)} {member.mention}')

@bot.command()
async def test(ctx):
    await ctx.send("Florian ist ein Hund")

@bot.command()
async def hafti(ctx):
    h1 = open ('haft1.txt')
    h2 = open ('haft2.txt')
    h3 = open ('haft3.txt')

    whichhaft = [h1, h2, h3]
    result = random.choice(whichhaft)
    print(result)

    

    await ctx.send(result.read())

#Commands but not for everyone
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1) 
    print(f'{amount} messages have been deleted')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason) 
    await ctx.send(f'{member.mention} wurde vom Server gekickt lol')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} wurde vom Server gebannt. Opfer')

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name}#{user.discriminator} wurde entbannt')
            return







bot.run('ODEwODYzNTcwMTc0MjE0MjE2.YCp1jA.6gZBX49SSAejCamyDN0tGlibKag')
