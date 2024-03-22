num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
       'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesste', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    print('-' * 30)
    escolha = int(input('Digite um número inteiro entre 0 a 20: '))
    if 20 >= escolha >= 0:
        print(num[escolha])
        continuar = ' '
        while continuar not in 'SN':
            continuar = input('\nDeseja continuar? [S/N] ').upper().strip()
        if continuar == 'N':
            break
    else:
        print('Número invalido!\n'
              'Tente novamente...')
print('-' * 30)
print('Volte Sempre!')