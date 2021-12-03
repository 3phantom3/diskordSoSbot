import discord
import os

client = discord.Client()

def calc(message):
    pass
    #res = message.split(' ')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$calc'):
        await message.channel.send(calk(msg))
client.run(os.getenv('TOKEN'))