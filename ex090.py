aluno = {}
aluno['nome'] = str(input('Nome do aluno:')).capitalize()
aluno['nota'] = float(input('Média do aluno:'))
print('O nome do aluno é {}'.format(aluno["nome"]))
print('A média do aluno é {}'.format(aluno["nota"]))
print('Sua situação é:', end=' ')
if aluno['nota'] < 7:
    print('Reprovado!')
else:
    print('Aprovado!')
