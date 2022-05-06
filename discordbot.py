from discord.ext import commands
from os import getenv
import discord

bot = commands.Bot(command_prefix='.')


@bot.listen('on_message')
async def paimon(message):
    print(message.content)
    if message.content == '.非常食':
        await message.channel.send('おいっ！オイラは非常食じゃないぞ！')

    if message.content == '.えへっ':
        await message.channel.send('エヘってなんだよ！')

    if message.content == '.通知':
        await message.channel.send('うるさい。')


presence = discord.Game("非常食")  # プレイ中


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
        announceChannelIds = [873947334059380808]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("<#" + str(before.channel.id) + "> から" + member.name + "  が抜けました")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("<#" + str(after.channel.id) + "> に" + member.name + "  が参加しました")


# Botのトークンを指定
token = getenv('DISCORD_BOT_TOKEN')
bot.run('OTAyNDgxMjk5NTI3MzE1NDU3.YXfDNQ.9HOLDFB-B5wJFmlbt6ysh15VgjE')
