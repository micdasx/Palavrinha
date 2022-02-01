def cincoLetras(arq):
    with open(arq, "r", encoding="UTF-8") as file:
        print(file.read())
        for palavra in file.read().splitlines():
            print(palavra)
        
        
def main():
    cincoLetras("palavras.txt")
    
if __name__ == "__main__": 
    main()