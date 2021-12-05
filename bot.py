import discord
import os
import calc
my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = ' '.join(message.content.split())

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')
    if message.content.startswith('$help'):
      await message.channel.send('function "$calc 100 1M 100 1H" -- enter after 1 spase')
    if message.content.startswith('$calc'):
      await message.channel.send(calc.calc(msg))

client.run(my_secret)