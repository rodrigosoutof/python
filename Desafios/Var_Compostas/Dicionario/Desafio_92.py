from datetime import datetime
cliente = dict()

# 1- Ler nome, ano de nascimento(transformar para idade), e carteira de trabalho
cliente['Nome'] = str(input('Digite seu nome: '))
cliente['Nascimento'] = int(input('Digite o ano em que nasceu: '))
cliente['Idade'] = datetime.now().year - cliente['Nascimento']
cliente['Carteira'] = int(input('Digite o número da sua carteira de trabalho (0 caso não tenha): '))

# 2 - Se cliente possuir carteira de trabalho, devemos registrar ano de contratação e salario
if cliente['Carteira'] > 0:
    cliente['Contrato'] = int(input('Digite o ano da sua contratação primeira contratação: '))
    cliente['Aposentadoria'] = (cliente['Contrato'] + 35) - cliente['Nascimento']
    cliente['Salario'] = float(input('Digite seu salário: '))
print('=-'*30)
print()
for k, v in cliente.items():
    print(f'{k} tem o valor {v}')
