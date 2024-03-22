import random
#print(f'O numero sorteado é {random.choice([0,1,2,3,4,5])}')

var = random.choice([0, 1, 2, 3, 4, 5])

num = int(input('Digite um numero entre 0 e 5: '))

if num == var:
    print(f'''
    Você escolheu o numero {num}
    O numero sorteado foi {var}
    
    VOCÊ ACERTOU !!! ''')

else:
    print(f'''
    Você escolheu o numero {num}
    O numero sorteado foi {var}

    VOCÊ ERROU !!! ''')
