# import streamlit as st    # interface grafica 
# import pandas as pd       # tratamento de dados
# from sklearn.linear_model import LinearRegression # o tipo de treinamento do modelo

# st.header('ANALISE DE NOTAS - PREVENDO')

# estudos = pd.DataFrame({
# 'notas':[1,2,4,6,8,10],
# 'horas':[2,4,5,7,9,10]
# })

# #st.scatter_chart(estudos, x = 'horas', y= 'notas')
# modelo_escola = LinearRegression() 
# modelo_escola.fit(estudos[['horas']], estudos['notas'])

# h_estudo = st.slider('horas de estudos', 0,12,5)
# nota_final = modelo_escola.predict([[h_estudo]])
# print(nota_final)

# st.metric(f'sua nota seria' ,f'{min(nota_final[0], 10.0):.1f}')


# st.header('PREVISÃO DE VENDAS')


# dados_vendas = pd.DataFrame({


#    'investimentos':[100,200,300,550,750,800],
#    'faturamento':[1200,2500,3700,3900,5500,6900]


# })


# st.write(dados_vendas)


# # treinar os dados 


# X = dados_vendas[['investimentos']]
# y = dados_vendas['faturamento']


# model = LinearRegression().fit(X,y) # treina o modelo com os dados


# investimento =  st.number_input('Digite o investimento', value = 150)


# if investimento:
#     if st.button('Analisar:'):
    
#         previsao = model.predict([[investimento]])[0] #previsão
#         st.write(f'Faturamento -  previsto R${previsao:.2f} **')# resultado

import streamlit as st    # interface grafica 
import pandas as pd       # tratamento de dados
import numpy as np        # suporte matemático
from sklearn.linear_model import LinearRegression # o tipo de treinamento do modelo

dados =  pd.read_csv('vendas.csv')
df  =  pd.DataFrame(dados)

st.title("Previsão Automática de Vendas")

st.subheader("Histórico de Vendas")
st.dataframe(df, hide_index=True)

modelo_vendas = LinearRegression() 
modelo_vendas.fit(df[['mes']], df['vendas'])

st.subheader("Projeção para os Próximos Meses") 

ultimo_mes = int(df['mes'].max())
proximos_meses = [ultimo_mes + 1, ultimo_mes + 2, ultimo_mes + 3, ultimo_mes + 4]

df_futuro = pd.DataFrame({'mes': proximos_meses})
vendas_projetadas = modelo_vendas.predict(df_futuro)

df_previsao = pd.DataFrame({
    'Mês': proximos_meses,
    'Previsão de Vendas': [f"{v:.0f}" for v in vendas_projetadas]
})

st.subheader("Próximos Meses")
st.dataframe(df_previsao, hide_index=True)
