print('Bom dia !!!\n'
      'Vamos converter os números.\n')
opc = int(input('Digite 1 para converter para binário\n'
                'Digite 2 para converter para octal\n'
                'Digite 3 para converter para hexadecimal: '))

n1 = int(input('\nDigite um número inteiro: '))

if opc == 1:
    binario = bin(n1)[2:]
    print(f'\nA representação binaria do número {n1} é {binario}')
elif opc == 2:
    octal = oct(n1)[2:]
    print(f'\nA representação octal do número{n1} é {octal}')
elif opc == 3:
    hexa = hex(n1)[2:]
    print(f'\nA representação hexadecimal do número {n1} é {hexa}')
else:
    print('Verifique o número digitado e tente novamente.')
