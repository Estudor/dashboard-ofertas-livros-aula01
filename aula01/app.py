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

mais_caro = dados.livro_mais_caro(livros)
st.metric("Livro mais caro:", mais_caro[0], mais_caro[1])

st.metric("Quantidade de livros com 5 estrelas", dados.contar_cinco_estrelas(livros))
st.dataframe(livros)