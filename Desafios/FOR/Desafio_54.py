data = ''
maioridade = 0
menoridade = 0
for cont in range(0, 7, 1):
    data = int(input('Digite o ano de seu nascimento: '))
    anos = 2023 - data
    if anos > 18:
        maioridade += 1
    else:
        menoridade += 1

print(f'{maioridade} pessoas já atingiram a maioridade.\n'
      f'{menoridade} pessoas ainda não atingiram a maioridade')
