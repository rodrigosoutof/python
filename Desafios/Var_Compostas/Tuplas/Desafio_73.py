times = ('Brasil', 'Argentina', 'Colombia', 'Peru', 'Chile', 'Venezuela', 'Paraguai',
         'Bolivia', 'México', 'Panamá', 'Canadá', 'Alasca', 'China', 'Japão', 'França',
         'Grécia', 'Portugal', 'Itália', 'Alemanha', 'Suiça')
escolha = ' '

print('\nOs 5 primeiros times foram: ')
for p in range(5):
    print(f'{p+1}ª - {times[p]}')
    p += 1

print('\nOs últimos 4 times foram: ')
for u in range(4):
    print(f'{u+17}ª - {times[u+16]}')
    u += 1
print('\nOs times na ordem alfabética: ')
print(sorted(times))

#escolha = input('\nDigite o time para saber em que posição ficou: ')
#for cont in range(len(times)):
#    if escolha == times[cont]:
#        print(f'{escolha} ficou em {cont + 1}ª posição.')

print('-'*60)
print('Resolução Guanabara')
print('-'*60)
print(f'\nOs 5 primeiros são {times[:5]} ')
print(f'Os 4 utlimos são {times[-4:]}')
print(f'A Chile ficou na {times.index("Chile")+1}ª posição')


