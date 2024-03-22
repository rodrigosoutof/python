casa = float(input('Digite o valor da casa que deseja comprar: '))
sal = float(input('Digite seu salário: '))
anos = int(input('Digite em quantos anos você pretende pagar: '))
meses = int(input('Digite os meses, caso haja: '))

juros = sal + (sal * 0.3)
temp_total = meses + (anos * 12)
prest = casa / temp_total

print(f'O valor da sua casa é de R$ {casa :.2f}\n'
      f'A mensalidade será de R$ {prest :.2f}')

if juros < prest:
    print('\nVocê não pode pagar essa prestação, ela excede em 30% seu salário.\n'
          f'Você pode pagar no maxímo R$ {juros :.2f}')
else:
    print('\nParabéns, você recebera o emprestimo para comprar a casa!')




