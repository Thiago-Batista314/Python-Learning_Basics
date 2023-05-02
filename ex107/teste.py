from ex107 import moeda

valor = float(input('Digite o preço: R$'))
print('O dobro de R${:.2f} é R${:.2f}.'.format(valor, moeda.dobro(valor)))
print('A metade de R${:.2f} é R${:.2f}.'.format(valor, moeda.metade(valor)))
print('A redução de 15% em R${} fica R${}.'.format(valor, moeda.diminuir(valor, 15)))
print('O aumento de 15% em R${} fica R${}'.format(valor, moeda.aumentar(valor, 15)))
