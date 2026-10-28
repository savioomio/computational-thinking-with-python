# Exercício 15 – Gerando textos com apply(axis=1) + lambda
from base import carregar_vendas

vendas = carregar_vendas()

# o if/else escolhe entre duas frases: com "x" ou sem "x" (quando qtd é 1)
vendas["resumo"] = vendas.apply(
    lambda l: f"{l['cliente']} comprou 1 {l['produto']} em {l['regiao']}"
    if l["qtd"] == 1
    else f"{l['cliente']} comprou {l['qtd']}x {l['produto']} em {l['regiao']}",
    axis=1,
)

print(vendas["resumo"].head(4))
print(vendas["resumo"][4])  # pedido 1005
