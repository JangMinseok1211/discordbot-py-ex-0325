from cmath import log
from distutils.sysconfig import PREFIX
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix='!')

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

# 그룹 과 그룹에 속한 사람들을 저장할 딕셔너리
group_dict = {}


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == f'call':
        await message.channel.send("callback!")
    if message.content.startswith('!help'):
        await message.channel.send(f"!그룹 '그룹명' '@사용자1' '@사용자2' ... - '그룹명으로 사용자를 추가하여 생성합니다 \n !호출 '그룹명' - 그룹에 포함된 사용자를 호출 합니다. \n !삭제 '그룹명' 그룹을 삭제합니다")

    if message.content.startswith('집합') or message.content.startswith('ㅈㅎ') or message.content.startswith(
            'wlqgkq') or message.content.startswith('wg'):
        user_name = str(message.author)
        await message.delete()
        await message.channel.send(f'{user_name[:-5]} 님이 집합 시킵니다. @everyone')

    # 메시지가 !그룹으로 시작하면 새로운 그룹을 추가
    if message.content.startswith('!그룹'):
        # 메시지에서 그룹명과 사용자 이름들 추출
        group_name, *people = message.content.split()[1:]

        # 그룹명을 키로, 사용자 이름들을 값으로 하는 딕셔너리 추가
        group_dict[group_name] = people

        await message.channel.send(f"{group_name} 그룹이 추가되었습니다.")

    # 메시지가 !mention으로 시작하면 해당 그룹에 속한 사용자들을 멘션
    if message.content.startswith('!호출'):
        # 메시지에서 그룹명 추출
        group_name = message.content.split()[1]

        # 그룹명에 해당하는 사용자 이름들 추출
        if group_name in group_dict:
            people = group_dict[group_name]

            # 사용자 이름들을 멘션하여 메시지 보내기
            mention_str = ' '.join([f'<{p}>' for p in people])
            await message.channel.send(f"{group_name} 그룹의 멤버: {mention_str}")
        else:
            await message.channel.send(f"{group_name} 그룹을 찾을 수 없습니다.")

    if message.content.startswith('!삭제'):
        group_name = message.content.split()[1]
        if group_name.lower() not in group_dict:
            await message.channel.send(f"{group_name} 그룹이 존재하지 않습니다.")
            return

        # 그룹에서 멘션할 사용자 목록 가져오기
        mention_list = [f"<{user}>" for user in group_dict[group_name.lower()]]

        # 그룹 삭제
        del group_dict[group_name.lower()]

        # 멘션할 사용자가 있을 경우, 메시지 보내기
        if mention_list:
            await message.channel.send(f"{group_name} 그룹에서 {', '.join(mention_list)}를 삭제했습니다.")
        else:
            await message.channel.send(f"{group_name} 그룹을 삭제했습니다.")

   


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
