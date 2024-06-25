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