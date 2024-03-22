import random

total = 0
vit = 0
continuar = ''
print('\n--- JOGO DO PAR OU IMPAR ---')

while True:

    while True:
        escolha = (input('\nQual é sua escolha [P/I]: ').upper())

        if escolha == 'P' or escolha == 'I':
            num2 = int(input('Escolha um número entre 0 até 10: '))
            num1 = random.randrange(10)
            total = (num1 + num2) % 2

            if escolha == 'P' and total == 0:
                vit += 1
                print(f'Parabéns, {num2} + {num1} = {num1+num2}\n'
                      f'{num1+num2} é Par!')

            elif escolha == 'P' and total == 1:
                print(f'Uma Pena, {num2} + {num1} = {num1+num2}\n'
                      f'{num1+num2} é Impar!')
                break

            elif escolha == 'I' and total == 1:
                vit += 1
                print(f'Parabéns, {num2} + {num1} = {num1+num2}\n'
                      f'{num1+num2} é Ímpar!')

            elif escolha == 'I' and total == 0:
                print(f'Uma Pena, {num2} + {num1} = {num1+num2}\n'
                      f'{num1+num2} é Par!')
                break

        else:
            print('\nValor escolhido não existe, escolha de novo !!!')

    if vit == 0:
        continuar = input(f'\nVocê ganhou {vit} partida(s).\n'
                          f'Quer tentar de novo [S/N]? ').upper()

        if continuar == 'N':
            break

    else:
        continuar = input(f'\nParabéns!!!'
                          f'Você ganhou {vit} partida(s).\n'
                          f'Quer tentar de novo [S/N]? ').upper()

        if continuar == 'N':
            break

localv1 = 'Volte sempre!'

print('~'*30)
print(f'{localv1:^30}')
print('~'*30)