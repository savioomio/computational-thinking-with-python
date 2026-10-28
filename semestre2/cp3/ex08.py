# Exercício 8 – Alerta de quantidade com for + zip + if
from base import carregar_vendas

vendas = carregar_vendas()

alertas = 0
for produto, qtd, regiao in zip(vendas["produto"], vendas["qtd"], vendas["regiao"]):
    if qtd < 3:
        print(f"ATENÇÃO: {produto} ({regiao}) vendeu só {qtd} unidade(s)")
        alertas += 1

print(f"Alertas gerados: {alertas}")
