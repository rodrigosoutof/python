n1 = 0
n2 = 0
cont = 0
print('-'*30)
print('Digite 999 para sair')
print('-'*30)

while cont != 999:
    n1 = int(input('Digite um número para somar: '))

    if n1 != 999:
        total = n1 + n2
        n2 = total
        n1 = 0
        cont += 1

    else:
        cont = 999
print('~'*30)
print(f'A soma dos números digitados é: {total}\n')
print('Fim')


