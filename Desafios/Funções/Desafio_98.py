from time import sleep


def contagem():
    n1 = 1
    n2 = 10
    print(('~' * 50))
    print('Contagem crescente de 1 até 10 de 1 em 1:')
    while n1 <= 10:
        print(f'{n1}', end='')
        n1 += 1
        if n1 <= 10:
            print('...', end=' ')
        sleep(0.5)
    print()
    print(('~' * 50))
    print('Contagem decrescente de 10 até 1 de 2 em 2: ')
    while n2 >= 1:
        print(f'{n2}', end='')
        n2 -= 2
        if n2 >= 1:
            print('...', end=' ')
        sleep(0.5)
    print()
    print(('~' * 50))

    print('Agora é sua vez de personalizar a contagem.\n')
    inicio = int(input('Digite um número inteiro para iniciarmos a contagem: '))
    fim = int(input('Digite um número inteiro que sera o fim da contagem: '))
    passo = int(input('Digite um número inteiro que será o passo da contagem: '))
    if passo == 0:
        passo = 1
        print(f'NÚMERO INVALIDO!\n'
              f'Não podemos movimentar de 0 em 0, consideramos o passo como 1.')

    i = inicio
    f = fim
    if passo <= -1:
        passo = passo * (-1)
    print(('~' * 50))

    if inicio < fim and passo > 0:
        print(f'Contagem crescente de {inicio} até {fim} de {passo} em {passo}')
        while i <= fim:
            print(f'{i}', end='')
            i += passo
            if i <= fim:
                print('...', end=' ')
            sleep(0.5)

    elif fim < inicio or passo <= -1:
        print(f'Contagem decrescente de {inicio} até {fim} de {passo} em {passo}')
        while i >= fim:
            print(f'{i}', end='')
            i -= passo
            if i >= fim:
                print('...', end=' ')
            sleep(0.5)
    print()
    print(('~' * 50))


while True:
    contagem()

    conf = ' '
    while conf not in 'SN':
        conf = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if conf == 'N':
        print('Volte Sempre!')
        break
