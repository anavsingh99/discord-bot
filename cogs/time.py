import requests
import json
import os
import discord
from discord.ext import commands

class Time(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Time Bot is online.')

    @commands.command(aliases=['timeinAmerica'])
    async def UStime(self, ctx, *, city):
        api_token = os.getenv('API_TOKEN')
        response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=" + api_token + "&format=json&by=zone&zone=America/" + city)
        response_json = response.json()
        output = response_json['formatted']
        await ctx.send(f'The local time in {city.title()} is: {output}')

    @commands.command(aliases=['timeinAsia'])
    async def Asiatime(self, ctx, *, city):
        api_token = os.getenv('API_TOKEN')
        response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=" + api_token + "&format=json&by=zone&zone=Asia/" + city)
        response_json = response.json()
        output = response_json['formatted']
        await ctx.send(f'The local time in {city.title()} is: {output}')

def setup(client):
    client.add_cog(Time(client))