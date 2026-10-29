## O laço percorre preço e quantidade lado a lado e classifica cada pedido como "Alto" (preço × quantidade >= 1000) ou "Baixo".
## Resultado esperado na coluna classe: Alto, Baixo, Alto, Alto, Alto, Baixo.
## Resposta: zip(vendas["preco"], vendas["qtd"])

import pandas as pd

vendas = pd.DataFrame({
    "pedido":  [1001, 1002, 1003, 1004, 1005, 1006],
    "produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Notebook", "Webcam"],
    "regiao":  ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco":   [4200.0, 89.9, 1350.0, 210.0, 3990.0, 149.9],
    "qtd":     [2, 10, 3, 5, 1, 4],
})

# zip junta as duas colunas em pares (preco, qtd), um par por pedido
classes = []
for preco, qtd in zip(vendas["preco"], vendas["qtd"]):
    if preco * qtd >= 1000:
        classes.append("Alto")
    else:
        classes.append("Baixo")

vendas["classe"] = classes

print(vendas)
