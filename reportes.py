import streamlit as st
import pandas as pd
import numpy as np
st.title('reportes')
#cargar datos des un csv
ventas_df = pd.read_csv('data/Ventas_minoristas.csv')
ventas_df
st.write(ventas_df.describe())
st.write(ventas_df.dtypes)
st.write(ventas_df.info())
#numero de ventas
num_ventas = ventas_df ['Cantidad'].count()
st.write(f'numero de ventas: {num_ventas}')
total_ventas = ventas_df ['Cantidad'].sum()
st.write(f'total de ventas: {total_ventas}')
#TOP 10 de ventas
top_ventas = ventas_df.nlargest(10, 'Cantidad')
st.write(f'top de ventas:')
st.write(top_ventas)
#total de ventas por mes
# Preparar la data para manejar las fechas (Agrega MES y AÑO) - IMPORTANTE
ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha']) # -> REALIZA UNA CONVERSION
ventas_df['Año'] = ventas_df['Fecha'].dt.year
ventas_df['Mes'] = ventas_df['Fecha'].dt.month
#crear un formato de numero en texto
ventas_df['Mes_texto'] = ventas_df['Mes'].replace({1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'})
st.write(ventas_df)
#LISTA DE productos unicos
productos= ventas_df['Producto'].unique()
st.write(productos)
#lsita de secciones unicas
secciones= ventas_df['Seccion'].unique()
st.write(secciones)
#lista de marca_ID unicas
marca_id= ventas_df['Marca_ID'].unique()
st.write(marca_id)
#rango de cantidad
rango_cantidad= ventas_df['Cantidad'].max()-ventas_df['Cantidad'].min()
rango_fechas= ventas_df['Fecha'].max()-ventas_df['Fecha'].min()
#total de ventas
total_ventas_mes = ventas_df.groupby('Mes_texto')['Cantidad'].sum()
st.write(total_ventas_mes)
#total ventas productos por mes 
total_ventas_producto_mes = ventas_df.groupby(
    ['Producto', 'Mes_texto'])['Cantidad'].sum()
st.write(total_ventas_producto_mes)

