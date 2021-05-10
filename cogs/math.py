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
    @commands.command(help="adds two numbers")
    async def add(self, ctx, num1: float, num2:float):
        num_sum = num1 + num2
        await ctx.send(num_sum)

    @add.error
    async def add_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Enter valid numbers!")
        else:
            await ctx.send("There was an error.")
    
    @commands.command(help="subtracts two numbers")
    async def subtract(self, ctx, num1: float, num2:float):
        sub = num1 - num2
        await ctx.send(sub)

    @subtract.error
    async def sub_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Enter valid numbers!")
        else:
            await ctx.send("There was an error.")

    @commands.command(help="multiplies two numbers")
    async def multiply(self, ctx, num1: float, num2:float):
        multi = num1*num2
        await ctx.send(multi)

    @multiply.error
    async def mult_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Enter valid numbers!")
        else:
            await ctx.send("There was an error.")

    @commands.command(help="divides two numbers")
    async def divide(self, ctx, num1: float, num2:float):
        div = num1/num2
        await ctx.send(div)

    @divide.error
    async def div_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Enter valid numbers!")
        else:
            await ctx.send("There was an error.")

    @commands.command(help="raises one number to the power of the other")
    async def raisedto(self, ctx, num1: float, num2:float):
        power = num1**num2
        await ctx.send(power)

    @raisedto.error
    async def raisedto_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Enter valid numbers!")
        else:
            await ctx.send("There was an error.")

def setup(client):
    client.add_cog(Math(client))