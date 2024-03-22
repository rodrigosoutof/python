dist = int(input('Digite a distancia em Km da viagem: '))

if dist <= 200:
    valor = dist * 0.5
    print(f'O valor da sua viagem é {valor :.2f}')
else:
    valor = dist * 0.45
    print(f'O valor da sua viagem é {valor :.2f}')


