lista = []
dados = []
resp = 's'
pesados = leves = cont = 0
nome_pesados = []
nome_leves = []

while resp == 's':
    dados.append(str(input('Nome:')))
    dados.append(int(input('Peso:')))
    lista.append(dados[:])
    dados.clear()

    resp = str(input('Quer continuar [S/N]?')).lower().strip()
    cont += 1

for i in lista:
    if i[1] >= 100:
        pesados += 1
        nome_pesados.append(i[0])
    if i[1] <= 60:
        leves += 1
        nome_leves.append(i[0])

print('Você cadastrou {} pessoas no total.'.format(cont))

if pesados == 1:
    print('1 pessoa tem mais de 100 kg que é {}'.format(nome_pesados))
else:
    print('{} pessoas tem mais de 100 kg que são {}'.format(pesados, nome_pesados))
if leves == 1:
    print('1 pessoa tem menos de 60 kg que é {}'.format(nome_leves))
else:
    print('{} pessoas tem mais de 100 kg que são {}'.format(leves, nome_leves))
