rest50 = rest20 = rest10 = rest01 = 0
total50 = total20 = total10 = total01 = 0

print('-'*30)
print('Banco Ferreira')
print('-'*30)

saq = float(input('\nQuanto deseja sacar?\n'
                  'Valor: '))
while True:
    if saq >= 50:
        total50 = saq % 50
        if total50 == 0:
            rest50 = saq / 50
            print(f'Foi necessario {rest50:.0f} notas de R$50,00')
            break
        else:
            rest50 = saq // 50
            total50 = saq - (50 * rest50)
            print(f'Foi necessario {rest50:.0f} notas de R$50,00')
            if total50 == 20:
                rest20 = total50 / 20
                print(f'Foi necessario {rest20:.0f} notas de R$20,00')
                break
            elif total50 > 20:
                rest20 = total50 // 20
                total20 = total50 - (20 * rest20)
                print(f'Foi necessario {rest20:.0f} notas de R$20,00')
                if total20 == 0:
                    break
                elif total20 == 10:
                    rest10 = total20 / 10
                    print(f'Foi necessario {rest10:.0f} notas de R$10,00')
                    break
                elif total20 > 10:
                    rest10 = total20 // 10
                    total10 = total20 - (10 * rest10)
                    print(f'Foi necessario {rest10:.0f} notas de R$10,00')
                    if total10 == 0:
                        break
                    elif total10 == 1:
                        rest01 = total10 / 1
                        print(f'Foi necessario {rest01:.0f} notas de R$1,00')
                        break
                    elif total10 > 1:
                        rest01 = total10 // 1
                        total01 = total10 - (1 * rest01)
                        print(f'Foi necessario {rest01:.0f} notas de R$1,00')
                        if total01 == 0:
                            break
                elif total20 < 10:
                    rest01 = total20 / 1
                    print(f'Foi necessario {rest01:.0f} notas de R$1,00')
                    break

print('Fim!')