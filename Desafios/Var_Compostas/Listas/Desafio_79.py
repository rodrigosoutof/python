lista = []

while True:
    num = int(input('\nDigite um número: '))

    if num in lista:
        print('Numero já existe! Tente outro número.')
    else:
        lista.append(num)
        print(lista)

    conf = ' '
    while conf not in 'SN':
        conf = input('\nDeseja continuar?[S/N] ').upper().strip()

    if conf == 'N':
        break

print('-='*30)
print(f'\nOs números digitados foram: {lista}')
lista.sort()
print(f'Os números na ordem crescente: {lista}')
print('FIM!\n')
print('-='*30)

