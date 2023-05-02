lista = ('Python', 'Data Analisys', 'Rezar', 'Estudar')
for elemento in lista:
    print('\nA palavra {} tem essas vogais:'.format(elemento.upper()), end='')
    for letra in elemento:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
