def ficha(nome='', gols='0'):
    if nome.strip() == '' or nome.isnumeric():
        nome = '<desconhecido>'
    if gols.strip() == '' or gols.isalpha():
        gols = 0
    print('O jogador {} fez {} gols.'.format(nome, gols))


ficha(str(input('Nome do Jogador:')), str(input('Gols:')))
