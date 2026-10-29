## Crie uma coluna chamada frete: R$ 0 para pedidos de SP e R$ 25 para as demais regiões. Utilize apply e lambda.

import pandas as pd

vendas = pd.DataFrame({
    "pedido":  [1001, 1002, 1003, 1004, 1005, 1006],
    "produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Notebook", "Webcam"],
    "regiao":  ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco":   [4200.0, 89.9, 1350.0, 210.0, 3990.0, 149.9],
    "qtd":     [2, 10, 3, 5, 1, 4],
})

# apply na coluna regiao -> a lambda recebe cada valor da coluna (ex.: "SP")
vendas["frete"] = vendas["regiao"].apply(lambda regiao: 0 if regiao == "SP" else 25)

print(vendas)
