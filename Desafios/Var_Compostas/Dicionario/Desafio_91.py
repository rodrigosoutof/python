from random import randint
from operator import itemgetter
from time import sleep

jogada = dict()
resultado = list()

for i in range(0, 4):
    jogada['jogador'] = i + 1
    jogada['valor'] = randint(1, 6)
    resultado.append(jogada.copy())

print('Resultado dos jogos')
for c in resultado:
    for k, v in c.items():
        print(f'{k}: {v}', end=' ')
    print()

print()
print('CORREÇÃO')

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

print('Resultado dos jogos')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*30)
print()
for i, v in enumerate(ranking):
    print(f'{i+1}ª Lugar: {v[0]} com {v[1]}.')






