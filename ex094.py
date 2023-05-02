dicionario = {}
lista = []
resp = 's'
soma = media = 0

while resp == 's':
    dicionario['nome'] = str(input('Nome:')).title()
    dicionario['sexo'] = str(input('Sexo: [M/F]')).lower()

    while dicionario['sexo'] != 'm' and dicionario['sexo'] != 'f':
        print('\033[31mERRO! Digite apenas M ou F!\033[m')
        dicionario['sexo'] = str(input('\033[33mSexo: [M/F]\033[m')).lower()

    dicionario['idade'] = int(input('Idade:'))
    media += dicionario['idade']
    lista.append(dicionario.copy())
    dicionario.clear()
    soma += 1
    resp = str(input('Quer continar? [S/N]')).lower()

    while resp != 's' and resp != 'n':
        print('\033[31mERRO! Digite apenas S ou N!\033[m')
        resp = str(input('Quer continar? [S/N]')).lower()

media /= soma
print('-='*30)

print('A) Ao todo temos {} pessoas cadastradas.'.format(soma))
print('B) A média de idade é de {:.2f} anos.'.format(media))
print('C) As mulheres cadastradas foram ', end='')

for i in lista:
    if i['sexo'] == 'f':
        print(i['nome'], ' ', end='')

print('\nD) Lista das pessoas que tem idade acima da média:')

for i in lista:
    if i['idade'] > media:
        print('     nome = {}; sexo = {}; idade = {};'.format(i['nome'], i['sexo'], i['idade']))

print('<<< ENCERRADO! >>>')
