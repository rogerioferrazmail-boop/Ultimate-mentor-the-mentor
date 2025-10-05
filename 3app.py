import pandas as pd
# from config import NUM_MENTORES, SESSOES_POR_MENTOR # Removed import as variables are defined in notebook

mentores = [f"Mentor {i+1}" for i in range(NUM_MENTORES)]

# Cria sessões por mentor
def gerar_sessoes():
    sessoes = []
    for mentor in mentores:
        for i in range(SESSOES_POR_MENTOR):
            sessoes.append({
                "mentor": mentor,
                "sessao_id": f"{mentor}_S{i+1}",
                "data": f"2025-{10+i}-15",
                "zoom": f"https://zoom.us/{mentor.lower().replace(' ', '')}/sessao{i+1}",
                "inscritos": []
            })
    return sessoes

sessoes = gerar_sessoes()