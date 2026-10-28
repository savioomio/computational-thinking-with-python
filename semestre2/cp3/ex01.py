# Exercício 1 – Montando um DataFrame com zip
import pandas as pd

produtos = ["Cabo HDMI", "Hub USB", "Mousepad", "Suporte Notebook"]
precos   = [39.9, 129.0, 25.5, 189.9]
estoques = [120, 35, 300, 18]

# zip junta as listas "lado a lado": 1º com 1º, 2º com 2º...
tuplas = list(zip(produtos, precos, estoques))
print(tuplas)

fornecedor = pd.DataFrame(tuplas, columns=["produto", "preco", "estoque"])
print(fornecedor)
