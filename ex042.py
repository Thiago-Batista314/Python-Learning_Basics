r1 = float(input('Digite o valor da reta 1:'))
r2 = float(input('Digite o valor da reta 2:'))
r3 = float(input('Digite o valor da reta 3:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Pode formar um triângulo e ele é equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Pode formar um triângulo e ele é isósceles!')
    else:
        print('Pode formar um triângulo e ele é escaleno!')
else:
    print('Não pode formar um triângulo!')
