"""Leitura dos arquivos CSV do projeto.
"""


from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return livros

def ler_livros_v2():
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            print(arquivo.readline())
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)
    
def ler_livros_v1():
    arquivo = None
    try:
        arquivo = open("livros.csv", "r", encoding="utf-8")
        print(arquivo.readline())
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)
    finally:
        if arquivo is not None:
            arquivo.close()

def calcular_preco_medio(livros):
    soma: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        soma+=preco_num
        
    preco_medio: float = soma / len(livros)
    return preco_medio

def contar_cinco_estrelas(livros):
    contador: int = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if livro["nota"] == "Five":
            contador += 1
    return contador

def livro_mais_caro(livros):
    maior_preco: float = 0
    maior_livro = [0, ""]
    for livro in livros:
        if(float(livro["preco"].replace("£", "")) > maior_preco):
            maior_preco = float(livro["preco"].replace("£", ""))
            maior_livro[0] = livro["titulo"]
            maior_livro[1] = livro["preco"]
    return maior_livro



if __name__ == "__main__":
    livros = ler_livros()
    #print(f"A quantidade de livros da coleção é de {len(livros)} livros.")

    #preco_medio: float = calcular_preco_medio(livros)
    #print(f"O preço médio dos livros é de £{preco_medio:.2f}")
    print(livro_mais_caro(livros))
    #cinco_estrelas = contar_cinco_estrelas(livros)
    #print(f"A quantidade de livros com 5 estrelas é de: ", contar_cinco_estrelas(livros))