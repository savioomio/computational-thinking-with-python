# Exercício 17 – Acumulador com for + break
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total().sort_values("data")

acumulado = 0
for data, pedido, total in zip(vendas["data"], vendas["pedido"], vendas["total"]):
    acumulado += total
    print(f"{data.date()} | pedido {pedido} | acumulado R$ {acumulado:.2f}")
    if acumulado >= 20000:
        print(f"Marca de R$ 20000 atingida em {data.date()} com o pedido {pedido}")
        break
