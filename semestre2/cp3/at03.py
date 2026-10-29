## A empresa tem uma meta de R$ 15.000 em vendas. Escreva um código que some os totais dos pedidos, um a um,
## na ordem em que aparecem, e descubra em qual pedido a soma chegou à meta.

import pandas as pd

vendas = pd.DataFrame({
    "pedido":  [1001, 1002, 1003, 1004, 1005, 1006],
    "produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Notebook", "Webcam"],
    "regiao":  ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco":   [4200.0, 89.9, 1350.0, 210.0, 3990.0, 149.9],
    "qtd":     [2, 10, 3, 5, 1, 4],
})
vendas["total"] = vendas["preco"] * vendas["qtd"]

meta = 15000
acumulado = 0

for pedido, total in zip(vendas["pedido"], vendas["total"]):
    acumulado += total
    print(f"Pedido {pedido}: +R$ {total:.2f}, acumulado R$ {acumulado:.2f}")
    if acumulado >= meta:
        print(f"A meta R${meta} foi atingida no pedido {pedido}.")
        break
