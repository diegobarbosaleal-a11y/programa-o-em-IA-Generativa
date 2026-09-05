# O Seletor de Cursos

import streamlit as st

st.header('Seja bem-vindo à Aba de seleção de cursos')
st.divider()
cursos_e_tecnologias = {
    "Python": ["Pandas", "NumPy", "Django", "FastAPI", "SQL"],
    "Web": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Inteligência Artificial": ["Scikit-Learn", "TensorFlow", "PyTorch", "OpenCV"]
}

curso_selecionado = st.selectbox(
    "Escolha um curso de seu interesse:",
    ["Selecione um Curso"] + list(cursos_e_tecnologias.keys()),
)

if curso_selecionado != "Selecione um Curso":
    tecnologias_disponiveis = cursos_e_tecnologias[curso_selecionado]
    
    tecnologias_selecionadas = st.multiselect(
        f"Quais tecnologias de {curso_selecionado} você quer aprender?",
        tecnologias_disponiveis,
    )

    if tecnologias_selecionadas:
        st.success(f" Você escolheu o curso de **{curso_selecionado}** com as tecnologias: {', '.join(tecnologias_selecionadas)}.")
    else:
        st.info(" Selecione uma ou mais tecnologias acima para completar sua escolha.")
else:
    st.warning("Por favor, selecione um curso para liberar as tecnologias disponíveis.")