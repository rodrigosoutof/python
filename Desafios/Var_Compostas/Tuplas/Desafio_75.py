#num1 = int(input('Digite o primeiro número inteiro: '))
#num2 = int(input('Digite o segundo número inteiro: '))
#num3 = int(input('Digite o terceiro número inteiro: '))
#num4 = int(input('Digite o quarto número inteiro: '))
#cont = 0
#cont_par = 0
#numeros = (num1, num2, num3, num4)

#for n in numeros:
#    if n == 9:
#       cont += 1

#print(f'\nApareceram {cont}x o número 9')
#print(f'\nA primeira vez que aparece o número 3 é na posição {numeros.index(3)+1}')
#print(f'\nOs números pares são ', end='')

#for n in numeros:
#   if n % 2 == 0:
#        print(n, end=' ')
#print('\n')

#Correção

num = (int(input('Digite o primeiro número inteiro: ')),
       int(input('Digite o segundo número inteiro: ')),
       int(input('Digite o terceiro número inteiro: ')),
       int(input('Digite o quarto número inteiro: ')))

print(f'\nOs valores digitados foram: {num}')
print(f'O número 9 apareceu {num.count(9)} vez(es)')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('Não foi digitado o número 3')
print(f'Os números pares são ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print('\n')