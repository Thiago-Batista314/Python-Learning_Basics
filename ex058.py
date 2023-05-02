from random import randint
comp = randint(0, 10)
cont = 0
acertou = False
print('Pensei num número entre 0 e 10. Tente adivinhá-lo.')
while not acertou:
    jog = int(input('Qual o seu palpite?'))
    cont += 1
    if jog == comp:
        acertou = True
    else:
        if jog > comp:
            print('Menos... Tente novamente:')
        elif comp > jog:
            print('Mais... Tente novamente:')
print('Acertou!!! Foram {} tentativas.'.format(cont))
