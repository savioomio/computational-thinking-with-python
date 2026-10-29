## Agora mostre como calcular o preço total para cada produto, considerando preço e quantidade. Utilize lambda e apply para fazer isso.

import pandas as pd

vendas = pd.DataFrame({
    "pedido":  [1001, 1002, 1003, 1004, 1005, 1006],
    "produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Notebook", "Webcam"],
    "regiao":  ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco":   [4200.0, 89.9, 1350.0, 210.0, 3990.0, 149.9],
    "qtd":     [2, 10, 3, 5, 1, 4],
})

# axis=1 -> a lambda recebe cada LINHA do DataFrame
vendas["total"] = vendas.apply(lambda linha: linha["preco"] * linha["qtd"], axis=1)

print(vendas)
