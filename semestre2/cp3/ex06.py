# Exercício 6 – Regra com duas colunas: apply(axis=1) + lambda
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total()

# axis=1 -> a lambda recebe a LINHA inteira, e acessa as colunas com linha["coluna"]
vendas["desconto"] = vendas.apply(
    lambda linha: linha["total"] * 0.10
    if linha["categoria"] == "Informatica" and linha["qtd"] >= 2
    else 0,
    axis=1,
)
vendas["total_final"] = vendas["total"] - vendas["desconto"]

com_desconto = vendas[vendas["desconto"] > 0]
print(com_desconto[["pedido", "produto", "qtd", "total", "desconto", "total_final"]])
print(f"Total de descontos: R$ {vendas['desconto'].sum():.2f}")
