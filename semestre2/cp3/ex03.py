# Exercício 3 – Classificação com for + if
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total()

niveis = []
for total in vendas["total"]:
    if total >= 3000:
        niveis.append("Alto")
    else:
        niveis.append("Baixo")

vendas["nivel"] = niveis
print(vendas[["pedido", "total", "nivel"]])

qtd_alto = (vendas["nivel"] == "Alto").sum()
print(f"Pedidos 'Alto': {qtd_alto}")
