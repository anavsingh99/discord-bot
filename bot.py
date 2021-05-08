import discord
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

# Credentials
load_dotenv('.env')
api_token = os.getenv('API_TOKEN')

#Helper functions
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is Certain.', 
                'It is decidedly so',
                'Without a doubt.',
                'Yes definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

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