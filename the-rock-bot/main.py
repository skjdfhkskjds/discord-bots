import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
from grab_images import new_image
from replit import db
from keep_alive import keep_alive

load_dotenv()
token = os.environ.get('TOKEN')

bot = commands.Bot(command_prefix='')

def load_images():
    return os.listdir('rock images/')

def scorePoints(author):
    if author in db.keys():
        int(db[author])
        db[author] = str(int(db[author]) + 1)
    else:
        db[author] = '1'

images = load_images()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = message.content
    
    if "rock" in str(msg.lower()):
        scorePoints(str(message.author))
        image = images[random.randint(0, len(images)-1)]
        random_pic = 'rock images/' + image
        name = image.split('.png')[0]
        with open(random_pic, 'rb') as f:
            picture = discord.File(f)   
            await message.channel.send(file=picture)
        await message.channel.send(f"You've heard of The Rock, let me introduce you to the {name}, instead!")

    else:
        await bot.process_commands(message)

@bot.command(name='$add_image')
async def image(ctx, filename, url):
    output = new_image(filename, url)
    images = load_images()
    await ctx.reply(output)
    
@bot.command(name='$score')
async def score(ctx):
    print(ctx.author)
    await ctx.reply(f"Your score is: {db[str(ctx.author)]}")

@bot.command(name='$help')
async def help__(ctx):
    help_list = ["$help: Returns all of the commands and what they do.",
                  "$add_image: Use in the form $add_image {name} {url} to add an image",
                  "$score: Returns your score! You get points each time you invoke the rock",
                  "$leaderboard: Returns the entire leaderboard",
                  "$inspire: Returns our national anthem to inspire you"]
    msg = '\r\n'.join(help_list)
    await ctx.send(f'```{msg}```')

@bot.command(name='$leaderboard')
async def leaderboard(ctx):
    members = list(db.keys())
    scores = []
    for member in members:
        s = int(db[member])
        print(s)
        scores.append(s)

  # Bubble Sort
    for iter_num in range(len(scores)-1,0,-1):
      for i in range(iter_num):
         if scores[i]<scores[i+1]:
            temp1 = scores[i]
            temp2 = members[i]
            scores[i] = scores[i+1]
            scores[i+1] = temp1
            members[i] = members[i+1]
            members[i+1] = temp2
    
    
    leaderboard_list = [member + ': ' + str(score) for member, score in zip(members, scores)]
    msg = '\r\n'.join(leaderboard_list)
    await ctx.send(f'```{msg}```')

@bot.command(name='$inspire')
async def inspire(ctx):
    lyrics = ["It's about drive, it's about power",
"We stay hungry, we devour",
"Put in the work, put in the hours and take what's ours (ahoo)",
"Black and Samoan in my veins",
"My culture bangin' with Strange",
"I change the game, so what's my motherfuckin' name (Rock!)"]
    msg = '\r\n'.join(lyrics)
    await ctx.send(msg)
    with open('the rock.jpg', 'rb') as f:
            picture = discord.File(f)   
            await ctx.send(file=picture)

keep_alive()
bot.run(token)
