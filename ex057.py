sexo = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Valor não aceito. Digite novamente:')).upper().strip()[0]
print('OK.')
