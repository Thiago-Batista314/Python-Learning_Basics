from datetime import date
a = int(input('Em que ano você nasceu?'))
ano = date.today().year
alistamento = ano - a
if alistamento > 18:
    print('Se passaram {} anos do seu alistamento.'.format(alistamento - 18))
elif alistamento < 18:
    print('Ainda faltam {} anos para seu alistamento.'.format((alistamento - 18) * -1))
else:
    print('Está na hora de se alistar.')
