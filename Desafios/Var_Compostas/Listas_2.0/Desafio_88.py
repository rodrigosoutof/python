import random
jogos = list()

print('-=' * 20)
qtd = int(input('Digite quantos jogos quer gerar: '))

for j in range(0, qtd):
    teste = list()
    contador = 0
    while True:
        num = random.randrange(1, 60)
        if num not in teste:
            teste.append(num)
            contador += 1

        if contador == 6:
            break
    teste.sort()
    jogos.append(teste[:])

print('-='*3, f'Sorteio de {qtd} jogos', '-='* 3)
print()
for j in range(0, qtd):
    print(f'O {j +1}ª jogo é {jogos[j]}')
print('-=' * 20)

