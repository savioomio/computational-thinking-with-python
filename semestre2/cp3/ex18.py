# Exercício 18 – Comparando duas colunas com zip (subiu, caiu ou igual)
import pandas as pd

custos = pd.DataFrame({
    "produto":      ["Notebook", "Mouse", "Monitor", "Teclado", "Webcam", "Headset", "Impressora", "SSD"],
    "custo_antigo": [3100.0, 45.0, 900.0, 120.0, 80.0, 190.0, 610.0, 280.0],
    "custo_novo":   [3250.0, 45.0, 870.0, 135.0, 80.0, 175.0, 655.0, 260.0],
})

situacao = []
for antigo, novo in zip(custos["custo_antigo"], custos["custo_novo"]):
    if novo > antigo:
        situacao.append("subiu")
    elif novo < antigo:
        situacao.append("caiu")
    else:
        situacao.append("igual")
custos["situacao"] = situacao

custos["variacao_pct"] = custos.apply(
    lambda l: round((l["custo_novo"] - l["custo_antigo"]) / l["custo_antigo"] * 100, 1),
    axis=1,
)

print(custos)
print(custos["situacao"].value_counts())
