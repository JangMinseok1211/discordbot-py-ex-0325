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
async def user_message(message):
    if message.author client.user:
        return
    if message.content.startswith(f'집합'):
        await message.channel.delete()
        await message.channel.send('{message.author.mention} 님이 집합 시킵니다. @everyone')
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
