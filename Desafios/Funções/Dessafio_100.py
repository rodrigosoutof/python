from random import randint
# quando coloco um valor aqui em cima significa que declarei uma variável global


def sorteio(lista):
    for n in range(0, 5):
        num = randint(0, 100)
        lista.append(num)
    print('Os números sorteados foram: ', end='')
    for c in lista:
        print(c, end=' ')
    print()


def somapar(lista):
    par = 0
    for i, n in enumerate(lista):
        if n % 2 == 0:
            par += n
    print(f'A soma dos números pares é: {par}')


numbers = list()

print('Bem vindo ao programa!\n')
sorteio(numbers) # passangem de parametro, sem definir uma variavel global.
somapar(numbers)




