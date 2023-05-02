from datetime import date
ano = date.today().year
idade1 = int(input('''Digite seu ano de nascimento 
para entrar em alguma categoria de natação:'''))
idade = ano - idade1
if idade < 9:
    print('Sua categoria de natação é MIRIM!')
elif 9 < idade < 14:
    print('Sua categoria de natação é INFANTIL!')
elif 14 < idade < 19:
    print('Sua categoria de natação é JUNIOR!')
elif idade == 19 or idade == 20:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')
