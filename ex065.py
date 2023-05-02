resp = 'S'
media = maior = menor = soma = quant = 0

while resp == 'S':
    n = int(input('Digite um número:'))
    soma += n
    quant += 1

    if quant == 1:
        maior = menor = n

    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
media = soma / quant
print(soma, media, quant)
print('{} {}'.format(maior, menor))
