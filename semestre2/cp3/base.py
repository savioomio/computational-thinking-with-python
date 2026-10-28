# DataFrame base usado em todos os exercícios da lista CP3
import pandas as pd


def carregar_vendas():
    """Devolve o DataFrame base da lista (12 pedidos)."""
    return pd.DataFrame({
        "pedido":    [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012],
        "data":      pd.to_datetime(["2026-09-01", "2026-09-02", "2026-09-03", "2026-09-05",
                                     "2026-09-06", "2026-09-08", "2026-09-10", "2026-09-11",
                                     "2026-09-13", "2026-09-15", "2026-09-18", "2026-09-20"]),
        "cliente":   ["Ana Souza", "Bruno Lima", "Carla Dias", "Ana Souza", "Diego Rocha", "Bruno Lima",
                      "Carla Dias", "Elisa Prado", "Diego Rocha", "Ana Souza", "Elisa Prado", "Bruno Lima"],
        "produto":   ["Notebook", "Mouse", "Monitor", "Teclado", "Notebook", "Webcam",
                      "Headset", "Impressora", "Monitor", "Mouse", "SSD", "Teclado"],
        "categoria": ["Informatica", "Acessorio", "Informatica", "Acessorio", "Informatica", "Acessorio",
                      "Acessorio", "Informatica", "Informatica", "Acessorio", "Informatica", "Acessorio"],
        "regiao":    ["SP", "RJ", "SP", "MG", "RJ", "SP", "MG", "SP", "RJ", "MG", "SP", "RJ"],
        "preco":     [4200.0, 89.9, 1350.0, 210.0, 3990.0, 149.9, 320.0, 980.0, 1290.0, 95.0, 450.0, 199.0],
        "qtd":       [2, 10, 3, 5, 1, 4, 2, 1, 2, 6, 3, 4],
    })


def carregar_vendas_com_total():
    """DataFrame base já com a coluna total (criada no Exercício 2)."""
    vendas = carregar_vendas()
    vendas["total"] = vendas["preco"] * vendas["qtd"]
    return vendas
