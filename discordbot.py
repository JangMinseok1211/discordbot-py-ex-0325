from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
      import asyncio
if "집합" in message.content:
    await message.delete()
    await message.channel.send(f"{message.author.mention} 님이 집합 시킵니다. @everyone")
    
if "ㅈㅎ" in message.content:
    await message.delete()
    await message.channel.send(f"{message.author.mention} 님이 집합 시킵니다. @everyone")
    
if "wg" in message.content:
    await message.delete()
    await message.channel.send(f"{message.author.mention} 님이 집합 시킵니다. @everyone")
    
if "wlqgkq" in message.content:
    await message.delete()
    await message.channel.send(f"{message.author.mention} 님이 집합 시킵니다. @everyone")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
