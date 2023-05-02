def aumentar(valor, acrescentar, mudar=False):
    aumentado = valor*(acrescentar/100) + valor
    if mudar:
        return moeda(aumentado)
    if not mudar:
        return aumentado


def dobro(valor, mudar=False):
    dobrado = valor * 2
    if mudar:
        return moeda(dobrado)
    if not mudar:
        return dobrado


def diminuir(valor, descontar, mudar=False):
    descontado = valor - (valor*(descontar/100))
    if mudar:
        return moeda(descontado)
    if not mudar:
        return descontado


def metade(valor, mudar=False):
    resultado = valor / 2
    if mudar:
        return moeda(resultado)
    if not mudar:
        return resultado


def titulo(msg):
    tam = len(msg)
    print('-='*tam)
    print('{:^30}'.format(msg))
    print('-='*tam)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor, aumento, diminuicao):
    titulo('RESUMO DO VALOR')
    print('Valor analisado:  ', moeda(valor))
    print('Dobro do preço:   ', dobro(valor, True))
    print('Metade do preço:  ', metade(valor, True))
    print('{}% de aumento:   '.format(aumento), aumentar(valor, aumento, True))
    print('{}% de desconto:  '.format(diminuicao), diminuir(valor, diminuicao, True))
    print('-='*15)
