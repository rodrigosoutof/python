def escreva(a):
    tamanho = (len(a)) + 2
    print('~'*tamanho)
    print(f'{a:^{tamanho}}')
    print('~'*tamanho)


palavra = str(input('Escreva qualquer coisa: '))
escreva(palavra)
