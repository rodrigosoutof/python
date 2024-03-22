historico = dict()

historico['nome'] = str(input('Digite o nome: '))
historico['media'] = float(input('Digite a média: '))

if historico['media'] < 6:
    historico['situacao'] = 'Reprovado'
else:
    historico['situacao'] = 'Aprovado'

print(f'- O nome do aluno(a) é: {historico["nome"]}')
print(f'- A média é: {historico["media"]}')
print(f'- A situação é: {historico["situacao"]}')

# correção
print()
for k, v in historico.items():
    print(f'- {k} é igual a {v}')