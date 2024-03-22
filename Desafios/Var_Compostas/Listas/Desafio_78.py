num = []
cont = maior = menor = 0

for n in range(0, 5):
    num.append(int(input(f'Digite um número inteiro da posição {n}: ')))

for p, n in enumerate(num):
    if p == 0 or n > maior:
        maior = n
    if p == 0 or n < menor:
        menor = n

print(f'O maior número é {maior} e está na posição ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor número é {menor} e está na posição ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')