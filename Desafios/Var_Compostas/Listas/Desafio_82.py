lista = list()
impar = list()
par = list()

while True:
    conf = ' '
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N] ').upper().strip()
    if conf == 'N':
        break

print('=-' *30)
print(f'\nOs valores digitados foram {lista}')
print(f'Os números pares são {par}')
print(f'Os números impares digitados são {impar}')

