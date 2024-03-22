# 1 - Leia o nome, idade e sexo de varias pessoas e guarde-os em um dicionário, e todos os dados em uma lista
pessoas = list()
dados = dict()

while True:
    dados['nome'] = str(input('Digite o nome: '))
    dados['idade'] = int(input('Digite a idade: '))
    #correção, somou a idade aqui -> soma += dados['idade']
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Digite o sexo [M/F]: ')).upper().strip()
        if dados['sexo'] not in 'MF':
            print('Sexo inexistente, digite novamente!')
    pessoas.append(dados.copy())
    print()

    conf = ' '
    while conf not in 'SN':
        conf = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if conf == 'N':
        print('Encerrando...')
        print()
        break

print('-='*30)
# 2 - Mostre quantas pessoas foram cadastradas
c = len(pessoas)
print(f'Foram cadastrados um total de {c} pessoas.')
print()

# 3 - Média da idade do grupo
# segunda parte da correção da média ->media = soma / len(pessoas)
#print(f'A média é {media:5.2f}')
med = 0
for c in pessoas:
    for k, v in c.items():
        if k == 'idade':
            med += v/len(pessoas)
print(f'A média da idade das pessoas cadastradas é {med:.2f}')
print()

# 4 - Criar uma lista com todas mulheres
mulheres = list()
for c in pessoas:
    for k, v in c.items():
        if k == 'sexo' and v == 'F':
            mulheres.append(c.copy())
print('As mulheres cadastradas são: ')
print()
for c in mulheres:
    for k, v in c.items():
        print(f'{k} - {v}', end=' - ')
    print()

# 5 - Uma lista com as pessoas com idade acima da média
velhos = list()
print(f'\nAs pessoas que possuem idade acima da média de {med} anos, são: ')
print()
for c in pessoas:
    for k, v in c.items():
        if k == 'idade' and v > med:
            velhos.append(c.copy())
for c in velhos:
    for k, v in c.items():
        print(f'{k} - {v}', end=' - ')
    print()
print('-='*30)







