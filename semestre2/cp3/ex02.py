# Exercício 2 – Coluna calculada e for linha a linha
from base import carregar_vendas

vendas = carregar_vendas()

# vetorizado: multiplica a coluna inteira de uma vez, sem laço
vendas["total"] = vendas["preco"] * vendas["qtd"]

for pedido, total in zip(vendas["pedido"], vendas["total"]):
    print(f"Pedido {pedido}: R$ {total:.2f}")
