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

    str_cities = "Adak, Anchorage, Boise, Chicago, Denver, Detroit, Juneau, Los_Angeles, Menominee, Metlakatla, New_York, Nome, Phoenix, Sitka, Yakutat"
    @commands.command(aliases=['timeinAmerica'], help="gives the local time in the following US cities: " + str_cities)
    async def UStime(self, ctx, *, city):
        api_token = os.getenv('API_TOKEN')
        response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=" + api_token + "&format=json&by=zone&zone=America/" + city)
        response_json = response.json()
        output = response_json['formatted']
        await ctx.send(f'The local time in {city.title()} is: {output}')

    str_cities2 = "Kabul, Yerevan, Baku, Bahrain, Dhaka, Thimpu, Brunei, Phnom_Penh, Shanghai, Tblisi, Hong_Kong, Beirut, Macau, Kuala_Lumpur, " 
    str_cities3 = "Kolkata, Jakarta, Jayapura, Makassar, Pontianak, Tehran, Baghdad, Jerusalem, Tokyo, Amman, Almaty, Pyongyang, Seoul, Kuwait, Bishkek, Vientiane, "
    str_cities4 = "Kathmandu, Muscat, Karachi, Gaza, Hebron, Manila, Qatar, Novosibirsk, Riyadh, Singapore, Colombo, Damascus, Taipei, Bangkok, Dubai, Ho_Chi_Minh"
    @commands.command(aliases=['timeinAsia'], help="gives the local time in the following Asian cities: " + str_cities2 + str_cities3 + str_cities4)
    async def Asiatime(self, ctx, *, city):
        api_token = os.getenv('API_TOKEN')
        response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=" + api_token + "&format=json&by=zone&zone=Asia/" + city)
        response_json = response.json()
        output = response_json['formatted']
        await ctx.send(f'The local time in {city.title()} is: {output}')

def setup(client):
    client.add_cog(Time(client))