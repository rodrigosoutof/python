print('-' * 30)
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
# galera.append(teste) - cria uma relação entre a lista e o local copiado
galera.append(teste[:])  # realizando a cópia da lista, e não deixando ligação entre a lista e o local copiado
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('-' * 30)

turma = [['Juca', 19], ['Tonico', 33], ['Luna', 4]]
print(turma)
print(turma[0])
print(turma[2][0])
print('-' * 30)

for p in turma:
    print(p)
print('-' * 30)

for p in turma:
    print(f'Somente nome {p[0]}')
print('-' * 30)

for p in turma:
    print(f'Somente idade {p[1]}')
print('-' * 30)

for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-' * 30)

pessoas = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()

for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')
print(pessoas)
print('-' * 30)




