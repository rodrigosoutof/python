n2 = int(input('Digite um numero entre 0 a 9999: '))

if 9999 >= n2 >= 1000:
    n1 = str(n2)
    print(f'''  
    Milhar:  {n1[0]}
    Centena: {n1[1]}
    Dezena:  {n1[2]}
    Unidade: {n1[3]}''')

elif 1000 > n2 >= 100:
    n1 = str(n2)
    print(f'''  
    Centena: {n1[0]}
    Dezena:  {n1[1]}
    Unidade: {n1[2]}''')

elif 100 > n2 >= 10:
    n1 = str(n2)
    print(f'''
    Dezena:  {n1[0]}
    Unidade: {n1[1]}''')

elif 10 > n2 >= 0:
    n1 = str(n2)
    print(f'Unidade: {n1[0]}')

else:
    print('Esse número esta fora do range solicitado!')





