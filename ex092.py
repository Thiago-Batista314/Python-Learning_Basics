from datetime import date
dicionario = {}
dicionario['nome'] = str(input('Nome:')).title()
dicionario['idade'] = date.today().year - int(input('Ano de Nascimento:'))
dicionario['carteira'] = int(input('Carteira de Trabalho (0 não tem):'))
if dicionario['carteira'] != 0:
    dicionario['contratação'] = int(input('Ano de Contratação:'))
    dicionario['salario'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = dicionario['idade'] + (dicionario['contratação'] + 35 - date.today().year)
print('-='*30)
for k, v in dicionario.items():
    print('-> {} tem valor {}'.format(k, v))
 