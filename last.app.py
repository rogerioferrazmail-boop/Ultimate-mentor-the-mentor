import streamlit as st
# from data import sessoes, mentores  # Removed import
# from logic import inscrever, verificar_vagas  # Removed import
# from utils import encontrar_sessao_por_id  # Removed import
# from export import exportar_csv  # Removed import
# from calendar import gerar_ics  # Removed import

st.set_page_config(page_title="Reservas com Mentores", layout="wide")
st.title("Sistema de Reservas com Mentores")

st.sidebar.header("Inscrição")
nome = st.sidebar.text_input("Nome")
email = st.sidebar.text_input("Email")

# Add placeholder data and functions
# You should replace these with your actual data and logic from your project files

sessoes = [
    {"sessao_id": 1, "mentor": "Mentor A", "data": "2024-08-01", "zoom": "link1", "vagas": 5, "inscritos": []},
    {"sessao_id": 2, "mentor": "Mentor A", "data": "2024-08-02", "zoom": "link2", "vagas": 3, "inscritos": []},
    {"sessao_id": 3, "mentor": "Mentor B", "data": "2024-08-03", "zoom": "link3", "vagas": 4, "inscritos": []},
]
mentores = list(set([s["mentor"] for s in sessoes]))

def encontrar_sessao_por_id(sessoes_list, sessao_id):
    for sessao in sessoes_list:
        if sessao["sessao_id"] == sessao_id:
            return sessao
    return None

def verificar_vagas(sessao):
    return sessao["vagas"] - len(sessao["inscritos"])

def inscrever(sessao, nome, email):
    if verificar_vagas(sessao) > 0:
        sessao["inscritos"].append({"nome": nome, "email": email})
        return True
    return False

import pandas as pd

def exportar_csv(sessoes_list):
    all_inscricoes = []
    for sessao in sessoes_list:
        for inscrito in sessao["inscritos"]:
            all_inscricoes.append({
                "sessao_id": sessao["sessao_id"],
                "mentor": sessao["mentor"],
                "data": sessao["data"],
                "nome": inscrito["nome"],
                "email": inscrito["email"]
            })
    return pd.DataFrame(all_inscricoes)

def gerar_ics(sessao, nome):
    # Placeholder function for generating ICS file
    with open(f"{nome}_sessao.ics", "w") as f:
        f.write("BEGIN:VCALENDAR\n")
        f.write("VERSION:2.0\n")
        f.write("BEGIN:VEVENT\n")
        f.write(f"SUMMARY:Sessão com {sessao['mentor']}\n")
        f.write(f"DTSTART:{sessao['data'].replace('-', '')}T100000Z\n") # Example date format
        f.write(f"DTEND:{sessao['data'].replace('-', '')}T110000Z\n")   # Example date format
        f.write(f"LOCATION:{sessao['zoom']}\n")
        f.write("END:VEVENT\n")
        f.write("END:VCALENDAR\n")


mentor_escolhido = st.sidebar.selectbox("Escolhe o mentor", mentores)

# Mostrar sessões do mentor
sessoes_mentor = [s for s in sessoes if s["mentor"] == mentor_escolhido]
sessao_id = st.sidebar.selectbox("Escolhe a sessão", [s["sessao_id"] for s in sessoes_mentor])

if st.sidebar.button("Inscrever"):
    sessao = encontrar_sessao_por_id(sessoes, sessao_id)
    if inscrever(sessao, nome, email):
        st.sidebar.success("Inscrição feita com sucesso!")
        gerar_ics(sessao, nome)
        st.sidebar.download_button("📅 Adicionar ao calendário", data=open(f"{nome}_sessao.ics", "rb").read(), file_name=f"{nome}_sessao.ics")
    else:
        st.sidebar.error("Sessão cheia. Escolhe outra.")

# Página principal
st.subheader("Sessões por Mentor")
for mentor in mentores:
    st.markdown(f"### {mentor}")
    sessoes_do_mentor = [s for s in sessoes if s["mentor"] == mentor]
    dados = []
    for s in sessoes_do_mentor:
        dados.append({
            "Sessão": s["sessao_id"],
            "Data": s["data"],
            "Zoom": s["zoom"],
            "Vagas disponíveis": verificar_vagas(s)
        })
    st.table(dados)

# Exportar dados
if st.button("📤 Exportar inscrições para CSV"):
    df = exportar_csv(sessoes)
    st.download_button("Download CSV", data=df.to_csv(index=False), file_name="inscricoes.csv")