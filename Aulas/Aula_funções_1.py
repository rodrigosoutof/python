def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# programa principal
soma(4, 5)
soma(b=8, a=9)
soma(2, 1)
print()


# empacotando parâmetros
def contador(*num):  # * pode ser 0 ou varios numeros
    # for valor in num:
    #    print(f'{valor} ', end='')
    # print('Fim')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 3)
contador(5, 3, 6, 8, 10)
print()


def soma(* val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')


soma(5, 4)
soma(1, 2, 3)
print()


# Trabalhando com listas
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
print()


