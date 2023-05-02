from datetime import date
cont = 0
contm = 0
for c in range(0, 7):
    idade = int(input('Digite os anos de nascimento de pessoas aleatórias:'))
    atual = date.today().year - idade
    if atual > 21 or atual == 21:
        cont = cont + 1
    else:
        contm = c + 1 - cont
print('{} pessoas são maiores de idade.'.format(cont))
print('{} pessoas são menores de idade.'.format(contm))
