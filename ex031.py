viagem = int(input('Qual a distância da sua viagem, em KM?'))
if viagem <= 200:
    preco1 = viagem * 1/2
    print('O valor dela será: R$', preco1)
else:
    preco2 = viagem * 9/20
    print('O valor dela será: R$',preco2)
