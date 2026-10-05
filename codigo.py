import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv('vendas.csv')
st.write('# Sistema de vendas online')

st.sidebar.write('## Cadastrar vendas')
Data = st.sidebar.date_input('Data')
Vendedor = st.sidebar.selectbox('Vendedor',['Ana', 'Bruno', 'Carla'])
Produto = st.sidebar.selectbox('Produto',['Notebook', 'Celular', 'Fone'])
Quantidade =st.sidebar.number_input('Quantidade', step=1)
Valor = st.sidebar.number_input('Valor')
Botao_cadastrar = st.sidebar.button('Botao de cadastro')
if Botao_cadastrar:
    nova_venda = [str(Data), Vendedor, Produto, Quantidade, Valor, ]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv('vendas.csv', index=False)
    st.success('Venda cadastrada')


st.write('## Vendas cadastradas')
st.dataframe(tabela_vendas)

st.write('## Dashboard')
faturamento = tabela_vendas['valor'].sum()
st.metric('Faturamento Total', f'R${faturamento}')
grafico1= px.bar(tabela_vendas, x= 'vendedor', y='valor',color='produto')
st.plotly_chart(grafico1)
grafico2 = px.pie(tabela_vendas, names='produto',values='valor')
st.plotly_chart(grafico2)








