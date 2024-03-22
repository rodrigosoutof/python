from random import randint, sample

num1 = randint(1, 100)
num2 = randint(1, 100)
num3 = randint(1, 100)
num4 = randint(1, 100)
num5 = randint(1, 100)

lista = (num1, num2, num3, num4, num5)
ordenada = sorted(lista)
print(f'Os números geradora são: {lista}')
print(f'O menor número é {ordenada[0]}')
print(f'O maior número é {ordenada[-1]}')

#Correção

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('\nOs valores sorteados foram: ', end='')

for c in numeros:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}\n')


a = tuple(sample(range(10), 5))
print(a)
print(f'\nO maior valor é {max(a)} e o menor é {min(a)}.')
