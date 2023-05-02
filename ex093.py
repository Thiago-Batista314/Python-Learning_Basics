jogador = {'nome': str(input('Nome do Jogador:'))}
lista = []
num = int(input('Quantas partidas {} jogou?'.format(jogador['nome'])))
for c in range(0, num):
    gols = int(input('    Quantos gols na {}ª partida?'.format(c + 1)))
    lista.append(gols)
jogador['gols'] = lista[:]
jogador['total'] = sum(lista)
lista.clear()
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print('O campo {} tem valor {}'.format(k, v))
print('-='*30)
print('O jogador {} jogou {} partidas'.format(jogador['nome'], num))
for c in range(0, len(jogador['gols'])):
    print('   => Na partida {}, fez {} gols.'.format(c+1, jogador['gols'][c]))
print('Foi um total de {} gols.'.format(jogador['total']))
