@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = (amount + 1))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command.')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify the amount of messages to delete.')

## From Documentation
@client.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

def to_upper(argument):
    return argument.upper()

@client.command()
async def up(ctx, *, content: to_upper):
    await ctx.send(content)

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = (amount + 1))

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

@client.event
async def on_member_join(member):
    print(f'{member} the dumbass has joined a server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has been banished!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    
@client.command(aliases = ['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send (f'Question: {question}\nAnswer: {random.choice(responses)}')