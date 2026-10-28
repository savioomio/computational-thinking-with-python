# Exercício 16 – Função com parâmetros extras no apply
from base import carregar_vendas

vendas = carregar_vendas()


def reajustar(preco, categoria, pct_info, pct_acess):
    if categoria == "Informatica":
        pct = pct_info
    else:
        pct = pct_acess
    return round(preco * (1 + pct / 100), 2)


# a lambda pega a linha e repassa os valores + os percentuais fixos para a função
vendas["preco_novo"] = vendas.apply(
    lambda l: reajustar(l["preco"], l["categoria"], 5, 8), axis=1
)

# mostra cada produto uma vez só
ja_mostrados = []
for produto, categoria, preco, preco_novo in zip(
    vendas["produto"], vendas["categoria"], vendas["preco"], vendas["preco_novo"]
):
    if produto not in ja_mostrados:
        print(f"{produto} ({categoria}): R$ {preco:.2f} -> R$ {preco_novo:.2f}")
        ja_mostrados.append(produto)
