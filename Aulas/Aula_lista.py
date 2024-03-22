num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
# num.pop()
# num.pop(0)
num.remove(2) # Remove a primeira ocorrencia do numero
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

# CUIDADO o simbolo = realiza uma ligação de uma lista a outra e não uma copia!

print('\n')
a = [1, 2, 3, 4]
b = a
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# para copiarmos utilizamos o fatiamento de todos valores de uma lista para outra

c = [1, 2, 3, 4]
d = c[:]
d[2] = 9
print(f'Lista C: {c}')
print(f'Lista D: {d}')

