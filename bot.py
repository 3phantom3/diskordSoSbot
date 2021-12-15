import discord
import os
import calc
import datetime

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
        msg = ' '.join(message.content.split()[1:])
        time_input = datetime.datetime.strptime(msg,'%d-%m-%Y %H:%M')
        basa[str(message.channel.id)] = time_input
        await message.channel.send(msg)
        await message.channel.send(msg)

# async def background_task():
#     for i in basa:
#         timesave = datetime.datetime.strptime(basa[i], '%d-%m-%Y %H:%M')
#         delta = datetime.datetime.utcnow() - timesave
#         if delta == datetime.timedelta(hours=1):
#             await client.get_channel(int(i)).sendgit ('''```🗓NOTIFICATION:
# Trap is in 1 hour.``` @everyone''')
#         elif delta == datetime.timedelta(minutes=15):
#             await client.get_channel(int(i)).send('''```🗓NOTIFICATION:
# Trap is in 15 minutes.``` @everyone''')
#         elif delta == datetime.timedelta(minutes=5):
#             await client.get_channel(int(i)).send('''```🗓NOTIFICATION:
# Trap is in 5 minutes. Recall all your troops``` @everyone''')
#         elif delta == 0:
#             await client.get_channel(int(i)).send('''```🗓NOTIFICATION:
# It's Trap Time!``` @everyone''')
#             timesave += datetime.timedelta(days=2)
#             basa[i] = timesave
#
# client.loop.create_task(background_task())
client.run(my_secret)