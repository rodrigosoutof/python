import bisect

# lista = list()
# cont = 0
# for n in range(0, 5):
#    num = int(input('Digite um número: '))
#    if cont == 0:
#        lista.append(num)
#    else:
#        for v in range(len(lista)):
#            if num >= v:
#                lista.append(0)
#            else:
#                lista.append(1)
#    cont += 1
# print(lista)
# Correção
lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-' *30)
print(f'Os valores digitados em ordem foram {lista}')

# A quem interessar, bisect.insort(lista, n) já insere 'n' na lista de forma ordenada:

numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: {numbers}')
