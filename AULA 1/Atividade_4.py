# Visualizador de Planilhas Interativo

import pandas as pd
import streamlit as st
st.title("Painel de Dados")
dados = {
    "Aluno": ["Maiara", "Diego", "João", "Rafael", "José"],
    "Gasto": ["Luz", "Água", "Internet", "Condomínio", "Gás"],
    "Valor R$": ["110", "75", "100", "295", "55"],
    "Data Vencimento": ["2026-09-01", "2026-09-15", "2026-09-10", "2026-09-30", "2026-09-05"]
}
df = pd.DataFrame(dados)
st.subheader("Visão Interativa")
st.dataframe(
    df, 
    use_container_width=True, 
    hide_index=True           
)
st.markdown("---")
st.subheader("Visão Estática")
st.table(df)
