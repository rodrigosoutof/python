from time import sleep
numbers = list()


def maior(lista):
    for i, p in enumerate(lista):
        print(f'Na posição {i+1} foi digitado o número {p}')
        if i == 0:
            m = p
        elif p >= m:
            m = p

    print(f'\nO maior número digitado é {m}')


print('+'*50)
print('Bem vindo ao meu programa!')
print('Vamos verificar qual é o maior número digitado.')
print('+'*50)

while True:
    num = int(input('Digite um número inteiro: '))
    numbers.append(num)
    print()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar?[S/N] ')).upper().strip()
        print('+' * 50)
    if cont == 'N':
        print('Obrigado por usar nosso programa!\n'
              'Em instantes seu resultado será exibido na tela...')
        print('+' * 50)
        sleep(2)
        break

maior(numbers)
print('+'*50)
