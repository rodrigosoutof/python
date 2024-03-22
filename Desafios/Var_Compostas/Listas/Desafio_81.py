lista = list()

while True:
    conf = ' '
    lista.append(int(input('Digite um número: ')))

    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N] ').upper().strip()
    if conf == 'N':
        break

print(f'\nForam digitados {len(lista)} números')
print(f'Os valores digitados {lista}')
if 5 in lista:
    print(f'O número 5 esta ná {lista.index(5)}ª posição ')
else:
    print('Não foi localizado o valor 5 na lista.')
lista.sort(reverse=True)
print(f'Os valores digitados ordenados decrescente {lista}')

