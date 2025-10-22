import random

def jogar():
    print('---> Jogo da adivinhação <--- \n Você achou uma mala cheia de dinheiro. Porém a mala está com um cadeado. Para abrir o cadeado e conseguir pegar o dinheiro, você precisa descobrir a senha.')
    numerosecreto = random.randint(1,100)
    tentativas = 5
    
    while tentativas > 0:
        chute = int(input(f'Adivinhe o número secreto que está entre 1 e 100 (Restam {tentativas} tentativas): '))
        if chute == numerosecreto:
            print(f'Parabéns! Você acertou. O número secreto é {numerosecreto}')
            return
        elif chute < numerosecreto:
            print('Você chutou baixo. Tente novamente.')
        else:
            print('Você chutou alto. Tente novamente.')
        tentativas -= 1
    print(f'Xiii.. Fim de jogo. O número secreto era {numerosecreto}')
