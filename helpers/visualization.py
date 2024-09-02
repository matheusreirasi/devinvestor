import pandas as pd
from api.api import get_dados_fundamentus
from utils.string_to_float import *

def df_fundamentus():
  data = get_dados_fundamentus()
  df = pd.DataFrame(pd.read_html(data.content, decimal=',', thousands='.')[0])
  return df

df = df_fundamentus()


colunas_strings_de_numero = ["Div.Yield", "Mrg Ebit", "Mrg. Líq.", "ROIC", "ROE", "Cresc. Rec.5a"]
string_to_float(df, colunas_strings_de_numero)

minimum_requirements_df = df[df["Liq.2meses"] > 1000000]


df_div_yield = pd.DataFrame()
df_div_yield['Papel'] = minimum_requirements_df[ minimum_requirements_df['Div.Yield'] > 0].sort_values(by=['Div.Yield'], ascending=False)['Papel'][:100].values
df_div_yield['Cotação'] = minimum_requirements_df[ minimum_requirements_df['Div.Yield'] > 0].sort_values(by=['Div.Yield'], ascending=False)['Cotação'][:100].values
df_div_yield['Div.Yield'] = minimum_requirements_df[ minimum_requirements_df['Div.Yield'] > 0].sort_values(by=['Div.Yield'], ascending=False)['Div.Yield'][:100].values

df_p_vp = pd.DataFrame()
df_p_vp['Papel'] = minimum_requirements_df[ minimum_requirements_df['P/VP'] > 0].sort_values(by=['P/VP'],ascending=True)['Papel'][:100].values
df_p_vp['Cotação'] = minimum_requirements_df[ minimum_requirements_df['P/VP'] > 0].sort_values(by=['P/VP'],ascending=True)['Cotação'][:100].values
df_p_vp['P/VP'] = minimum_requirements_df[ minimum_requirements_df['P/VP'] > 0].sort_values(by=['P/VP'],ascending=True)['P/VP'][:100].values

df_roe = pd.DataFrame()
df_roe['Papel'] = minimum_requirements_df.sort_values(by=['ROE'], ascending=False)['Papel'][:100].values
df_roe['Cotação'] = minimum_requirements_df.sort_values(by=['ROE'], ascending=False)['Cotação'][:100].values
df_roe['ROE'] = minimum_requirements_df.sort_values(by=['ROE'], ascending=False)['ROE'][:100].values

colunas_comuns = set(df_div_yield.columns) & set(df_p_vp.columns) & set(df_roe.columns)
#df_acoes_comum = df_div_yield.merge(df_p_vp,on= 'Papel').merge(df_roe, on='Papel').drop(columns= colunas_comuns)
df_acoes_comum = df_div_yield.merge(df_p_vp,on= 'Papel').merge(df_roe, on='Papel').drop(columns= ['Cotação_x','Cotação_y'])