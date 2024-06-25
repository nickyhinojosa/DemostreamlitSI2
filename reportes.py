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
st.write(ventas_df)
