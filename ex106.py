def titulo(msg, cor=''):
    tam = len(msg)+4
    print('{}'.format(cor)+'-=' * (int(tam/2)+1))
    print(' ', msg.upper())
    print('-=' * (int(tam/2)+1))


def pyhelp():
    from time import sleep
    titulo('SISTEMA DE AJUDA pyHELP', '\033[42m')
    ajuda = str(input('\033[mFunção ou Biblioteca >'))

    while ajuda != 'fim':
        sleep(0.5)
        titulo('PROCURANDO COMANDO "{}" NO MANUAL'.format(ajuda), '\033[44m')
        sleep(0.5)

        print('\033[m', end='')
        print('\033[30;47;1m')
        
        help(ajuda)
        sleep(0.25)
        ajuda = str(input('\033[mFunção ou Biblioteca >'))

        if ajuda.lower() == 'fim':
            print('\033[30;41;1mFINALIZANDO PROGRAMA!')
            sleep(0.5)


pyhelp()
