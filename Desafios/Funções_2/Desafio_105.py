boletim = list()


def notas(lista, situacao=0):
    """
    :param lista: Insere todas notas digitadas
    :param situacao: Possibilita mostrar ou não a situação da classe
    :return: Retorna os dados de maior, menor e a média das notas.
    """
    maior = menor = media = total = 0

    print(lista)
    print(len(lista))

    for i, v in enumerate(lista):
        total += v
        if v > maior:
            maior = v

        if i == 0 or v < menor:
            menor = v

    print(f'A maior nota é: {maior}')
    print(f'A menor nota é: {menor}')
    media = total/len(lista)
    print(f'A média da classe é: {media:.2f}')
    if situacao == 'S' and media <= 3:
        print('A situação da classe esta \033[1:31mRUIM\033[0m!')
    elif situacao == 'S' and 3 < media < 7:
        print('A situação da classe esta \033[1:34mREGULAR!\033[0m')
    elif situacao == 'S' and media >= 7:
        print('A situação da classe está \033[1:32mÓTIMA\033[0m!')


while True:
    n = float(input('Insira a nota: '))
    boletim.append(n)

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar inserido as notas: [S/N] ')).upper().strip()

    if cont == 'N':
        print('-='*30)
        print('Obrigado por utilizar meu programa.\nEm segundos será exibido o relatorio das notas.')
        print('-=' *30)
        break

print()
sit = ' '
while sit not in 'SN':
    sit = str(input('Deseja saber a situação da classe?[S/N] ')).upper() .strip()

notas(boletim, sit)
