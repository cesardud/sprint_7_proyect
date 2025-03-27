import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv("vehicles_us.csv")
st.header("Análisis de vehículos en venta en E.U.A")

hist_button = st.button('Construir histograma') # crear un botón
if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')
if disp_button:
    st.write("Creación de una gráfica de dispersión para el conjunto de datos de anuncios de venta de coches")
    fig_disp =  px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_disp, use_container_width=True)

build_hist = st.checkbox('Mostrar histograma')
build_disp = st.checkbox('Mostrar gráfico de dispersión')

if build_hist:
    st.write("Histograma de odómetro")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if build_disp:
    st.write("Dispersión entre odómetro y precio")
    fig_disp = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_disp, use_container_width=True)
