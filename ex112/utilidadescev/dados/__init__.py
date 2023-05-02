def leia_dinheiro(msg):
    valido = False
    entrada = str(input(msg))
    while not valido:
        while entrada.isalpha() or entrada.strip() == '':
            print('\033[31mERRO!"{}" não é um valor monetário!\033[m'.format(entrada.title()))
            entrada = str(input(msg))
        else:
            valido = True
            final = entrada.replace(',', '.')
            return float(entrada)
