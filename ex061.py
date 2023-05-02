print('=='*20)
print('OS 10 PRIMEIROS VALORES DA P.A.!!!')
print('=='*20)
print()
num = int(input('Digite o 1º valor da P.A.:'))
raz = int(input('Digite a razão da P.A.:'))
cont = 0
while cont < 10 :
    print(num, ' => ', end='')
    num += raz
    cont += 1
print('FIM')