sal = float(input('Digite um salario: '))

if sal < 1250.00:
    valor = sal * 0.15 + sal
    print('Você recebera um aumento de 15%!\n'
          f'Seu novo salario passara de R$ {sal :.2f} para R$ {valor :.2f}')
else:
    valor = sal * 0.10 + sal
    print('Você recebera um aumento de 10%!\n'
          f'Seu novo salario passara de R$ {sal :.2f} para R$ {valor :.2f}')

