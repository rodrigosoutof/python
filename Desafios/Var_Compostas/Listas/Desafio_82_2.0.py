lista = list()
impar = list()
par = list()

while True:
    conf = ' '
    lista.append(int(input('Digite um número: ')))

    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N] ').upper().strip()
    if conf == 'N':
        break

for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('=-' * 30)
print(f'\nOs valores digitados foram {lista}')
print(f'Os números pares são {par}')
print(f'Os números impares digitados são {impar}')
