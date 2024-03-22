nome = input('Digite seu nome: ')
# print('\nBem vindo(a) ',nome, '!') - > maneiras para passar variavel
print('\nBem vindo(a) {}!'.format(nome))
print(f'É um prazer te ter em nosso curso {nome}!\n')

dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')

print('\n Você nasceu ', dia, '/', mes, '/', ano)

print('\n Vamos somar')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
total = n1 + n2
print('\n O resultado da soma é: ',total)