import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import random

client = commands.Bot(command_prefix='.')  # create an instance of a bot, decorater, event

@client.event
async def on_ready(): # when the bot is ready - ready state, know that things are working
    print('Bot is ready.')

# Credentials
load_dotenv('.env')

client.run(os.getenv('TOKEN'))  # webhook, running the bot using token