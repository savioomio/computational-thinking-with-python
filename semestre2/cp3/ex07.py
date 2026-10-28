# Exercício 7 – Dicionário com zip e mapeamento de colunas
from base import carregar_vendas

vendas = carregar_vendas()

regioes = ["SP", "RJ", "MG"]
metas   = [15000, 12000, 5000]

# monta o dicionário: cada região vira chave e a meta vira o valor
meta_por_regiao = {}
for regiao, meta in zip(regioes, metas):
    meta_por_regiao[regiao] = meta
print(meta_por_regiao)

# map troca cada valor da coluna pelo valor correspondente no dicionário
vendas["meta_regiao"] = vendas["regiao"].map(meta_por_regiao)
print(vendas[["pedido", "regiao", "meta_regiao"]].head())
