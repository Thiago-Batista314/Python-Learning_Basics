preco = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20)
for c in range (0, len(preco)):
    if c % 2 == 0:
        print(f'{preco[c]:.<30}', end='R$')
    if c % 2 == 1:
        print('{:.>}'.format(preco[c]))
