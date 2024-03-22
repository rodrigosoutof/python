print('Tabuada automatica'
      '\nDigite qualquer número negativo para finalizar.')

num = 0
cont = 0
total = 0

while True:
    num = float(input('\nDigite um número: '))
    if num < 0:
        break
    else:
        while cont <= 10:
            total = num * cont
            print(f'{num:.2f} x {cont:.2f} = {total:.2f}')
            cont +=1
    cont = 0

print('Volte sempre!')