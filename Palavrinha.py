import discord
import json

with open("configuracoes.config", "r") as jsonfile:
    configFile = json.load(jsonfile)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(message.content)

client.run(configFile["TOKEN"])