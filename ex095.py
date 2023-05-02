time = []
jogador = {}
lista = []
resp = 's'
while resp == 's':
    jogador['nome'] = str(input('Nome do Jogador:'))
    num = int(input('Quantas partidas {} jogou?'.format(jogador['nome'])))
    for c in range(0, num):
        gols = int(input('    Quantos gols na {}ª partida?'.format(c + 1)))
        lista.append(gols)
    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista)
    time.append(jogador.copy())
    jogador.clear()
    lista.clear()
    resp = str(input('Quer continuar? [S/N]')).lower()
    if resp not in 'sn':
        print('\033[31mERRO! Digite apenas S ou N!\033[m')
        resp = str(input('\033[33mQuer continuar? [S/N]\033[m')).lower()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
n = 0
while n != 999:
    n = int(input('Quer mostrar os dados de qual jogador? (999 para finalizar)'))
    while n > len(time)-1 and n != 999:
        print('\033[31mERRO! Digite apenas um número válido!\033[m')
        n = int(input('\033[33mQuer mostrar os dados de qual jogador? (999 para finalizar)\033[m'))
    if n == 999:
        break
    print('--- Levantamento do jogador {} ---'.format(time[n]['nome']).upper())
    for l in range(0, len(time[n]['gols'])):
        print('No jogo {} fez {} gols.'.format(l+1, time[n]['gols'][l]))
    print('-' * 40)
print('<<< ENCERRADO! >>>')
