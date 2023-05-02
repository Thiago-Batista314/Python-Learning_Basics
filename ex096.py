def area(larg, comp):
    total = larg * comp
    print('A área desse terreno é de {} x {} = {}'.format(larg, comp, total))


def cabecalho(n, msg):
    print('-'*n)
    print(f'{msg:^}')
    print('-'*n)


cabecalho(20, "Área total")
area(larg=float(input('Digite a largura do terreno (m): ')), comp=float(input('Digite o comprimento do terreno (m): ')))
