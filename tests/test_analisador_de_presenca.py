from fast import AnalisadorDePresenca


def test_quando_1colaborador_comparece_a_todos_workshops_e_outro_colaborador_comparece_a2_seguidos_entao_retorna_alco2_hbas():
    """
    Neste exemplo, o colaborador com identificador 'hbas' compareceu a todos os workshops e
    'alco2' aos 2 últimos."""
    input = ["hbas ies", "alco2 hbas", "pot alco2 hbas"]
    output = ["alco2", "hbas"]
    ap = AnalisadorDePresenca(input)
    assert ap.ColaboradoresQueViram2WorkshopsSeguidos() == output


def test_quando_2colaboradores_comparecem_a_workshops_seguidos_entao_retorna_alco_hbas():
    """
    Neste exemplo, os 2 primeiros workshops tiveram a presença de 'hbas' e 'alco'. Não houve
    nenhuma repetição nos workshops seguintes.
    """
    input = [
        "hbas ies alco",
        "alco hbas tst gkmo",
        "pot aacs alco aaosc fgrr",
        "till ies alco2 tst gkmo hbas",
    ]
    output = ["alco", "hbas"]
    ap = AnalisadorDePresenca(input)
    assert ap.ColaboradoresQueViram2WorkshopsSeguidos() == output


def test_quando_nenhum_colaborador_comparece_nos_workshops_de_forma_consecutiva_entao_retorna_list_vazia():
    """
    Neste exemplo, o segundo workshop não teve a presença de nenhum colaborador e, portanto,
    não houve nenhum colaborador que tenha comparecido a 2 workshops seguidos.
    """
    input = ["hbas ies", "", "alco hbas gkmo"]
    output = []
    ap = AnalisadorDePresenca(input)
    assert ap.ColaboradoresQueViram2WorkshopsSeguidos() == output


def test_quando_nao_houve_workshops_entao_retorna_lista_vazia():
    """
    Neste exemplo, não houve nenhum workshop e, portanto, não houve nenhum colaborador que
    tenha comparecido a 2 workshops seguidos.
    """
    input = []
    output = []
    ap = AnalisadorDePresenca(input)
    assert ap.ColaboradoresQueViram2WorkshopsSeguidos() == output


def test_quando_2colaboradores_comparecem_em_todos_workshops_entao_retorna_hbas_ies():
    """
    Neste exemplo, tanto o colaborador com identificador 'hbas' quanto o colaborador com
    identificador 'ies' compareceram a todos os workshops.
    """
    input = ["hbas ies", "hbas ies"]
    output = ["hbas", "ies"]
    ap = AnalisadorDePresenca(input)
    assert ap.ColaboradoresQueViram2WorkshopsSeguidos() == output
