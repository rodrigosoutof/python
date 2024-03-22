print('-'*30)
print('Sequencia Fibonacci')
print('-'*30)
n = int(input('Digite quatos termos você quer mostrar: '))
print('~'*30)

t1 = 0
t2 = 1
cont = 3

print(f'{t1} -> {t2} ->', end='')

while cont <= n:
    t3 = t1 + t2
    print(f' {t3} ->', end='')
    cont += 1
    t1 = t2
    t2 = t3
    t3 = 0
print('FIM', end='')








