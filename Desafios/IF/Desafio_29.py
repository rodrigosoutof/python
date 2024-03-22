vel = int(input('Digite a velocidade do veiculo: '))
valor = (vel - 80) * 7.00

if vel > 80:
    print('Você foi multado ! \n'
          f'Sua multa é de R$ {valor :.2f}')

