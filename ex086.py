#                            Solução própria!
# linha1 = []
# linha2 = []
# linha3 = []
# lista = [linha1, linha2, linha3]
# for c in range(0, 3):
#     linha1.append(int(input('Digite um valor para a posição [0, {}]'.format(c))))
# for c in range(0, 3):
#     linha2.append(int(input('Digite um valor para a posição [1, {}]'.format(c))))
# for c in range(0, 3):
#     linha3.append(int(input('Digite um valor para a posição [2, {}]'.format(c))))
# print('-='*30)
# for i in linha1:
#     print('[ {} ]'.format(i), end='')
# print()
# for i in linha2:
#     print('[ {} ]'.format(i), end='')
# print()
# for i in linha3:
#     print('[ {} ]'.format(i), end='')

#                             Solução Guanabara!
import random
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = random.randint(0, 1000)
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print('[{:^5}]'.format(matriz[l][c]), end='')
    print()
