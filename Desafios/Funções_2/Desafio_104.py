def leiaint(msg):
    ok = False
    val= 0

    while True:
        print(msg, end='')
        n = input(' ')
        if n.isnumeric():
            val = int(n)
            ok = True
        else:
            print(f' \033[1:31m ERRO! Digite um número inteiro válido. \033[0m')
        if ok:
            break
    return val


num = leiaint('Digite número:')
print(f'Você digitou o número {num}')
