import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('MI PRIMERA APP')
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df
st.write("IMPRIMIR UN DATAFRAME DE STREAMLIT:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
st.write("un grafico de lineas")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

st.write("un grafico de lineas")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("imprime un plot de map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
st.write("")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.write("input")
st.text_input("tu nombre", key="nombre")
st.text_input("tu apellido", key="apellido")
st.session_state.nombre
st.session_state.apellido


st.write("caja de check box")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
st.write("caja de select box")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

