print('=='*20)
print('OS 10 PRIMEIROS VALORES DA P.A.!!!')
print('=='*20)
print()
num = int(input('Digite o 1º valor da P.A.:'))
raz = int(input('Digite a razão dessa P.A.:'))
fórmula = num + (11 - 1) * raz
for c in range(num, fórmula, raz):
    print(c, end = ' => ')
print('FIM!!!')