def notas(*n, sit=False):
    """
    -> Função para análise das notas
    :param n: recebe uma ou mais notas
    :param sit: pode mostrar ou não a situação da classe
    :return: retorna um dicionário com as informações de maior, menor e a média das notas.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'

    return r


resp = notas(5.2, 2.5, 10, sit=True)
print(resp)
help(notas)