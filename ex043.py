alt = float(input('Digite sua altura em metros:'))
pes = float(input('Digite seu peso am kg:'))
imc = pes / (alt**2)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
