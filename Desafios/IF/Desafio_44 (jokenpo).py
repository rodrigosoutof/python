import emoji
import random

papel = emoji.emojize(':hand_with_fingers_splayed:')
tesoura = emoji.emojize(':victory_hand:', )
pedra = emoji.emojize(':raised_fist:')
lista = [pedra, papel, tesoura]

escolha = int(input('Vamos jogar JOKENPO, escolha sua mão e digite\n\n'
                '1 - Para PEDRA\n'
                '2 - Para TESOURA\n'
                '3 - Para PAPEL\n'))

print('\nPrepare-se para o duelo!\n')

var = random.choice(lista)

if escolha == 1 and var == tesoura:
    print(f'{pedra} X {var}\n'
          'VOCÊ GANHOU !!!')
elif escolha == 1 and var == pedra:
    print(f'{pedra} X {var}\n'
          'EMPATOU !!!')
elif escolha == 1 and var == papel:
    print(f'{pedra} X {var}\n'
          'VOCÊ PERDEU !!!')

elif escolha == 2 and var == papel:
    print(f'{tesoura} X {var}\n'
          'VOCÊ GANHOU !!!')
elif escolha == 2 and var == tesoura:
    print(f'{tesoura} X {var}\n'
          'EMPATOU !!!')
elif escolha == 2 and var == pedra:
    print(f'{tesoura} X {var}\n'
          'VOCÊ PERDEU !!!')

elif escolha == 3 and var == pedra:
    print(f'{papel} X {var}\n'
          'VOCÊ GANHOU !!!')
elif escolha == 3 and var == papel:
    print(f'{papel} X {var}\n'
          'EMPATOU !!!')
elif escolha == 3 and var == tesoura:
    print(f'{papel} X {var}\n'
          'VOCÊ PERDEU !!!')
else:
    print('Valor escolhido não encontrado!!!\n'
          'Tente novamente!!!')









