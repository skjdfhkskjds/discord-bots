import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from stocks import Stock

load_dotenv()
token = os.environ.get('TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command()
async def add_stock(ctx, symbol):
    new_stock = Stock(symbol)
    await ctx.reply("Stock has been added to your portfolio")

