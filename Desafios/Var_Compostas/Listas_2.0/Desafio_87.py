matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = num = terceira = segunda = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite o valor da posição [{linha},{coluna}]: '))
        matriz[linha][coluna] = num

        if num % 2 == 0:
            par += num

        if coluna == 2:
            terceira += num

        if linha == 1 and coluna == 0:
            segunda = num
        elif linha == 1 and num >= segunda:
            segunda = num

print('=-' * 20)
print('-- MATRIZ --')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'\n A somatória dos números pares são: {par}')
print(f'\n A somatória dos números da terceira coluna é: {terceira}')
print(f'\n O maior número da segunda linha é {segunda}')
print()
print('=-' * 20)
