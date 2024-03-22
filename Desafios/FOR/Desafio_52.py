n1 = int(input('Digite um número inteiro: '))
total = 0
for cont in range(1, n1 + 1):
    if n1 % cont == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{cont}', end=' ')
print(f'\n\033[mO número {n1} foi divisível {total} vezes ')

if total == 2:
    print('E por isso ele é um número primo')
else:
    print('E por isso ele não é um número primo')