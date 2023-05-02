alunos = []
resp = 's'
cont = media = 0
while resp == 's':
    cont += 1
    nome = str(input('Nome:')).capitalize()
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    nomes = [nome, [nota1, nota2], media]
    alunos.append(nomes[:])
    nomes.clear()
    resp = str(input('[S/N]:'))
    print('-='*15)
print('-='*20)
print('{:<} {:^10} {:>14}'.format('No.', 'Nome', 'Média'))
for i in range(0, cont):
    print('{:<} {:^15} {:>10}'.format(i, alunos[i][0], alunos[i][2]))
anali = 0
while True:
    anali = int(input('Quer ver as notas de qual aluno? (999 para sair):'))
    while anali > len(alunos)-1 and anali != 999:
        anali = int(input('Valor Inválido! Quer ver as notas de qual aluno? (999 para sair):'))
    if anali != 999:
        print(f'As notas de {alunos[anali][0]} são : {alunos[anali][1]}')
    else:
        print('FINALIZANDO...')
        break
print('Código finalizado com sucesso!')
