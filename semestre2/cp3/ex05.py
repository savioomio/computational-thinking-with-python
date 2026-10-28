# Exercício 5 – if/elif/else dentro de uma função usada no apply
from base import carregar_vendas

vendas = carregar_vendas()


def faixa_preco(preco):
    if preco < 200:
        return "Barato"
    elif preco < 1000:
        return "Médio"
    else:
        return "Caro"


# passa a função SEM parênteses: o apply chama ela para cada valor
vendas["faixa"] = vendas["preco"].apply(faixa_preco)
print(vendas["faixa"].value_counts())
