import discord  # pip install discord.py
from dotenv import load_dotenv
import os
from discord.ext import commands
import random

help_command = commands.DefaultHelpCommand(no_category = 'General')

client = commands.Bot(command_prefix='.',
        help_command = help_command) 

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def load(ctx, extension):
    await ctx.send(f'Loading cogs.{extension}...')
    client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
    await ctx.send(f'Unloading cogs.{extension}...')
    client.unload_extension(f'cogs.{extension}')
@client.command()
async def reload(ctx, extension):
    await ctx.send(f'Unloading cogs.{extension}...')
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Loading cogs.{extension}...')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def latency(ctx):
    await ctx.send(f'{round(client.latency * 1000)} ms')

# Credentials
load_dotenv('.env')

client.run(os.getenv('DISCORD_TOKEN')) 