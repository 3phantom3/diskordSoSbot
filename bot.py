import discord
import os
import calc
import datetime
import asyncio

my_secret = os.environ['TOKEN']

client = discord.Client()
basa=dict()
@client.event
async def on_ready():
    print('Bot is redy')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.split()

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$help'):
        await message.channel.send('function "$calc 100 1M 100 1H" -- enter after 1 spase \n\
function "$conf 15-12-2021 15:00" -- set trap time')
    if message.content.startswith('$calc'):
        await message.channel.send(calc.calc(msg))
    if message.content.startswith('$conf'):
        time_input = datetime.datetime.strptime(' '.join(message.content.split()[1:]),'%d-%m-%Y %H:%M')
        basa[str(message.channel.id)] = time_input
        await message.channel.send(message.channel.id)
        await message.channel.send(time_input.strftime('%d-%m-%Y %H:%M'))

async def background_task():
    await client.wait_until_ready()
    while True:
        for i in basa:
            time_save = basa[i]
            time_now = datetime.datetime.utcnow
    #         if (time_save.day == time_now.day)and((time_now+datetime.timedelta(hours=1)).hour == time_save.hour)and(time_now.minute== time_save.minute):
    #             await client.get_channel(int(i)).send('''```🗓NOTIFICATION:
    # Trap is in 1 hour.``` @everyone''')
    #         elif (time_save.day == time_now.day)and(time_now == time_save.hour)and((time_now+datetime.timedelta(minutes=15)).minute== time_save.minute):
    #             await client.get_channel(int(i)).send('''```🗓NOTIFICATION:
    # Trap is in 15 minutes.``` @everyone''')
    #         elif (time_save.day == time_now.day)and(time_now == time_save.hour)and((time_now+datetime.timedelta(minutes=5)).minute== time_save.minute):
    #             await client.get_channel(int(i)).send('''```🗓NOTIFICATION:
    # Trap is in 5 minutes. Recall all your troops``` @everyone''')
            if time_now().minute == time_save.minute:
                await client.get_channel(int(i)).send('''```🗓NOTIFICATION:
    It's Trap Time!``` @everyone''')
                time_save += datetime.timedelta(days=2)
                basa[i] = time_save
        await asyncio.sleep(60)
client.loop.create_task(background_task())
client.run(my_secret)