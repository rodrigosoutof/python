import random

nom1 = input('Digite o primeiro nome: ')
nom2 = input('Digite o segundo nome: ')
nom3 = input('Digite o terceiro nome: ')
nom4 = input('Digite o quarto nome: ')

print(f'O nome sorteado para apagar o quadro é: {random.choice([nom1, nom2, nom3, nom4])}')

variaveis = [nom1, nom2, nom3, nom4]
print('\n Agora vamos mostrar a ordem de apresentação dos trabalhos.')
print(f'A ordem de apresentação é:{random.sample(variaveis, len(variaveis))}\n')
