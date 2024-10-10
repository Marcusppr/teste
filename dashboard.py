import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# Carregando o arquivo Excel
df = pd.read_excel('Controle de Manifestações 2024 - Versão 29-04.xlsx', sheet_name= 'Ouvidoria em Números')

# Verifica se a coluna "Mês" existe
if 'Mês' not in df.columns:
    st.error("A coluna 'Mês' não foi encontrada no arquivo Excel.")
else:
    # Criar checkboxes na barra lateral para cada mês único
    selected_months = []
    for mes in df['Mês'].unique():  # Garante que cada mês apareça apenas uma vez
        if st.sidebar.checkbox(mes):  # Cria checkbox para cada mês único
            selected_months.append(mes)

    # Filtrar o DataFrame com base nos meses selecionados
    if selected_months:
        df_filtered = df[df['Mês'].isin(selected_months)]  # Filtrar pelos meses selecionados
    else:
        df_filtered = df  # Se nenhum mês for selecionado, mostrar todos os dados

    # Mostrar os meses selecionados e o DataFrame filtrado
    st.write("Meses selecionados:", selected_months)
    st.dataframe(df_filtered)  # Exibe os dados filtrados

    # Exemplo de gráfico: (Ajuste conforme os dados)
    if not df_filtered.empty:
        fig = px.bar(df_filtered, x='Mês', y='Quantidade de Manifestações')  # Ajuste a coluna y conforme os dados
        st.plotly_chart(fig)

    else:
        st.warning("Nenhum dado disponível para os meses selecionados.")
