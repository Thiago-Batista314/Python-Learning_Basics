media = 0
cont = 0
homem = 0
mulher = 0
velho = 0
nomevelho = ''
cont1 = 0
for c in range(1, 5):
    print('-'*5, '{}ª PESSOA'.format(c), '-'*5)
    nome = str(input('NOME:'))
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [M/F]:')).upper()
    cont += 1
    media = media + idade
    if sexo == 'M':
        homem += 1
        if c == 1:
            velho = idade
            nomevelho = nome
        if idade > velho:
            velho = idade
            nomevelho = nome
    elif sexo == 'F':
        mulher += 1
        if idade > 20:
            cont1 += 1
print('A média da idade do grupo é {:.0f} anos'.format(media / cont))
print('='* 30)
if cont1 == 1:
    print('{} mulher tem mais que 20 anos.'.format(cont1))
else:
    print('{} mulheres tem mais que 20 anos.'.format(cont1))
print('='*30)
print('Homem mais velho do grupo é o {} e ele tem {} anos.'.format(nomevelho, velho))
print('='*30)
