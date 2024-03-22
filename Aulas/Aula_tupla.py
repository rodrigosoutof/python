lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print('-'*40)
print(lanche[1]) # mostra o elemento 1
print('-'*40)
print(lanche[-1]) # mostra o ultimo elemento
print('-'*40)
print(lanche[1:3]) # mostra o elemento 1 até o 2 excluindo o elemento 3
print('-'*40)
print(lanche[:3]) # mostra do inicio até o elemento 3
print('-'*40)
print(lanche[1:]) # mostra do elemento 1 até o fim
print('-'*40)
#lanche[1] = 'Refrigerante' -> Dará erro pois tuplas são imutaveis
print('-'*40)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
print('-'*40)
print(len(lanche))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba')
print('-'*40)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')
print('-'*40)
print(sorted(lanche))
print('-'*40)
print('-'*40)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #ela concatena os elementos não soma. Portanto b + a não é o mesmo.
print(c)
print(c.count(5)) # para contar quantos 5 há na tupla
print(c.index(8)) # para saber a posição que ocorre pela primeira vez o elemento
print(c.index(8, 1)) # para deslocarmos o indice para pesquisarmos
print('-'*40)
print('-'*40)

pessoa = ('Rodrigo', 30, 'Itapetininga')
#del(pessoa) # exclui a variavel da memoria
print(pessoa)

