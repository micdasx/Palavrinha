import discord
import json
import PalavraAleatoria as gerador

with open("configuracoes.config", "r") as jsonfile:
    configFile = json.load(jsonfile)

client = discord.Client()

#gera palavra aleatória
palavra = gerador.geraPalavra("palavras.txt")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(message.content)
    
    msg = message.content.split(" ", 5)
    if msg[0].const or msg[1] or msg[2] or msg[3] or msg[4] in palavra:
        messageSend = await message.channel.send("ta no caminho cara")

client.run(configFile["TOKEN"])