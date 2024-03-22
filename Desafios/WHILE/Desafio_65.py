comf = 'N'
cont = 0
n1 = 0
n2 = 0
n3 = 0
total = 0
maior = 0
menor = 0

while comf == 'N':
    n1 = int(input('Digite um número inteiro: '))

    if n1 < n3 or cont == 0:
        menor = n1

    if n1 > n3 or cont == 0:
        maior = n1

    total = n1 + n2
    n2 = total
    n3 = n1
    cont += 1

    comf = input('Digite S para continuar e N para encerrar: ').upper()

media = total / cont
print('-'*40)
print(f'A média dos números digitados é: {media:.2f}\n'
      f'O menor número digitado é: {menor}\n'
      f'O maior número digitado é: {maior}')

