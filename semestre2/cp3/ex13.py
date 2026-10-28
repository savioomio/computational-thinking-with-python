# Exercício 13 – Ranking Top 5
from base import carregar_vendas_com_total

vendas = carregar_vendas_com_total()

top5 = vendas.sort_values("total", ascending=False).head(5)

posicao = 1
for cliente, produto, total in zip(top5["cliente"], top5["produto"], top5["total"]):
    if posicao == 1:
        medalha = "🥇"
    elif posicao == 2:
        medalha = "🥈"
    elif posicao == 3:
        medalha = "🥉"
    else:
        medalha = ""
    print(f"{posicao}º {cliente} - {produto} - R$ {total:.2f} {medalha}")
    posicao += 1
