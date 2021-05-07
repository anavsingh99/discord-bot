import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('ODQwMDM3ODAzMjI4Mzk3NjI4.YJSYKw.clT7pBj98DMPAEXn5FTc3mwtrjY')