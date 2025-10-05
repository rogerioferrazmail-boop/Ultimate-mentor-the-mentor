# Removed import from config as variables are defined in notebook
# from config import LIMITE_PARTICIPANTES

def verificar_vagas(sessao):
    return LIMITE_PARTICIPANTES - len(sessao["inscritos"])

def inscrever(sessao, nome, email):
    if verificar_vagas(sessao) > 0:
        sessao["inscritos"].append({"nome": nome, "email": email})
        return True
    return False