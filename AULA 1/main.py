import streamlit as st
import pandas as pd

st.header('Calculadora STREAMLIT')
st.write('Adicione os números para calcular')

dados = pd.read_csv('vendas.csv')

n1 = st.number_input('Digite um número: ', step=1)
n2 = st.number_input('Digite um número: ', value=0, step=1)

soma_, div_, sub_, mult_ = st.columns(4)

if soma_.button('+'):
    soma = n1 + n2
    st.info(soma)
if sub_.button ('-'):
    sub = n1 - n2
    st.info(sub)
if mult_.button ('*'):
    mult = n1 * n2
    st.info(mult)
if div_.button (':'):
    if n2 != 0:
        div = n1 / n2
        st.info(div)
    else:
        st.error("Não é possível dividir por zero")

st.divider()

# 1. MOSTRAR/OCULTAR MAPA
if st.checkbox('Mostrar mapa'):
    st.map()

st.divider()

# 2. MOSTRAR/OCULTAR ANÁLISE DE DADOS
if st.checkbox('Mostrar análise de dados'):
    st.header('ANALISE DE DADOS')
    st.table(dados)
    st.bar_chart(dados, x = 'ano', y ='lucro')
    st.scatter_chart(dados, x = 'venda', y = 'lucro')
    st.line_chart(dados, x= 'ano', y = 'venda')
