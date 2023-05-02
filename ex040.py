nota1 = float(input('Qual foi a primeira nota?'))
nota2 = float(input('Qual foi a segunda nota?'))
media = (nota1 + nota2) / 2
if media < 5:
    print('Você foi REPROVADO pela sua média abaixo de 5.0!')
elif 5 < media < 6.9:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Parabéns! Você está APROVADO!')

