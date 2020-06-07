import discord
import requests
import json
import os

# create discord client
client = discord.Client()

@client.event
async def on_ready():

print("Bot is ready")

client.run(os.environ['token'])
