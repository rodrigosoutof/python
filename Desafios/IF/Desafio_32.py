ano = int(input('Digite um ano para sabemos se é bissexto: '))
res = ano % 4

if res == 0:
    print(f'Ano {ano} é bissexto.')
else:
    print(f"Ano {ano} não é bissexto.")