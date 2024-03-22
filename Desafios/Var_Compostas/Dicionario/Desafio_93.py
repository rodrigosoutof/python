aproveitamento = dict()
jogos = list()

# 1 - Nome do jogador e quantas partidas ele jogou
aproveitamento['Nome'] = str(input('Digite o nome do jogador: '))
aproveitamento['Partidas'] = int(input('Quantas partidas ele jogou: '))
print()

# 2 - Quantidade de gol em cada partida (lista)
for c in range(0, aproveitamento['Partidas']):
    gol = int(input(f'Quantos gols foram feitos na {c + 1}ª partida: '))
    jogos.append(gol)

aproveitamento['Gols'] = jogos

print('-='*20)
print()

print(f'O jogador {aproveitamento["Nome"]}')
print(f'Participou de {aproveitamento["Partidas"]}')
for i, v in enumerate(aproveitamento['Gols']):
    print(f'Gols na {i + 1}ª partida: {v}')

print()
print('-='*20)
