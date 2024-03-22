nome = str(input('Digite seu nome completo: '))
lista = nome.split()

print('''Seu primeiro nome é: {}
Seu segundo nome é: {}'''.format(lista[0], lista[len(lista)-1]))



