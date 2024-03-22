boletim = list()
num = med = 0

while True:

    nome = str(input('Digite o primeiro nome: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    teste = nome, nota1, nota2,
    boletim.append(teste[:])

    cont = ' '
    while cont not in 'SN':
        cont = input('\nDeseja continuar:[S/N] ').upper().strip()
    if cont == 'N':
        break

# print(boletim)
print()
print('No.', end='')
print('   Nome   ', end='')
print('Média')

for i in range(len(boletim)):
    print(f'{i:^3}', end=' ')
    for v, c in enumerate(boletim[i]):
        if v == 0:
            print(f'{c:^10}', end=' ')
        else:
            med += c
    print(f'{med/2:^5}')
    med = 0

while True:
    num = 0
    while num != 999:

        num = int(input('\n Digite o No. de um aluno para verificar as notas:(999 interrompe o programa) '))
        for i in range(len(boletim)):
            if num == i:
                for v, d in enumerate(boletim):
                    print(f'{d}', end=' ')

    if num == 999:
        break





