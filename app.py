import pandas as pd
import plotly.express as px
import streamlit as st

# Ler os dados apenas uma vez
car_data = pd.read_csv('vehicles_us.csv')

st.title('Análise de Veículos')

# Botão para histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para histograma
build_histogram = st.checkbox('Criar um histograma (via checkbox)')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão (odômetro x preço)')

if scatter_button:
    st.write('Gráfico de dispersão entre odômetro e preço')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)