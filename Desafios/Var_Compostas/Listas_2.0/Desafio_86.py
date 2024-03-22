matriz = [[], [], []]
num = 0
for n in range(0, 9):
    num = int(input('Digite um número para: '))
    if n <= 2:
        matriz[0].append(num)
    elif 5 >= n >= 2:
        matriz[1].append(num)
    else:
        matriz[2].append(num)

print()
print(matriz[0])
print(matriz[1])
print(matriz[2])

for c in range(len(matriz[0])):
    print(f'[{matriz[0][c]}]', end=' ')
print()
for c in range(len(matriz[1])):
    print(f'[{matriz[1][c]}]', end=' ')
print()
for c in range(len(matriz[2])):
    print(f'[{matriz[2][c]}]', end=' ')


