escolha = 0
c = 0
v = 0
n1 = 0
n2 = 0

print('\nCalculadora 1.0')

while c == 0:
    if v == 0 or escolha == 4:
        n1 = float(input('\nDigite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        v = 1
        escolha = 0

    elif v == 1:
        escolha = int(input('\nEscolha a função que deseja\n'
                            '1 - SOMA\n'
                            '2 - MULTIPLICAÇÃO\n'
                            '3 - MAIOR\n'
                            '4 - TROCAR VALORES\n'
                            '5 - FINALIZAR PROGRAMA\n'
                            'ESCOLHA: '))
        print(' ')

    if escolha == 1:
        total = n1 + n2
        print(f'{n1} + {n2} = {total}')

    elif escolha == 2:
        total = n1 * n2
        print(f'{n1} x {n2} = {total}')

    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}!')
        else:
            print(f'{n2} é maior que {n1}!')
    elif escolha == 5:
        c = 1
print('Obrigado por utilizar minha calculadora! \n'
      'Volte sempre!!!')











