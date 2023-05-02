import random

soma = soma_coluna = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = random.randint(0, 10)

        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

        if c == 2:
            soma_coluna += matriz[l][c]

        if l == 1 and c == 0:
            maior = matriz[l][c]

        elif l == 1 and c != 0:
            if matriz[l][c] > maior:
                maior = matriz[l][c]



for l in range(0, 3):

    for c in range(0, 3):
        print('[{:^5}]'.format(matriz[l][c]), end='')

    print()

print('-='*30)
print('A soma de todos os pares é {}'.format(soma))
print('A soma de todos os elementos da terceira coluna é {}'.format(soma_coluna))
print('O maior elemento da segunda linha é {}'.format(maior))
