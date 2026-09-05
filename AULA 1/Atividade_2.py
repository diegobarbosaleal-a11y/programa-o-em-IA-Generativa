# Formulário de Cadastro de Usuário

import streamlit as st
st.header('Cadastro de Clientes')
st.divider()
Texto_Nome = st.text_input("Adicione seu nome completo", )

st.divider()
Numero_Idade = st.number_input('Digite sua idade: ', step=1, value =0)

st.divider()
Selecao_Box = st.selectbox(
    "Já utilizou alguma Inteligencia Artificial Generativa:",
    ["Selecionar","Sim", "Não"]
)

st.divider()

if st.button("Enviar Respostas", type="primary"):
    if not Texto_Nome:
        st.error("Por favor, preencha o seu nome completo.")
    elif Numero_Idade <= 0:
        st.error("Por favor, insira uma idade válida.")
    elif Selecao_Box == "Selecionar":
        st.error("Por favor, selecione uma opção sobre o uso de IA.")
    else:
        st.divider()
        st.success("Formulário enviado com sucesso!")
        st.markdown("### Dados Cadastrados:")
        st.write(f"**Nome:** {Texto_Nome}")
        st.write(f"**Idade:** {Numero_Idade} anos")
        st.write(f"**Já usou IA Generativa:** {Selecao_Box}")
