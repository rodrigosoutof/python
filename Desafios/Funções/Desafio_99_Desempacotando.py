def contador(*num):
    m = 0
    print('~' * 50)
    print('Analisando os valores Passados...')
    for i, p in enumerate(num):
        print(f'{p}', end=' ')
        if i == 0:
            m = p
        elif p >= m:
            m = p
    tam = len(num)
    print(f'- Foram informados {tam} valores ao todo.')
    print(f'O maior número digitado é {m}')


contador(2, 1, 3)
contador(5, 3, 62, 8)
contador(6)
contador()
