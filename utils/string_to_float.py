def string_to_float(df, lista_de_colunas):
  for coluna in lista_de_colunas:
    if (df[coluna].dtype == object):
      df[coluna] = df[coluna].str.replace(".", "")
      df[coluna] = df[coluna].str.replace(",", ".")
      df[coluna] = df[coluna].str.rstrip("%").astype("float")/100