import discord  # pip install discord.py
from dotenv import load_dotenv
import os
from discord.ext import commands
import random
import requests
import json

client = commands.Bot(command_prefix='.')  # create an instance of a bot, decorater, event

@client.event
async def on_ready(): # when the bot is ready - ready state, know that things are working
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

# Credentials
load_dotenv('.env')
api_token = os.getenv('API_TOKEN')

@client.command(aliases=['timeinAmerica'])
async def timezone(ctx, *, city):
    response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=" + api_token + "&format=json&by=zone&zone=America/" + city)
    response_json = response.json()
    output = response_json['formatted']
    await ctx.send(f'The local time in {city} is: {output}')

@client.command(aliases=['timeinAsia'])
async def timezone2(ctx, *, city):
    response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=" + api_token + "&format=json&by=zone&zone=Asia/" + city)
    response_json = response.json()
    output = response_json['formatted']
    await ctx.send(f'The local time in {city} is: {output}')

client.run(os.getenv('DISCORD_TOKEN'))  # webhook, running the bot using token