mais_barato = ''
mil = soma = cont = maior = menor = 0
print('Digite 0 nos dois para acabar.')
while True:
    produto = str(input('Produto:'))
    preco = float(input('Preço: R$'))
    cont += 1
    if produto == '0' and preco == 0:
        break
    if preco >= 1000:
        mil += 1
    if cont == 1:
        maior = menor = preco
    else:
        if preco > maior:
            maior = preco
        if preco < menor:
            menor = preco
            mais_barato = produto
    soma += preco
print('O total da compra foi R$', soma)
print('O produto mais barato foi o {} custando R$ {:.2f}'.format(mais_barato, menor))
print('{} produto(s) passaram de R$1000'.format(mil))
