n1=int(input('Digite um número: '))
print(f'A tabuada de {n1} é:\n\n'
      f'{n1} X 0 = {n1*0}\n'
      f'{n1} X 1 = {n1*1}\n'
      f'{n1} X 2 = {n1*2}\n'
      f'{n1} X 3 = {n1*3}\n'
      f'{n1} X 4 = {n1*4}\n'
      f'{n1} X 5 = {n1*5}\n'
      f'{n1} X 6 = {n1*6}\n'
      f'{n1} X 7 = {n1*7}\n'
      f'{n1} X 8 = {n1*8}\n'
      f'{n1} X 9 = {n1*9}\n'
      f'{n1} X 10 = {n1*10}\n')

cont = 0
while cont <= 10:
    print(f'{n1} X {cont} = {n1*cont}')
    cont = cont + 1
