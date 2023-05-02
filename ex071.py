print('='*30)
print('Bancos Batista')
print('='*30)

valor = int(input('Digite o valor a ser sacado: R$'))

while True:

    aa = (valor // 100)
    rest_aa = valor - aa * 100

    a =(rest_aa // 50) # Número de notas de 50 a serem sacadas
    rest_a = rest_aa - a*50

    b = rest_a // 20 # Número de notas de 20 a serem sacadas
    rest_b = rest_a - b*20

    c = rest_b // 10 # Número de notas de 10 a serem sacadas
    rest_c = rest_b - c * 10

    d = rest_c // 5 # Número de notas de 5 a serem sacadas
    rest_d = rest_c - d*5

    e = rest_d // 1 # Número de notas de 1 a serem sacadas

    break

if aa > 0:
    print('Número de notas de 100 a serem sacadas:', aa)

if a > 0:
    print('Número de notas de 50 a serem sacadas:', a)

if b > 0:
    print('Número de notas de 20 a serem sacadas:',b)

if c > 0:
    print('Número de notas de 10 a serem sacadas:',c)

if d > 0:
    print('Número de notas de 5 a serem sacadas:',d)

if e > 0:
    print('Número de notas de 1 a serem sacadas:',e)
