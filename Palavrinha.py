import discord
import json
import PalavraAleatoria as gerador

with open("configuracoes.config", "r") as jsonfile:
    configFile = json.load(jsonfile)

client = discord.Client()

# gera palavra aleatória
ger = gerador.PalavraAleatoria()
palavras = ger.geraListaDePalavras("palavras.txt")
palavra = ger.geraPalavra()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'ah palavra é {palavra}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)
    
    msg = message.content.split(" ", 5)

    # palavra não existe
    if message.content not in palavras:
        messageSend = await message.channel.send("palavra nao existe")
    # acertou alguma das letras, precisa de correção
    elif msg in palavra.split(' '):
        messageSend = await message.channel.send("ta no caminho cara")
    # acertou a palavra
    elif message.content == palavra:
        messageSend = await message.channel.send("acertou a palavra")
    # palavra existe mas não acertou nenhuma letra
    else:
        messageSend = await message.channel.send("ta foda hein")

client.run(configFile["TOKEN"])