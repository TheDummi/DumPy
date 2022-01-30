import discord
import datetime
import traceback
from discord.ext import commands
client = commands.Bot(command_prefix=commands.when_mentioned_or(
    'py!'), case_insensitive=True)

token = "OTM3NDE5NjQ5MTI0MDMyNTEy.YfbeFA.OxSGgasHqyA2JTXDFGcy9v6OGNI"


@client.event
async def on_ready():
    print(f'I am online! {client.user.name}')


try:
    client.load_extension("cogs.moderation")
    client.load_extension("jishaku")
except:
    print("Failed to load moderation:")
    traceback.print_exc()

client.run(token)
