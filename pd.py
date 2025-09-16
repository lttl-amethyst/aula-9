import streamlit as st
import pandas as pd

st.title("Controle de Vendas")

dados = {
    "Produto": ["Caneta", "Caderno", "Borracha", "Caneta", "Caderno", "Caneta"],
    "Quantidade": [10, 5, 8, 3, 6, 12],
    "Preço_Unitário": [2.5, 15.0, 1.5, 2.5, 15.0, 2.5]
}

df = pd.DataFrame(dados)
df["Valor_Total"] = df["Quantidade"] * df["Preço_Unitário"]

st.subheader("Dados de Vendas")
st.dataframe(df)

st.subheader("Total vendido por produto")
resumo = df.groupby("Produto")["Valor_Total"].sum().reset_index()
st.bar_chart(resumo.set_index("Produto"))

st.subheader("Carregar arquivo de vendas")
uploaded_file = st.file_uploader("Escolha um arquivo CSV ou Excel", type=["CSV", "XLSX"])

if uploaded_file:
    if uploaded_file.name.endswith(".CSV"):
        df_upload = pd.read_csv(uploaded_file)
    else:
        df_upload = pd.read_excel(uploaded_file)

    st.write("Arquivo carregado com sucesso: ")
    st.dataframe(df_upload)