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