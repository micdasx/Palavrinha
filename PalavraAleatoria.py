# aqui será gerada a apalavra do dia, achar uma forma de fazer o contador e quando for meia noite rodar esse código

# a classe agora guarda nela mesmo a wordList e consegue gerar uma palavra aleatória
# o bom de uma implementação assim é evitar ao máximo ficar fazendo leituras de arquivos repetidamente
import random 

class PalavraAleatoria:

    def __init__(self):
        self.wordList = []

    def geraListaDePalavras(self, arq):  
        with open(arq, "r", encoding="UTF-8") as file: 
            self.wordList = file.read().splitlines()
        return self.wordList

    def geraPalavra(self):
        return random.choice(self.wordList)