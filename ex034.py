sal = int(input('O salário do funcionário:'))
if sal > 1250:
    aumento = (sal * 10/100) + sal
    print('Passará a receber R$', aumento)
if sal <= 1250:
    aumento = (sal * 15/100) + sal
    print('Passará a receber R$', aumento)
