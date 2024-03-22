palavras = ('Rodrigo', 'Elisa', 'Maria', 'Raul', 'Robson', 'Thiago')

for n in palavras:
    print(f'\nA palavra {n} possui as vogais: ', end=' ')
    for p in n:
        if p in 'Aa':
            print(p, end=' ')
        elif p in 'Ee':
            print(p, end=' ')
        elif p in 'Ii':
            print(p, end=' ')
        elif p in 'Oo':
            print(p, end=' ')
        elif p in 'Uu':
            print(p, end=' ')
print(' ')


#Correção
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')