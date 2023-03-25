from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

#그룹 과 그룹에 속한 사람들을 저장할 딕셔너리
group_dict={}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == f'call':
        await message.channel.send("callback!")

    if message.content.startswith('집합') or message.content.startswith('ㅈㅎ') or message.content.startswith(
            'wlqgkq') or message.content.startswith('wg'):
        user_name = str(message.author)
        await message.delete()
        await message.channel.send(f'{user_name[:-5]} 님이 집합 시킵니다. @everyone')
    #그룹 을 치면 새로운 그룹 추가
    if message.content.startswith('그룹'):
        #메시지에서 그룹명과 사용자 이름들 추출
        group_name, *people = message.content.split()[1:]
        #그룹몀을 키로, 사용자 이름들을 값으로 하는 딕셔너리 추가
        group_dict[group_name]=people
        await  message.channer.send(f"{group_name} 그룹이 추가되었습니다.")
        
    #메시지가 !호출 로 시작하면 해당 그룹에 속한 사용자들 멘션
    if message.content.startswith('!호출'):
        #메세지에서 그룹명 추출
        group_name = message.content.split()[1]
        
        #그룹명에 해당하는 사용자 이름들 추출
        if group_name in group_dict:
            people = group_dict[group_name]
            
            #사용자 이름들을 멘션하여 메세지 보내기
            mention_str = ' '.join([f'<@!{p}' for p in people])
            await  message.channel.send(f'{group_name} 그룹의 멤버: {mention_str}')
        else:
            await message.channel.send(f'{group_name} 그룹을 찾을 수 없습니다.')

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
