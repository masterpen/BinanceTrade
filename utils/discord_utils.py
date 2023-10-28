import discord
from config import discord_config

client = discord.Client()

async def send_message(message):
    channel = client.get_channel(int(discord_config.CHANNEL_ID))
    await channel.send(message)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

