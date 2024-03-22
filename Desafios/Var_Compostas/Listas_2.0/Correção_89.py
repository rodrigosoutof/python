ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = (nota1 / nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] '))
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    print('-=' * 35)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe o programa) '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte Sempre! >>>')
