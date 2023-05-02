from datetime import date
ano = int(input('Digite algum ano: Coloque 0 para o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('é um ano bissexto!')
else:
    print('não é bissexto!')
