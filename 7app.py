import pandas as pd

def exportar_csv(sessoes, caminho="inscricoes.csv"):
    dados = []
    for sessao in sessoes:
        for inscrito in sessao["inscritos"]:
            dados.append({
                "Mentor": sessao["mentor"],
                "Sessão": sessao["sessao_id"],
                "Data": sessao["data"],
                "Nome": inscrito["nome"],
                "Email": inscrito["email"]
            })
    df = pd.DataFrame(dados)
    df.to_csv(caminho, index=False)
    return df