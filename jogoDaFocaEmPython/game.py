import random
from os import system, name

#função para limpar a tela a cada execução
def limpa_tela():

    #window
    if name == 'nt':
        _= system('cls')
    
    #Mac ou Linux 
    else:  
        _= system('clear')
#Função
def game():
    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'manga', 'laranja','morangos']

    #Escolha rondonicamente uma palavra
    palavra = random.choice(palavras)

    #List comprehension
    letras_descobertas = ['_' for letra in palavra]

    #numero de chances
    chances = 6

    #Lista para as letras erras 
    letras_erradas = []
     
    #Loop enquanto número de chances for maior do que zero
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nchances restantes:", chances)
        print("letras erradas:", " ".join(letras_erradas))
        
        #Tentativas
        tentativas = input("\nDigite uma letra:").lower()
        
        #Condicional
        if tentativas in palavra:
            index = 0
            for  letra in palavra:
                if tentativas == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1    
            letras_erradas.append(tentativas)
        #Condicional
        if '_' not in letras_descobertas:
            print("\nvoce venceu, a palavra era:", palavra)
            break
    if '_' in letras_descobertas:
        print("\nvhjoce perdeu, a palavra era:", palavra)

if __name__ == "__main__":
    game()
    print("\nParabens. Voce está apredendo a programar em python.\n")
        