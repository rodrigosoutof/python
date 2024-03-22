n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

if n3 < n1 > n2 > n3:
    print('A ordem decrescente é: {}, {}, {} '.format(n1, n2, n3))
elif n2 < n1 > n3 > n2:
    print('A ordem decrescente é: {}, {}, {} '.format(n1, n3, n2))
elif n3 < n2 > n1 > n3:
    print('A ordem decrescente é: {}, {}, {} '.format(n2, n1, n3))
elif n1 < n2 > n3 > n1:
    print('A ordem decrescente é: {}, {}, {} '.format(n2, n3, n1))
elif n2 < n3 > n1 > n2:
    print('A ordem decrescente é: {}, {}, {} '.format(n3, n1, n2))
elif n1 < n3 > n2 > n1:
    print('A ordem decrescente é: {}, {}, {} '.format(n3, n2, n1))

if n3 < n1 > n2 > n3:
    print(f'O maior é {n1} e o menor {n3}')
elif n2 < n1 > n3 > n2:
    print(f'O maior é {n1} e o menor {n2}')
elif n3 < n2 > n1 > n3:
    print(f'O maior é {n2} e o menor {n3}')
elif n1 < n2 > n3 > n1:
    print(f'O maior é {n2} e o menor {n1}')
elif n2 < n3 > n1 > n2:
    print(f'O maior é {n3} e o menor {n2}')
elif n1 < n3 > n2 > n1:
    print(f'O maior é {n3} e o menor {n1}')

