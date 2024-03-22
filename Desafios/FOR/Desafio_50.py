total = 0

for cont in range(1, 7):
    num = int(input(f'Digite {cont}º número inteiro: '))
    ver = num % 2

    if ver == 0:
        total = num + total

print(f'\nA soma dos números pares é: {total}')


