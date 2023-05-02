from time import sleep


def contador():
    # Contagem Automática
    print('-='*20)
    print('Contagem de 1 a 10 de 1 em 1:')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.25)
    print('\n', '-=' * 20)
    print('Contagem de 10 a 0 e 2 em dois:')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.25)
    print('\n', '-=' * 20)
    # Contagem Personalizada
    print('Faça sua contagem personalizada:')
    i = int(input('Início:'))
    f = int(input('Fim:'))
    p = int(input('Passo:'))
    if p == 0:
        p = 1
    if i < f and p > 0 or i > f and p < 0:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.25)
    if i > f and p > 0 or i < f and p < 0:
        p = p*-1
        if f < 0:
            f -= 1
        for c in range(i, f, p):
            print(c, end=' ')
            sleep(0.25)


contador()
