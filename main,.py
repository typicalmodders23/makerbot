

import discord
import os
import random
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def nasheed(ctx):
    print("nasheed requested") 
    folder_path = r'isis' 
    files= os.listdir(folder_path)
    random_file = random.choice(files)
    print(f"Selected file: {random_file}")
    await ctx.send(file=discord.File(os.path.join(folder_path, random_file)))

@bot.command()
async def russia(ctx):
    print("russia requested")  
    folder_path= r'z'  
    files = os.listdir(folder_path)
    random_file =random.choice(files)
    print(f"Selected file: {random_file}") 
    await ctx.send(file=discord.File(os.path.join(folder_path, random_file)))



bot.run('')  # replace with your bot token
