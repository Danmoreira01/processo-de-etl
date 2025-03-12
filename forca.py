import random

# Lista de palavras para o jogo
palavras = ["FENNEC", "OCTANE", "DOMINUS", "ROCKETLEAGUE", "MERC"]

def escolher_palavra():
    return random.choice(palavras)

def mostrar_forca(tentativas):
    estagios = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """
    ]
    return estagios[tentativas]

def jogo_forca():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_erradas = []

    print("Bem-vindo ao jogo de forca!")
    print(mostrar_forca(tentativas))
    print(" ".join(palavra_oculta))

    while tentativas < len(mostrar_forca(0)) - 1:
        letra = input("Adivinhe uma letra: ").lower()

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            if letra not in letras_erradas:
                letras_erradas.append(letra)
                tentativas += 1

        print(mostrar_forca(tentativas))
        print(" ".join(palavra_oculta))
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        if "_" not in palavra_oculta:
            print("Parabéns! Você venceu!")
            break
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

if __name__ == "__main__":
    jogo_forca()
