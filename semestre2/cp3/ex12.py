# Exercício 12 – for por região com if (meta batida?)
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total()

meta_por_regiao = {}
for regiao, meta in zip(["SP", "RJ", "MG"], [15000, 12000, 5000]):
    meta_por_regiao[regiao] = meta

for regiao, meta in meta_por_regiao.items():
    # filtra só as linhas daquela região e soma o total
    grupo = vendas[vendas["regiao"] == regiao]
    faturamento = grupo["total"].sum()

    if faturamento >= meta:
        situacao = "META BATIDA"
    else:
        situacao = f"abaixo da meta (faltam R$ {meta - faturamento:.2f})"
    print(f"{regiao}: R$ {faturamento:.2f} / meta R$ {meta} -> {situacao}")
