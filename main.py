import discord
import os
import datetime
import pytz
from keep_alive import keep_alive
tz = 'UTC'
prefix = "date."
client = discord.Client()
ver = "Date/Time Bot v. 1.3.4"
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
  global prefix
  global tz
  now_est = datetime.datetime.now(pytz.timezone(tz))
  if message.author != client.user:
    if message.content.startswith(prefix + "version"):
      await client.send_message(message.channel, "This is " + ver + ".")
    if message.content.startswith(prefix + "time"):
      await client.send_message(message.channel, "<@" + message.author.id + ">, it is `" + now_est.strftime("%I:%M:%S %p %Z") + "` right now.")
    if message.content.startswith(prefix + "setPre") and message.content[len(prefix) + 7:] != "":
      print(message.content[len(prefix) + 7:])
      if (ord(message.content[-1:]) > 64 and ord(message.content[-1:]) < 91) or (ord(message.content[-1:]) > 47 and ord(message.content[-1:]) < 58):
        print('yee')
        prefix = message.content[len(prefix) + 7:] + " "
      else:
        prefix = message.content[len(prefix) + 7:]
      await client.send_message(message.channel, "Prefix is now " + prefix)
    if message.content.startswith(prefix + "setTZ") and message.content[len(prefix) + 6:] != "":
      tz = message.content[len(prefix) + 6:] 
      await client.send_message(message.channel, "Time zone is now " + tz)
    if message.content.startswith(prefix + "help"):
      await client.send_message(message.channel, "All commands start with " + prefix + ".\n**help**: Shows this page.\n**time**: Shows time in " + tz + ".\n**date**: Shows date.\n**now**: Shows date and time in " + tz + ".\n**setPre**: Sets Prefix.\n**setTZ**: Sets Time Zone.\n**version**: Version of bot\n")
    elif message.content.startswith(prefix + "date"):
      await client.send_message(message.channel, "<@" + message.author.id + ">, Today is `" + now_est.strftime("%A %B %d, %Y") + "`.")
    elif message.content.startswith(prefix + "now"):
      await client.send_message(message.channel, "<@" + message.author.id + ">, it is `" + now_est.strftime("%A %B %d, %Y, %I:%M:%S %p %Z") + "` right now.")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
