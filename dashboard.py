import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# Quant de manifestação em e-ouv, ligações, e-sic, mail e pedidos de acesso a informação
# Tempo de resposta médio

df = pd.read_excel(r'C:/Users/marcu/Documents/UnB/CFQ/Controle de Manifestações 2024 - Versão 29-04.xlsx', sheet_name= 'Ouvidoria em Números')
# mes = st.sidebar._checkbox(df['Mês'])

selected_months = []
for mes in df['Mês']:
    if st.sidebar.checkbox(mes):  # cria um checkbox para cada mês
        selected_months.append(mes)

# df_filtered = df[df['Mês'] == mes]
# df_filtered

# col1, col2 = st.columns(2)
# col3, col4, col5 = st.columns(3)

# fig = px.bar(df_filtered, x=)

st.write("Meses selecionados:", selected_months)

print(df)