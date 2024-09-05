import streamlit as st
from helpers.visualization import *

st.title('Análise de ações')

if not st.session_state['authentication_status']:
  st.info('Please Login from the Home page and try again.')
  st.stop()

st.title("Ações com requisito mínimo")
st.write('Liquidez nos últimos 2 meses maior que 1 milhão.')
st.write(minimum_requirements_df)
st.write(minimum_requirements_df.shape)

st.title("Tabela filtrada")
st.write("Tabela após a aplicação dos filtros de análise fundamentalista.")
col1, col2, col3 = st.columns(3)

col1.subheader("Dividend Yield")
col1.write(df_div_yield)
col1.write(df_div_yield.shape)

col2.subheader("P/VP")
col2.write(df_p_vp)
col2.write(df_p_vp.shape)

col3.subheader("ROE")
col3.write(df_roe)
col3.write(df_roe.shape)

st.subheader("Ações selecionadas")
st.write("Ações para análise que aparecem nas três tabelas.")
st.write(df_acoes_comum)
st.write(df_acoes_comum.shape)