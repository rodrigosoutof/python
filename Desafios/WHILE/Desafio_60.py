n1 = int(input('Digite um número inteiro para ver seu fatorial: '))

aux = n1
f = 1

print(f'Calculando: {n1}! = ', end='')

while aux > 0:
    print(f'{aux}', end='')
    print(' X ' if aux > 1 else ' = ', end='')
    f *= aux
    aux -= 1
    
print(f'{f}')

