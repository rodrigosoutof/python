expr = str(input('Digite uma expressão: '))
pilha = []
for simbo in expr:
    if simbo == '(':
        pilha.append('(')
    elif simbo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

