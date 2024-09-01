import streamlit as st

st.title("Conceitos e técnicas")

st.write("Os documentos necessários mais importantes para realizar as análises fundamentalistas são: Balanço patrimonial, demonstrativo de resultado do exercício e DFC.")

st.header("Aprenda o básico!", divider= True)

st.subheader("EBITDA")
st.write("""
  Essa análise vem da sigla em inglês para Earning before interest, taxes depreciation and amortization. Esse índice ajuda a analisar o desempenho operacional da empresa mensurando sua produtividade dentro do setor de atuação.
  \nÉ um valor monetário
  \nCálculo:
  \nLucro operacional líquido antes dos impostos + depreciação + amortização + juros
""")
st.subheader("EV/EBITDA")
st.write("""
  Esse indicador é considerado uma medida mais abrangente do que o indicador P/L pois leva em consideração o endividamento da empresa. Ele é utilizado para avaliar o potencial de valorização de uma empresa e a sua atratividade como investimento. Empresas com um EV/EBITDA baixo geralmente são consideradas mais atrativas, pois indicam um valor de mercado relativamente baixo em relação aos seus lucros.
  Por outro lado, empresas com um EV/EBITDA alto podem ser consideradas arriscadas pois indicam um valor de mercado elevado em relação ao seu lucro operacional.
  \nÉ um valor numérico
  \nCálculo:
  \nValor da empresa / Lucro operacional
""")
st.subheader("LPA")
st.write(""" 
  Sigla para lucro por ação, tem função semelhante ao PL, sendo que LPA diz em quanto tempo o investidor veria os lucros daquela ação.
  \nÉ um valor númerivo
  \nCálculo:
  \nLucro líquido 12 meses/Qtd de ações da empresa
""")
st.subheader("P/L")
st.write("""
  É o indicador mais utilizado para avaliar o quão atrativo está o preço de uma ação no mercado se comparado ao preço de ações de outras empresas do mesmo setor. Em geral, se o resultado do cálculo é baixo, o investidor poderá pagar um valor mais atrativo em relação ao potencial demonstrado pelos lucros dos últimos 12 meses, o que pode ser um indicativo de que as ações estão baratas, sendo assim um possível potencial de compra.
  \nÉ um valor numérico
  \nCálculo:
  \n*Preço da ação/Lucro por ação
""")
st.subheader("P/VP")
st.write("""
  Esse indicador mostra o quanto o investidor está disposto a pagar pelo ativo. Quanto mais elevado este indicador, maior o preço que o acionista estará pagando em relação ao valor patrimonial do ativo.
  \nÉ um valor numérico
  \nCálculo:
  \nPreço da ação/Valor patrimonial da ação
  \nPatrimônio líquido/Número total de açõs
""")
st.subheader("P/V")
st.write("""
  O preço dividido pelas vendas mostra a relação entre a capitalização e valor das vendas líquidas da companhia.
""")
st.subheader("Dividend Yield")
st.write("""
  Um dos mais importantes indicadores da análise fundamentalista, sobretudo para aqueles que buscam aplicações com foco em dividendos. Ele mostra ao analista o retorno em proventos que determinado ativo gerou nos últimos 12 meses com base em cotações atuais.
  \nÉ um valor percentual
  \nCálculo:
  \nDividendos pagos nos últimos 12 meses/Preço da ação
  \n(Dividendos pagos nos últimos 12 meses/Qtd ações)/Preço da ação
""")
st.subheader("ROE")
st.write("""
  Da sigla em inglês, Return on equity, é um indicador que mede o desempenho de uma empresa e mostra se ela está gerando benefícios aos seus acionistas. Além disso, o ROE mede a capacidade de uma empresa em agregar valor a ela mesma usando recursos próprios, gerando crescimento apenas com os recursos já disponíveis. Sendo assim, esse é um indicador que mede a eficiêcia da gestão.
  \nÉ um valor percentual
  \nCálculo:
  Lucro líquido/Patrimônio líquido
""")

st.header("Técnicas de quem sabe mais!", divider= True)

st.subheader("Primo Rico")
st.write("""
  1- Preço (P/L, PVP, DY)
  \n2- Lucratividade (ROE)
  \n3- Endividamento (Dívida líquida/EBTIDA)
  \n4- Crescimento (CAGR Lucro, compound anual growth rate)
  \n5- Governança corporativa (Resolução CVM 44)
  \n
  Nem todos os indicadores são recomendados para serem utilizados em todos os setores de empresas. Alguns setores naturalmente terão alguns indicadores maiores ou menores devido ao seu ramo de atuação, como empresas de tecnologia por exemplo que possuem poucos ativos em circulação, dificultando o cálculo do retorno sobre valor patrimonial por exemplo.
""")

st.header("Ramiro Gomes (Clube do Valor)")