from random import randint
its = ('pedra', 'papel', 'tesoura')
comp = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('qual a sua jogada?'))
print('-=' * 20)
print('Computador jogou', its[comp])
print('jogador jogou', its[jog])
print('-=' * 20)
if comp == 0:
    if jog == 1:
        print('Jogador venceu!')
    if jog == 2:
        print('Computador venceu!!!')
    if jog == comp:
        print('Empate!!!')
elif comp == 1:
    if jog == 0:
        print('Computador venceu!!!')
    if jog == 2:
        print('Jogador venceu!!!')
    if jog == comp:
        print('Empate!!!')
elif comp == 2:
    if jog == 0:
        print('Jogador venceu!!!')
    if jog == 1:
        print('Computador venceu!!!')
    if jog == comp:
        print('Empate!!!')
