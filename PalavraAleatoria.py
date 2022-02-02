# aqui será gerada a apalavra do dia, achar uma forma de fazer o contador e quando for meia noite rodar esse código
import random 

class PalavraAleatoria:
    def geraPalavra(arq):  
        with open(arq, "r", encoding="UTF-8") as file: 
            word = list(map(str, file.read().splitlines())) 
            
            print(random.choice(word)) 
        
        return word
