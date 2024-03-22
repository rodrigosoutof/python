import random

conf = 'S'
cont = 1

while conf == 'S':
    num = random.randrange(0, 10)
    tent = int(input('Digite qual número a maquina escolhera: '))

    print(f'A escolha da maquina foi... \n{num}')

    if tent == num:
        conf = 'N'
    else:
        print('\nVocê ERROU, a escolha da maquina foi {} e a sua foi {}\n'.format(num, tent))
        cont += 1

print('\nVocê ACERTOU, a escolha da maquina foi {} e a sua foi {}\n'
      'Você chutou {} vezes para acertar'.format(num, tent, cont))

