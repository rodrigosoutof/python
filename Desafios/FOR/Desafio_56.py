nome = ''
idade = 0
sexo = ''
total = 0
validacao_m = 0
validacao_f = 0
nom = ''
ida = ''
sex = ''

for cont in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo(M ou F): ')

    if sexo == 'M' or 'F':
        total += idade
        media = total / 4

        if validacao_m == 0 and sexo == 'M':
            validacao_m += 1
            nom = nome
            ida = idade
            sex = sexo

        elif idade > ida:
            nom = nome
            ida = idade
            sex = sexo

        elif sexo == 'F' and idade < 20:
            validacao_f += 1

    else:
        print('Você digitou o sexo errado, favor preencher novamente.')

print(f'\nO nome do homem mais velho é {nom}, ele tem {ida} anos e é do sexo {sex}.\n'
      f'A média da idade do grupo é de {media} anos.\n'
      f'A quantidade de mulheres menores de 20 anos é de {validacao_f} mulher(es).')







