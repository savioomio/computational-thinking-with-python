import pandas as pd

# dicionario = {
#     'chave1': ['valor1', 'valor2', 'valor3'],
#     'chave2': ['valor4', 'valor5', 'valor6'],
#     'chave3': [12, 12, [12, 10, 40]]
# }

# df = pd.DataFrame(dicionario)

# print(df)

produto = dict(nome='Caneta', estoque=100, preco=1.99)

data = pd.DataFrame([produto])

print(data)

produto.update({'title': 'Caneta top de linha', 'description': 'Caneta de escritório'})
data = pd.DataFrame([produto])
print(data)

del produto['estoque']
data = pd.DataFrame([produto])
print(data)