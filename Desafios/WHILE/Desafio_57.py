sexo = 'F'

while sexo == 'M' or sexo == 'F':
    sexo = input('Digite seu sexo, M para masculino e F para feminino: ').upper()

    if not (sexo == 'F' or sexo == 'M'):
        print('\n\nINVALIDO, TENTE NOVAMENTE !!!'
              '\nM para masculino e F para feminino.\n')

        sexo = 'M'
