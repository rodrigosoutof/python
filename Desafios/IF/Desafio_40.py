n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi {:.2f}, você está REPROVADO(A)!'.format(media))
elif media > 7:
    print('Sua média foi {:.2f}, você está APROVADO(A)!'.format(media))
else:
    print('Sua média foi {:.2f}, você está de RECUPERAÇÃO!'.format(media))

