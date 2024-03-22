def aumentar(v, p=0):
    total = (v * (p/100)) + v
    return total


def diminuir(v, p=0):
    total = v - (v*(p/100))
    return total


def dobro(v):
    total = v * 2
    return total


def metade(v):
    total = v / 2
    return total


def moeda(v):
    preco = f'R$ {v:.2f}'
    return preco


def resumo(v, a=0, d=0):
    msg = 'RESUMO DO VALOR'
    anl = moeda(v)
    dob = moeda(dobro(v))
    met = moeda(metade(v))
    aum = moeda((aumentar(v, a)))
    dim = moeda(diminuir(v, d))
    print('-' * 29)
    print(f'{msg:^29}')
    print('-' * 29)
    print(f' Preço analisado: {anl:>10}')
    print(f' Dobro do preço:  {dob:>10}')
    print(f' Metade do preço: {met:>10}')
    print(f' {a}% aumento:    {aum:>11}')
    print(f' {d}% redução:    {dim:>11}')
    print('-' * 29)

