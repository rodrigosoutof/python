def area(a, b):
    total = a * b
    print(f'A area total do terreno é {total:.2f}')


while True:

    largura = float(input('Digite a largura do terreno: '))
    comprimento = float(input('Digite o comprimento do terreno: '))
    area(largura, comprimento)
    print()

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if cont == 'N':
        break
