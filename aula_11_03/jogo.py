import random
numero_secreto= random.randint(1,10)
tentativas = 0
max_tentativas = 3

print ("seja bem vindo ao jogo , descubra o numero secreto") 

while tentativas < max_tentativas:

    palpite= int(input("Digite seu número de palpite:"))  
    tentativas += 1

    if palpite == numero_secreto:
        print("voce acertou!")

    elif palpite > numero_secreto:
        print("Você errou!, O Número secreto é menor.")

    else:
        print("Você errou!, O Número secreto é maior.")
