valores = []
maior = menor = 0
for c in range(0, 5):
    v = int(input('Digite algum valor para a posição {}:'.format(c)))
    valores.append(v)
    if c == 1:
        maior = menor = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
print('Os valores digitados foram: {}'.format(valores))
print('O maior valor digitado foi {} na posição '.format(maior),end='')
for c, v in enumerate(valores):
    if v == maior:
        print('{}...'.format(c),end='')
print('\nO menor valor digitado foi {} na posição '.format(menor),end='')
for pos, v in enumerate(valores):
    if v == menor:
        print('{}...'.format(pos),end='')
