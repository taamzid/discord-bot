import discord 
import os
import requests
import json
import random
from replit import db 
from keep_alive import keep_alive

client = discord.Client() 

sad_words = ["bhallagena", "vallagena", "mon bhalo na", "mon kharap", "mon valo na", "depressed", "depression", "depression e asi", "depression e achi", "pera lagtese onek"]

bot_solution = [
  "Chill! pera nai.", "biya koro, shob thik hoye jabe.", "prem koro!"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_tambot(bot_messages):
  if "tambot" in db.keys():
    tambot = db["tambot"]
    tambot.append(bot_messages)
    db["tambot"] = tambot
  else:
    db["tambot"] = [bot_messages]

def delete_tambot(index):
  tambot = db["tambot"]
  if len(tambot) > index:
    del tambot[index]
    db["tambot"] = tambot

@client.event
async def on_ready(): 
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('asos?'):
    await message.channel.send('tamzid offline! ashle reply dibe.')

  if message.content.startswith('Kire?'):
    await message.channel.send('tamzid offline! ashle reply dibe.')

  if message.content.startswith('kire?'):
    await message.channel.send('tamzid offline! ashle reply dibe.')

  if message.content.startswith('Kire asos?'):
    await message.channel.send('tamzid offline! ashle reply dibe.')

  if message.content.startswith('kire asos?'):
    await message.channel.send('tamzid offline! ashle reply dibe.')
    
  if message.content.startswith('tamzid?'):
    await message.channel.send('tamzid offline! ashle reply dibe.')


  if message.content.startswith('!quote'):
    quote = get_quote()
    await message.channel.send(quote)

  options = bot_solution
  if "tambot" in db.keys():
    options += db["tambot"]

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(bot_solution))

  if message.content.startswith("!add"):
    bot_messages = message.content.split("!add ",1)[1]
    update_tambot(bot_messages)
    await message.channel.send("New message added.")
  
  if message.content.startswith("!del"):
    tambot = []
    if "tambot" in db.keys():
      index = int(message.content.split("!del",1)[1])
      delete_tambot(index)
      tambot = db["tambot"]
    await message.channel.send(tambot)

  if message.content.startswith("!list"):
    tambot = []
    if "tambot" in db.keys():
      tambot = db["tambot"]
    await message.channel.send(tambot)

keep_alive()
client.run(os.getenv('TOKEN'))


 