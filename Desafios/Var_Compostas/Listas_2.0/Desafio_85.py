numeros = list()
par = list()
impar = list()
dado = 0

for n in range(0, 7):
    dado = int(input(f'Digite o {n+1}ª número: '))
    if dado % 2 == 0:
        par.append(dado)
    else:
        impar.append(dado)

par.sort()
impar.sort()
numeros.append(par[:])
numeros.append(impar[:])
print('=-'*30)
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números impares digitados foram: {numeros[1]}')
print('=-'*30)

