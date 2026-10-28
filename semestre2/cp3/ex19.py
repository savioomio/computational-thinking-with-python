# Exercício 19 – Análise por categoria
import pandas as pd
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total()

categorias = []
amplitudes = []
pcts = []

for categoria in ["Acessorio", "Informatica"]:
    # filtra só as linhas daquela categoria
    grupo = vendas[vendas["categoria"] == categoria]

    amplitude = grupo["total"].max() - grupo["total"].min()

    acima = grupo[grupo["total"] > 1000]
    pct = round(len(acima) / len(grupo) * 100, 1)

    categorias.append(categoria)
    amplitudes.append(amplitude)
    pcts.append(pct)

analise = pd.DataFrame({
    "categoria": categorias,
    "amplitude": amplitudes,
    "pct_acima_1000": pcts,
})
analise["perfil"] = analise["pct_acima_1000"].apply(
    lambda p: "ticket alto" if p > 50 else "ticket baixo"
)

print(analise)
