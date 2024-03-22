def voto(num):
    from datetime import date
    ano = date.today().year
    idade = ano - num
    if idade < 16:
        return f'Você tem somente {idade} anos, ainda não pode votar.'
    elif 70 >= idade >= 18:
        return f'PARABUEINS! Você tem {idade} anos, e você tem o dever de votar.'
    elif 18 > idade >= 16 or idade > 70:
        return f'Você tem {idade} anos, e seu voto não é obrigatório'


nascimento = int(input('Digite seu ano de nascimento: '))
print(voto(nascimento))
