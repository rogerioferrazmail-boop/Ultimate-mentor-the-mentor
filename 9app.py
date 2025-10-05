def encontrar_sessao_por_id(sessoes, sessao_id):
    for sessao in sessoes:
        if sessao["sessao_id"] == sessao_id:
            return sessao
    return None