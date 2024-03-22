frase = input('Digite uma palavra ou frase para verificar se é um palíndromo: ').upper()
frase = frase.replace(' ', '')
inverso = ''

for cont in range(len(frase) - 1, -1, -1):
    inverso += frase[cont]

print(frase,
      inverso)

if inverso == frase:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
