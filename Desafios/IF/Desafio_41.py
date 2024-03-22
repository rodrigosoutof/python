ano = int(input('Digite seu ano de nascimento: '))
res = 2023 - ano

if res <= 9:
    print(f'Você tem {res} anos, você está na categoria MIRIM.')
elif 9 < res <= 14:
    print(f'Você tem {res} anos, você está na categoria INFANTIL.')
elif 14 < res <= 19:
    print(f'Você tem {res} anos, você está na categoria JUNIOR.')
elif res == 20:
    print(f'Você tem {res} anos, você está na categoria SENIOR.')
else:
    print(f'Você tem {res} anos, você está na categoria MASTER.')
