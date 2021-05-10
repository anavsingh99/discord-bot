import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun Bot is online.')

    @commands.command(help="gives a nice compliment!")
    async def compliment(self, ctx):
        compliments = [ "You look great today!" ,
                        "You have really really nice programming skills." ,
                        "You make an excellent human.",
                        "You’re a true gift to the people in your life.",
                        "You’re amazing!",
                        "You have a remarkable sense of humor.",
                        "You are one of a kind.",
                        "You inspire me to be a better Bot.",
                        "Simply knowing you has made me a better Bot.",
                        "All my Bot friends think you're really cool!"]
        await ctx.send(random.choice(compliments))
    
    @commands.command(aliases=['8ball'], help="gives an 8-ball style answer to any question")
    async def _8ball(self, ctx, *, question: str):
        responses = ['It is Certain.', 
                    'It is decidedly so',
                    'Without a doubt.',
                    'Yes definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Ummm I guess...',
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
    
    @commands.command(help="replies with Pong!")
    async def ping(self, ctx):
        await ctx.send(f'Pong!')

    @commands.command(help="replies with Polo!")
    async def marco(self, ctx):
        await ctx.send(f'Polo!')

def setup(client):
    client.add_cog(Fun(client))