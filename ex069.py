maior = homens = menor = 0
while True:
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper().strip()
    ver = str(input('Quer continuar [S/N]:')).upper().strip()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if idade <= 20 and sexo == 'F':
        menor += 1
    if ver == 'N':
        break
print('Pessoas com mais de 18 anos: {}\nHomens cadastrados: {}\nMulheres com menos de 20 anos: {}'.format(maior, homens, menor))
    