cont_i = 0
cont_m = 0
cont_f = 0

while True:
    idade = int(input('\nDigite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite seu genero [M/F]: ').upper().strip()[0]

    if idade > 18:
        cont_i += 1

    if sexo == 'M':
        cont_m += 1

    if idade < 20 and sexo == 'F':
        cont_f += 1

    conf = ' '
    while conf not in 'SN':
        conf = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if conf == 'N':
        break

print('~'*30)
print(f'Há {cont_i} pessoas maiores de 18 anos. ')
print(f'Há {cont_m} homens cadastrados.')
print(f'Há {cont_f} mulheres menores de 20 anos.')
print('~'*30)




