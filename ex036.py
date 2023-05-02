vi = float(input('Qual o valor da casa?'))
sal = float(input('Qual o valor do salário?'))
tem = float(input('Em quantos meses vai pagar?'))
if vi / tem > (sal * 3/10):
    print('''O empréstimo foi negado!
    Pois o valor da prestação mensal ({:.2f}) foi maior que
    30% do valor da Salário para cobrir
    o valor da casa no período de {} meses'''
          .format(vi / tem , tem))
elif vi / tem < (sal * 3/10):
    print('''O empréstimo foi aprovado!
    Pois o valor do prestação mensal ({:.2f}) foi menor que
    30% do valor da Salário para cobrir
    o valor da casa no período de {}'''
          .format((vi / tem),tem))
