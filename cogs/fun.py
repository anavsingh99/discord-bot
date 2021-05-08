import discord
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun Bot is online.')
    
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
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
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!')

    @commands.command()
    async def marco(self, ctx):
        await ctx.send(f'Polo!')

def setup(client):
    client.add_cog(Fun(client))