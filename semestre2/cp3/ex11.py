# Exercício 11 – Condição vetorizada: máscaras com &, | e ~
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total()
colunas = ["pedido", "produto", "regiao", "categoria", "qtd", "total"]

# & = e, | = ou, ~ = não. Cada condição SEMPRE entre parênteses.
r1 = vendas[(vendas["regiao"] == "SP") & (vendas["total"] > 1000)]
print("1) SP e total > 1000")
print(r1[colunas])

r2 = vendas[(vendas["regiao"] == "RJ") | (vendas["categoria"] == "Acessorio")]
print(f"\n2) RJ ou Acessorio -> {len(r2)} pedidos")
print(r2[colunas])

r3 = vendas[~(vendas["categoria"] == "Informatica") & (vendas["qtd"] >= 5)]
print("\n3) Não Informatica e qtd >= 5")
print(r3[colunas])
