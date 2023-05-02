num = int(input('Digite o 1º valor da P.A.:'))
raz = int(input('Digite a razão da P.A.:'))
termo = num
cont = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while cont <= total:
        print(termo, ' => ', end='')
        termo = termo + raz
        cont += 1
    print('Pausa')
    mais = int(input('Quer ver mais quantos termos?'))
print('Você viu {} termos da PA'.format(total))
