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
    async def add(self, ctx, num1: float, num2:float):
        num_sum = num1 + num2
        await ctx.send(num_sum)
    
    @commands.command()
    async def subtract(self, ctx, num1: float, num2:float):
        sub = num1 - num2
        await ctx.send(sub)

    @commands.command()
    async def multiply(self, ctx, num1: float, num2:float):
        multi = num1*num2
        await ctx.send(multi)

    @commands.command()
    async def divide(self, ctx, num1: float, num2:float):
        div = num1/num2
        await ctx.send(div)

def setup(client):
    client.add_cog(Math(client))