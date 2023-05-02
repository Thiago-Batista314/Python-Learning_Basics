while True:
    n = int(input('Quer ver a tabuada de qual valor:'))
    cont = 0
    if n < 1:
        break
    while cont <= 10:
        print('{} x {} = {}'.format(n, cont, n * cont))
        cont += 1

print('ACABARAM AS TABUADAS!!!')
    