import streamlit as st
import pandas as pd
from api.api import get_dados_fundamentus
from utils.string_to_float import *

def df_fundamentus():
  data = get_dados_fundamentus()
  df = pd.DataFrame(pd.read_html(data.content, decimal=',', thousands='.')[0])
  return df

df = df_fundamentus()

st.write(df)