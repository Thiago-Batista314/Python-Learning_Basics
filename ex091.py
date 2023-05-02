from random import randint
from time import sleep
from operator import itemgetter
c = 0
dicionario = {'Jogador 1': randint(1, 6),
              'Jogador 2': randint(1, 6),
              'Jogador 3': randint(1, 6),
              'Jogador 4': randint(1, 6)}
ranking = []
print('resultados das jogadas!'.upper())
print('-='*20)
for k, v in dicionario.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado!')
sleep(1)
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print('ranking!'.upper())
for i, v in enumerate(ranking):
    print(f'  - {i+1}º Lugar: O {v[0]} tirou {v[1]}')
    sleep(1)
