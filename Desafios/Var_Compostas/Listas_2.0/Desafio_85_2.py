numeros = [[], []]
num = 0

for n in range(0, 7):
    num = int(input(f'Digite o {n + 1} número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[1].sort()
numeros[0].sort()
print('=-' * 30)
print(f'Os números pares digitados foram: ´{numeros[0]}')
print(f'Os números impares digitados foram: ´{numeros[1]}')
print('=-' * 30)
