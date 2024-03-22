print('Para encerrar o programa digite 999')
num = 0
cont = 0
total = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    else:
        cont += 1
        total += num

print(f'\nFoi digitado {cont} números e a soma deles é {total}')