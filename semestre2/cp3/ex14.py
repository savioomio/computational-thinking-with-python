# Exercício 14 – Frete com for + zip + condição
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total()

frete_tabela = {"SP": 25.0, "RJ": 35.0, "MG": 40.0}

fretes = []
for regiao, total in zip(vendas["regiao"], vendas["total"]):
    if total >= 2000:
        fretes.append(0)
    else:
        fretes.append(frete_tabela[regiao])
vendas["frete"] = fretes

print(vendas[["pedido", "regiao", "total", "frete"]])

gratis = 0
for frete in vendas["frete"]:
    if frete == 0:
        gratis += 1
print(f"Pedidos com frete grátis: {gratis}")
