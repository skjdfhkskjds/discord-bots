import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
token = os.environ.get('TOKEN')

images = os.listdir('rock images/')

client = discord.Client()

@client.event
async def on_message(message):
    if "rock" in str(message.content.lower()):
        random_pic = 'rock images/' + images[random.randint(0, len(images)-1)]
        with open(random_pic, 'rb') as f:
            picture = discord.File(f)   
            await message.channel.send(file=picture)

client.run(token)
