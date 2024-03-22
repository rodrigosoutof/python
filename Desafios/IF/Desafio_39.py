ano = int(input('Digite o ano do seu nascimento: '))
total = 2023 - ano

if total == 18:
    print(f"Parabéns você já tem {total} anos")
    print('Chegou a hora de você se alistar! ')
elif total < 18:
    print(f'Ainda não é sua hora de se alistar volte daqui {18 - total} anos')
else:
    print(f'Já se passaram {total -18} anos do seu alistamento, regularize sua situação!')