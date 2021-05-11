# Bikini Bot-tom

DS3002 Final Project: Anav Singh (as9dw) and Darsh Patel (dp2bkq)

Bikini Bot-tom is a helpful Discord bot that takes in multiple commands which are divided into various categories using cogs. It's name comes from the iconic show "SpongeBob SquarePants" and is a reference to the city where all the characters lived!

Use .help to see the full range of Bikini Bot-tom's commands.

## Setup
```bash
pip install discord.py
pip install python-dotenv
```
Add DISCORD_TOKEN and API_TOKEN to your .env file in the folder. The tokens should be sent to you on Discord by the creators of Bikini Bot-tom.

## General

1) .clear - takes in one argument (int) and clears that many messages from the chat
2) .latency - gives the current latency
3) .load, .unload - enabling/disabling cogs
4) .reload - implementing changes made to a cog

## Math

Using the math commands category, the bot can perform many basic math operations such as:
1) .add - takes in two arguments (floats) and adds them
2) .subtract - takes in two arguments (floats) and subtracts them
3) .multiply - takes in two arguments (floats) and multiplies them
4) .divide - takes in two arguments (floats) and divides the first by the second
5) .raisedto - takes in two arguments (floats) and raises the first to the power of the second

## Fun
The fun commands category has various commands to make you smile :)
1) .8ball - takes in a question and gives an answer like an 8-ball
2) .compliment - gives you a compliment
3) .marco - replies with Polo!
4) .ping - replies with Pong!

## Time
These commands will give the local time in certain cities based on location.
1) .Asiatime - gives the time in Asia for the cities listed under .help Asiatime
2) .UStime - gives the time in the US for the cities listed under .help UStime
