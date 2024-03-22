#valor = prod = 0
#produtos = ('Pneu', 350.00,
#            'Óleo', 45.50,
#            'Transmissão', 143.33,
#            'Banco', 67.70,
#            'Lona de freio', 40.00)

#print('-- Preço dos produtos --\n')
#while prod <= len(produtos):
#    valor += 1
#    print(f'{produtos[prod]}: R${produtos[valor]}')
#    prod += 2
#    valor += 1

#print(' ')

#Correção

estoque = ('Pneu', 350.00,
           'Óleo', 45.50,
           'Transmissão', 143.33,
           'Banco', 67.70,
           'Lona de freio', 40.00,
           'Embreagem', 1168.29)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(0, len(estoque)):
    if pos % 2 == 0:
        print(f'{estoque[pos]:.<30}', end='')
    else:
        print(f'R$ {estoque[pos]:>7.2f}')
print('-'*40)