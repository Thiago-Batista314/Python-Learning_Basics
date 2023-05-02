da = float(input('Foi alugado por quantos dias?'))
km = float(input('Quantos quilometros rodados?'))
pa = da*60 + km*0.15
print('O total do aluguel foi de R${:.2f}'.format(pa))
