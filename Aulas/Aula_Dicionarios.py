import random
pessoas = {'nome': 'Rodrigo', 'sexo': 'M', 'idade': 30}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

pessoas['peso'] = 60.1
del pessoas['sexo']

pessoas['nome'] = 'Tiririca'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Dicionário em listas
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]["uf"])
print('-=' * 30)
print()
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for est in brasil:
    for val in est.values():
        print(val, end=' ')
    print()
