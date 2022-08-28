from discord.ext import commands
from os import getenv
import traceback
import discord


import asyncio
bot = commands.Bot(command_prefix='.')

@bot.listen('on_message')
async def paimon(message):
    print(message.content)
    if message.content == '.シャンハイ':
        await message.channel.send('<:emoji_22:990543009735127090> <:emoji_36:992655220188381226> <:emoji_35:992655130342207488>')

    if message.content == '.チー':
        await message.channel.send('キレそう')

    if message.content == '.チー牛':
        await message.channel.send('<:emoji_13:990229855067054101> <:emoji_10:990229561918754816> <:emoji_11:990229695301820427> <:emoji_12:990229756643540992>')

    if message.content == '.からしな1':
        await message.channel.send('朝だーーーーーーーーーーーー！！！！！プロジェクト炎上、睡眠時間は返上、生活リズムは無事変調、胃酸が逆上、食道に炎症、太田胃酸を飲みましょう　ねます')

    if message.content == '.からしな2':
        await message.channel.send('ふとんがwwwふっとんだwwwwwwww')

    if message.content == '.眠井':
        await message.channel.send('チー牛殺す')


presence = discord.Game("Apex Legends")  # プレイ中


@bot.event
async def on_ready():
    await bot.change_presence(activity=presence)


# チャンネル入退室時の通知処理
@bot.event
async def on_voice_state_update(member, before, after):
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = bot.get_channel(873950453866582077)

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds0 = [873947334059380808]

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds1 = [1012932369822515310]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds0:
            await botRoom.send("<#" + str(before.channel.id) + "> から" + member.name + "  が抜けました")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds0:
            await botRoom.send("<#" + str(after.channel.id) + "> に" + member.name + "  が参加しました")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds1:
            await botRoom.send(member.name + "が" + "シベリア送りになりました")


# Botのトークンを指定
token = getenv('DISCORD_BOT_TOKEN')
bot.run('OTAyNDgxMjk5NTI3MzE1NDU3.YXfDNQ.9HOLDFB-B5wJFmlbt6ysh15VgjE')
