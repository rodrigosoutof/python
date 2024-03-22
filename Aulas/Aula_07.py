# nome = input('Digite seu nome: ')
#print('Prazer em te conhecer {:_^20}!' .format(nome))

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 # divisão inteira
rd = n1 % n2 # resto da divisão
e = n1 ** n2

print('Resultados:\n Soma: {}\n Subtração: {}\n Multiplicação: {}\n Divisão: {}\n'.format(s, sub, m, d), end='>>\n')
print(' Divisão inteira: {}\n Resto da divisão: {}\n Exponencial: {}'.format(di, rd, e))
