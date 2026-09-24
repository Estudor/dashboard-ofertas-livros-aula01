"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")

livros = dados.ler_livros()
qtd_livros = len(livros)
st.metric("Total de Livros", qtd_livros)

preco_medio = dados.calcular_preco_medio(livros)
st.metric("Preço médio", f"{preco_medio:.2f}")

st.dataframe(livros)