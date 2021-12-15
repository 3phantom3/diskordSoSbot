import discord
import os
import calc
import sqlite3
import datetime

my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is redy')
    global basa, cur
    basa = sqlite3.connect('my.db')
    cur = basa.cursor()
    if basa:
      print('Database connect!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.split()

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')
    if message.content.startswith('$help'):
      await message.channel.send('function "$calc 100 1M 100 1H" -- enter after 1 spase /n\
        function "$conf 15-12-2021 15:00" -- set trap time')
    if message.content.startswith('$calc'):
      await message.channel.send(calc.calc(msg))
    if message.content.startswitch('$conf'):
      cur.execute ("""CREATE TABLE IF NOT EXISTS servertimetrap(channelid INTEGER PRIMARY KEY, time DATETIME);""")
      basa.commit()
      time_input = datetime.datetime.strptime(message.content,'%d-%m-%Y %H:%M')
      try:
        cur.execute("""INSERT INTO servertimetrap VALUES(?,?)""", (message.channel, time_input))
        basa.commit()
      except sqlite3.IntegrityError:
        cur.execute("""UPDATE  servertimetrap SET time = ? WHERE channelid = ?""", (time_input, message.channel))
        basa.commit()

async def background_task():
      base1 = cur.execute("""SELECT * FROM servertimetrap""")
      for i in base1:
        timesave = datetime.datetime.strptime(i[1], '%d-%m-%Y %H:%M')
        delta = datetime.datetime.utcnow() - timesave
        if delta == datetime.timedelta(hours=1):
          await i[0].send('''```🗓NOTIFICATION: 
Trap is in 1 hour.``` @everyone''')
        elif delta == datetime.timedelta(minutes=15):
          await i[0].send('''```🗓NOTIFICATION: 
Trap is in 15 minutes.``` @everyone''')
        elif delta == datetime.timedelta(minutes=5):
          await i[0].send('''```🗓NOTIFICATION: 
Trap is in 5 minutes. Recall all your troops``` @everyone''')
        elif delta == 0:
          await i[0].send('''```🗓NOTIFICATION: 
It's Trap Time!``` @everyone''')
          timesave += datetime.timedelta(days=2)
          cur.execute("""UPDATE  servertimetrap SET time = ? WHERE channelid = ?""", (timesave, i[0]))
          basa.commit()

client.loop.create_task(background_task())
client.run(my_secret)