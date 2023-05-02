def notas(*n, situacao=False):
    """
    :param n: Nota do aluno (quantas quiser colocar);
    :param situacao: Se a média do aluno está média, alta ou baixa;
    :return: Retorna o dicionário com as notas, maior e menor nota, média e situação;
    """
    dicionario = {}
    maior = menor = cont = soma = 0

    for nota in n:
        soma += nota
        if nota == n[0]:
            maior = menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
        cont += 1

    media = soma / cont
    dicionario['total'] = cont
    dicionario['maior nota'] = float(maior)
    dicionario['menor nota'] = float(menor)

    if situacao:
        if media <= 3.0:
            situacao = 'Péssima!'
        if 3.1 <= media < 6.0:
            situacao = 'Ruim!'
        if 6.0 <= media < 7.0:
            situacao = 'Medíocre!'
        if 7 <= media <= 9.9:
            situacao = 'Boa!'
        if media == 10:
            situacao = 'Perfeita!'
        dicionario['média'] = media
        dicionario['situação'] = situacao

    return dicionario


resp = notas(10.0, situacao=True)
help(notas)
