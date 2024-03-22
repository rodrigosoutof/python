pessoas = list()
dados = list()
maior_p = list()
menor_p = list()
c = 0

while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    c += 1
    conf = ' '
    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N] ').upper().strip()
    if conf == 'N':
        break

for p in pessoas:
    if p[1] >= 70:
        maior_p.append(p)
    else:
        menor_p.append(p)

print('~' * 30)
print(f'\nForam cadastradas {c} pessoas.')
print(' ')
print('As pessoas mais pesadas cadastradas foram:')
for p in maior_p:
    print(f'{p[0]} com {p[1]}Kg')
print(' ')
print('As pessoas menos pesadas cadastradas foram:')
for p in menor_p:
    print(f'{p[0]} com {p[1]}Kg')
print('')
print('~' * 30)

# Correção
pes = list()
dad = list()
mai = men = c = 0

while True:
    dad.append(str(input('Digite o nome: ')))
    dad.append(int(input('Digite o peso: ')))

    if len(pes) == 0:
        mai = men = dad[1]
    else:
        if dad[1] > mai:
            mai = dad[1]
        if dad[1] < men:
            men = dad[1]

    pes.append(dad[:])
    dad.clear()

    conf = ' '
    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N] ').upper().strip()
    if conf == 'N':
        break

print('~' * 30)
print(f'\nForam cadastradas {len(pes)} pessoas.')
print(' ')
print(f'O maior peso foi de {mai}Kg, Peso de ', end='')
for p in pes:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print(' ')
print(f'O menor peso foi de {men}Kg, Peso de ', end='')
for p in pes:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print('')
print('~' * 30)


