nome = input('Digite seu nome completo:')
print('Ele com todas as letras maiúsculas:', nome.upper())
print('Ele com todas as letras minúsculas:',nome.lower())
nome1 = nome.split()
nome2 = "".join(nome1)
print('Todas as letras sem espaços:', len(nome2))
print('quantas letras tem o 1º nome:', len(nome1[0]))
