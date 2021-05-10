import discord  # pip install discord.py
from dotenv import load_dotenv
import os
from discord.ext import commands
import random

help_command = commands.DefaultHelpCommand(no_category = 'General')

client = commands.Bot(command_prefix='!', help_command=help_command)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(help="loads cogs by name")
async def load(ctx, extension):
    await ctx.send(f'Loading cogs.{extension}...')
    client.load_extension(f'cogs.{extension}')
@client.command(help="unloads cogs by name")
async def unload(ctx, extension):
    await ctx.send(f'Unloading cogs.{extension}...')
    client.unload_extension(f'cogs.{extension}')
@client.command(help="unloads and reloads cogs by name")
async def reload(ctx, extension):
    await ctx.send(f'Unloading cogs.{extension}...')
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Loading cogs.{extension}...')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command(help="sends current latency")
async def latency(ctx):
    await ctx.send(f'{round(client.latency * 1000)} ms')

@client.command(help="clears last x amount of messages")
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = (amount + 1))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command.')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify the amount of messages to delete.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Enter a valid number.")
    else:
        await ctx.send("There was an error.")

# Credentials
load_dotenv('.env')

client.run(os.getenv('DISCORD_TOKEN')) 