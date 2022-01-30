import discord
import datetime
import traceback
import json
from discord.ext import commands


config = json.load(open('data/config.json'))

client = commands.Bot(command_prefix=commands.when_mentioned_or(
    config['prefix']), case_insensitive=True)


@client.event
async def on_ready():
    print(f'I am online! {client.user.name}')


try:
    client.load_extension("cogs.moderation")
    client.load_extension("jishaku")
except:
    print("Failed to load moderation:")
    traceback.print_exc()

client.run(config['token'])
