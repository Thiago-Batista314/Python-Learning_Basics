pre = float(input('Digite o valor do produto: R$'))
met = input('''Qual vai ser o método de pagamento:
Digite 1 para pagamento à vista com cheque e dinheiro
Digite 2 para pagar com o cartão.''')
if met == '1':
    print('Então, o produto terá 10% de desconto, ficando R${:.2f}'.format(pre - (pre * 1/10)))
elif met == '2':
    vista = pre - (pre * 1/20)
    cart = input(''''Quer à vista, com 5% de desconto, ou parcelado?
    Parcelado em 2x fica o preço normal;
    Parcelado em 3x ou mais, tem 20% de juros;
    Para escolher, digite "à vista" ou "parcelado"''')
    if cart == 'à vista':
        print('Então, o valor vai ser R${}'.format(vista))
    elif cart == 'parcelado':
        vez = input('Em quantas vezes?')
        if vez == '2':
            print('Então o produto não terá desconto.')
        if vez >= '3':
            print('''Então o preço do porduto será R$ {},
ou seja, juros de 30%.'''.format(pre + (pre * 1/5)))
