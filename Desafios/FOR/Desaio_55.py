peso = 0.0
maior = 0.0
menor = 0.0

for cont in range(0, 5):
    peso = float(input('Digite seu peso: '))

    if cont == 0:
        maior = peso
        menor = peso

    elif peso >= maior:
        maior = peso

    elif peso <= menor:
        menor = peso

print(f'\nO maior peso é {maior:.2f} \n'
      f'O menor peso é {menor:.2f}')


