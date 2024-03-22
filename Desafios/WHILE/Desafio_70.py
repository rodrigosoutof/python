total = 0
con_mil = 0
con_bar = 0
nome_bar = ''
preco02 = 0

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    total += preco

    if preco >= 1000.00:
        con_mil += 1

    if con_bar == 0 or preco < preco02:
        con_bar += 1
        preco02 = preco
        nome_bar = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('\nDeseja continuar? [S/N] ').upper() .strip()

    if continuar == 'N':
        break

print('~'*40)
print(f'O total gasto na compra é de: {total:.2f}')
print(f'{con_mil} produtos custão mais de R$1000.00')
print(f'O nome do produto mais barato é: {nome_bar}')
print('~'*40)