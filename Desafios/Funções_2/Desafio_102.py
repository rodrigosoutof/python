def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número.
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


aju = str(input('Quer saber a descrição da função? [S/N] ')).upper().strip()
if aju == 'S':
    help(fatorial)
else:
    num = int(input('Digite um número: '))
    mostrar = str(input('Deseja mostrar o cálculo do fatorial?[S/N] ')).upper().strip()
    if mostrar == 'S':
        print(fatorial(num, show=True))
    else:
        print(fatorial(num, show=False))
