import datetime


def voto(ano_de_nascimento):
    """
    :param ano_de_nascimento: Put the birth year for know if you may vote.
    :return: Nothing
    """
    possibilidade = datetime.date.today().year - ano_de_nascimento

    if 18 <= possibilidade <= 60:
        return 'Obrigatório'
    if 16 <= possibilidade <= 17 or possibilidade > 60:
        return 'Opcional'
    if possibilidade < 16:
        return 'Negado'


resp = voto(2007)
print('Você tem estado de voto:', resp)
