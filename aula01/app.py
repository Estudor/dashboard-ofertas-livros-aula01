"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")
col1, col2, col3, col4 = st.columns(4)

livros = dados.ler_livros()
qtd_livros = len(livros)
col1.metric("Total de Livros", qtd_livros)
col1.metric("Quantidade de livros com 5 estrelas", dados.contar_cinco_estrelas(livros))

preco_medio = dados.calcular_preco_medio(livros)
col2.metric("Preço médio", f"{preco_medio:.2f}")

mais_caro = dados.livro_mais_caro(livros)
col3.metric("Livro mais caro:", mais_caro[0], mais_caro[1])

st.dataframe(livros)