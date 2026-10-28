# Exercício 10 – Limpando texto com apply + lambda
import pandas as pd
from base import carregar_vendas

vendas = carregar_vendas()

cadastro = pd.DataFrame({
    "cliente_bruto": ["  ana souza", "BRUNO LIMA ", "carla   dias", "Diego rocha", " elisa PRADO"]
})

# nome.split()  -> quebra em palavras e joga fora TODOS os espaços extras: ["carla", "dias"]
# " ".join(...) -> junta as palavras de volta com 1 espaço só: "carla dias"
# .title()      -> primeira letra de cada palavra maiúscula: "Carla Dias"
cadastro["cliente"] = cadastro["cliente_bruto"].apply(lambda nome: " ".join(nome.split()).title())
print(cadastro)

# confere se todos os nomes limpos existem em vendas
clientes_vendas = list(vendas["cliente"])
todos_existem = True
for nome in cadastro["cliente"]:
    if nome not in clientes_vendas:
        todos_existem = False
print(todos_existem)
