import random
import time
palpites = []
print('-='*15)
print('{:^30}'.format('joga na mega-sena'.upper()))
print('-='*15)
n = int(input('Quer que eu faça quantos palpites?'))
for c in range(0, n):
    jogo = []
    for v in range(0, 6):
        jogo.append(random.randint(0, 60))
        for i in jogo:
            if i in jogo:
                jogo[v] = random.randint(0, 60)
        jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()
    print('Jogo {}: {}'.format(c+1, palpites[c]))
    time.sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)
