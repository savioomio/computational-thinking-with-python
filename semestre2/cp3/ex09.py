# Exercício 9 – Contador manual x value_counts
from base import carregar_vendas

vendas = carregar_vendas()

contagem = {}
for regiao in vendas["regiao"]:
    if regiao not in contagem:
        contagem[regiao] = 1
    else:
        contagem[regiao] += 1

print(contagem)
print(vendas["regiao"].value_counts())
