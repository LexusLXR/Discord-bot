import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

import requests
import json

bot_token= open('Config.json', 'r')
data= json.load(bot_token)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='*', intents=intents)

queues= {}
def check_queue(ctx, id):
    if id in queues and queues[id]:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)

@bot.event
async def on_ready():
    print("Bot is ready for use desu")
    print("Fuck me nyaaaa desuu")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello nyaa! I am Kage's personal pet. Nice to meet you.")
@bot.command()    
async def hi(ctx):
    await ctx.send("Fuck me nyaaaa desuu")

@bot.command()    
async def greet(ctx, member: discord.Member):
    await ctx.send(f'Hello {member.mention} desu! i am your slave desu! ||plz cum on me desu!!||')

@bot.event
async def on_member_join(member):
    
    welcome_channel_id = 863643976333262871 
    welcome_channel = member.guild.get_channel(863643976333262871)
    # Mention the new member and send a welcome message
    
    
    if welcome_channel:
        await welcome_channel.send(f'konichiwa{member.mention} desu! Welcome to the server! if you need anything dont ask kage because he is dum dum ask me instead desu ')

@bot.event
async def on_member_remove(member):
    goodbye_channel = member.guild.get_channel(863643976333262871)

    if goodbye_channel:
        await goodbye_channel.send(f'sayonara nigga{member.mention}')
    
@bot.command()
async def meme(ctx):
    meme_url = 'https://cdn.discordapp.com/attachments/479963532000231424/1145732113186963559/369602742_2014977578862842_7572931396998453032_n.png'
    meme_url1 = 'https://cdn.discordapp.com/attachments/479963532000231424/1145606446113890386/FB_IMG_1693140085199.png'
    await ctx.send(meme_url1) 

@bot.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        await ctx.send("I am here desu")
    else:
        await ctx.send("you are not in voice channel desu , you must be connect to a voice channel to run this command desu")

@bot.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel desu")
    else:
        await ctx.send("i am not in the voice channel desu")
        
@bot.slash_command()
async def play(ctx, arg):
    channel =  ctx.message.author.voice.channel
    voice = await channel.connect()
    voice = ctx.guild.voice_client
    song = arg + '.mp3'
    source = FFmpegPCMAudio(song)
    player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))
    await ctx.send("Song is playing desu")

@bot.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)   
    if voice and voice.is_playing():
        voice.pause()
        await ctx.send("song is paused desu!")
    else:
        await ctx.send("there is no Audio playing u dum dum baka!")

@bot.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)   
    if voice and voice.is_paused():
        voice.resume()
        await ctx.send("Resumed playback song desu!")
    else:
        await ctx.send("At the moment there is no song desu!")

    
@bot.command(pass_context = True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client
    song = arg + '.mp3'
    
    try:
        source =FFmpegPCMAudio(song)
    except Exception as e:
        await ctx.send(f" failed to load song: {e}")
    
    guild_id = ctx.message.guild.id

    if guild_id in queues:
        queues[guild_id].append(source)
    else:
        queues[guild_id] = [source]
        
    await ctx.send(f"Added {song} to queue desu!")
        
@bot.command(pass_context = True)
async def stop(ctx):   
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




















bot.run(data["bot_token"])