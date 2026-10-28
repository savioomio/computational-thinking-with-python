# Exercício 4 – A mesma regra com apply + lambda
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total()

# nivel (do Exercício 3) feito com for
niveis = []
for total in vendas["total"]:
    if total >= 3000:
        niveis.append("Alto")
    else:
        niveis.append("Baixo")
vendas["nivel"] = niveis

# nivel2: mesma regra, sem for
vendas["nivel2"] = vendas["total"].apply(lambda t: "Alto" if t >= 3000 else "Baixo")

# transforma as duas colunas em lista e compara
print(list(vendas["nivel"]) == list(vendas["nivel2"]))
