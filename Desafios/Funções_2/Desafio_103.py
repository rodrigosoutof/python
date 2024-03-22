def ficha(jogador='<desconhecido>', gol=0):
    print(f'Jogador: {jogador} fez {gol} gol(s) na partida')


n = str(input('Digite o nome do jogador: '))
g = str(input('Digite quantos gols marcou: ')) # utilizando str devido ao erro quando utilizamos o int
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
