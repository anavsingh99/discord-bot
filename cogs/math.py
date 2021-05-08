import discord
from discord.ext import commands

class Math(commands.Cog):

    def __init__(self,client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Math Bot is online.')

    # Commands
    @commands.command()
    async def add(self,num1: int, num2:int, ctx):
        sum2 = num1 + num2
        await ctx.send(sum2)

def setup(client):
    client.add_cog(Math(client))