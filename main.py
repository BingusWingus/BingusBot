import discord
from discord.ext import commands
import os
from discord import FFmpegPCMAudio

from dotenv import load_dotenv
load_dotenv() #load enviornment variables frrom .env file

# Set up Discord intents to access all events
intents = discord.Intents.all()    
client = commands.Bot(command_prefix = '!',intents=intents) 



@client.event
async def on_ready(): # when the bot is ready, print the text below
    print("The bot is now ready for use!")
    print("-----------------------------")


#ctx allows you to communicate with discord server
@client.command()
async def hello(ctx): 
    await ctx.send("Hello, I am Bingus Bot :3")


@client.command()
async def daniel(ctx): 
    await ctx.send("Neegus man!")


@client.event #runs when a memeber joins a server
async def on_member_join(member):
    channel_id = int(os.getenv("WELCOME_CHANNEL_ID")) #use int because channel id is integer
    channel = client.get_channel(channel_id)
    await channel.send(f"Welcome to Neegus Central, {member.mention}!")



#Bingus bot will join using join/leave using command 
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('meow.wav')
        player = voice.play(source)


        await ctx.send("I have arrived, Neegus!")
    else:
        await ctx.send("Please join voice channel 3:")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Goodbye, Neegus")
    else:
        await ctx.send("I am not in a voice channel >:(")

#pausing command
@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients , guild = ctx.guild)
    if voice and voice.is_playing():
        voice.pause()
    else:
        await ctx.send("There is no audio playing!")

#resume command
@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients , guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("There is no audio paused!")

#stop command
@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients , guild = ctx.guild)
    voice.stop()

#play command
@client.command(pass_context = True)
async def play(ctx , arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + '.wav')
    player = voice.play(source)


# Get the Discord token from environment variables and run the bot
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)