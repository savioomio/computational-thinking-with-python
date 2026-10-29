## Pedidos de SP recebem 10% de desconto sobre o total; os demais recebem 0.
## Resultado esperado na coluna desconto: 840.0, 0, 405.0, 0, 0, 59.96.

import pandas as pd

vendas = pd.DataFrame({
    "pedido":  [1001, 1002, 1003, 1004, 1005, 1006],
    "produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Notebook", "Webcam"],
    "regiao":  ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco":   [4200.0, 89.9, 1350.0, 210.0, 3990.0, 149.9],
    "qtd":     [2, 10, 3, 5, 1, 4],
})
vendas["total"] = vendas["preco"] * vendas["qtd"]

descontos = []
for regiao, total in zip(vendas["regiao"], vendas["total"]):
    if regiao == "SP":
        descontos.append(round(total * 0.10, 2))
    else:
        descontos.append(0)

vendas["desconto"] = descontos

print(vendas)
