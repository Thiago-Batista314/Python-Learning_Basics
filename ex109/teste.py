from ex109 import moeda

valor = float(input('Digite o preço: R$'))
print('O dobro de {} é {}.'.format(moeda.moeda(valor), moeda.dobro(valor, True)))
print('A metade de {} é {}.'.format(moeda.moeda(valor), moeda.metade(valor, True)))
print('O aumento de 80% em {} fica {}.'.format(moeda.moeda(valor), moeda.aumentar(valor, 80, True)))
print('O desconto 35% em {} fica {}.'.format(moeda.moeda(valor), moeda.diminuir(valor, 35, True)))
