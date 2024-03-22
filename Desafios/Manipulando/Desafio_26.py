frase = str(input('Digite sua frase: ')).strip().upper()
print('Há {} letras A na frase'.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece pela primeira vez na posição {}'.format(frase.rfind('A')+1))


