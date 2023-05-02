from ex108 import moeda

valor = float(input('Digite o preço: R$'))
print('O dobro de {} é {}.'.format(moeda.moeda(valor), moeda.moeda(moeda.dobro(valor))))
print('A metade de {} é {}.'.format(moeda.moeda(valor), moeda.moeda(moeda.metade(valor))))
print('O aumento de 80% em {} fica {}.'.format(moeda.moeda(valor), moeda.moeda(moeda.aumentar(valor, 80))))
print('O desconto 35% em {} fica {}.'.format(moeda.moeda(valor), moeda.moeda(moeda.diminuir(valor, 35))))
