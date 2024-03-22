prod = float(input('Digite o valor do produto: R$ '))
cond = int(input('\nDigite a condição que quer realizar o pagamento\n\n'
                 '1 - À vista Dinheiro/Cheque (10% de desconto)\n'
                 '2 - À vista no cartão (5% de desconto)\n'
                 '3 - Em 2x no cartão (Sem desconto)\n'
                 '4 - Em 3x ou mais no cartão (20% de juros)\n'))

if cond == 1:
    desc = prod * 0.1
    total = prod - desc
    print(f'O preço sem desconto é R$ {prod:.2f}, voce recebeu R$ {desc:.2f} de desconto.\n'
          f'O produto ficara por R$ {total:.2f}')
elif cond == 2:
    desc = prod * 0.05
    total = prod - desc
    print(f'O preço sem desconto é R$ {prod:.2f}, voce recebeu R$ {desc:.2f} de desconto.\n'
          f'O produto ficara por R$ {total:.2f}')
elif cond == 3:
    print(f'O produto não tem desconto, você pagará R$ {prod:.2f}')
elif cond == 4:
    juros = prod * 0.2
    total = prod + juros
    print(f'O preço sem juros é R$ {prod:.2f}, voce pagará R$ {juros:.2f} de juros.\n'
          f'O produto ficara por R$ {total:.2f}')


