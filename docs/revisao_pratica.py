"""Gabarito/prática da revisão: lambda, pandas e consumo de API.

Rode com: python docs/revisao_pratica.py
(as partes de API precisam de internet)
"""
import pandas as pd
import requests

URL = "https://jsonplaceholder.typicode.com"


# ---------------------------------------------------------------- Lambda
print("=== Lambda ===")
dobro = lambda x: x * 2
classifica = lambda n: "Par" if n % 2 == 0 else "Ímpar"
print(dobro(5), classifica(7))

numeros = list(range(1, 21))
pares = list(filter(lambda n: n % 2 == 0, numeros))
quadrados = list(map(lambda n: n ** 2, pares))
print(pares)
print(quadrados)

produtos_lista = [{"nome": "Caneta", "preco": 2.0}, {"nome": "Mochila", "preco": 90.0}]
print(sorted(produtos_lista, key=lambda p: p["preco"], reverse=True))
print(max(produtos_lista, key=lambda p: p["preco"])["nome"])


# ---------------------------------------------------------------- Pandas
print("\n=== Pandas ===")
df = pd.DataFrame({
    "produto": ["Caneta", "Caderno", "Mochila", "Lápis", "Estojo"],
    "preco":   [2.5, 18.0, 90.0, 1.5, 55.0],
    "qtd":     [100, 20, 5, 200, 8],
})

# 1. coluna calculada (vetorizado)
df["total"] = df["preco"] * df["qtd"]

# 2. filtro combinado + ordenação
filtrado = df[(df["total"] > 100) & (df["qtd"] < 10)].sort_values("total", ascending=False)
print(filtrado)

# 3. apply + lambda
df["categoria"] = df["preco"].apply(lambda p: "Caro" if p > 50 else "Barato")

# 4. groupby
print(df.groupby("categoria")["total"].sum())
print(df.groupby("categoria").agg({"total": ["sum", "mean"], "qtd": "max"}))

# apply por linha (axis=1)
df["resumo"] = df.apply(lambda l: f"{l['produto']}: R$ {l['total']:.2f}", axis=1)
print(df[["produto", "categoria", "resumo"]])

# loc x iloc
print(df.loc[0, "produto"], df.iloc[0, 0])

# nulos
df_nulos = pd.DataFrame({"nota": [8.0, None, 6.0]})
print(df_nulos["nota"].fillna(df_nulos["nota"].mean()))


# ------------------------------------------------------------------- POO
print("\n=== POO ===")


class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def total(self):
        return self.preco * self.qtd

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f} x {self.qtd})"


class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, qtd, validade):
        super().__init__(nome, preco, qtd)
        self.validade = validade

    def __str__(self):
        return f"{super().__str__()} - vence em {self.validade}"


itens = [
    Produto("Caneta", 2.5, 100),
    Produto("Mochila", 90.0, 5),
    ProdutoPerecivel("Leite", 5.0, 30, "2026-12-01"),
]
for item in itens:
    print(item)  # polimorfismo: cada classe usa o seu __str__

df_obj = pd.DataFrame([i.__dict__ for i in itens])
df_obj["total"] = [i.total() for i in itens]
print(df_obj)


# ------------------------------------------------------------------- API
print("\n=== API ===")
try:
    # 6. usuários → DataFrame plano
    resp = requests.get(f"{URL}/users", timeout=10)
    resp.raise_for_status()
    users = pd.json_normalize(resp.json())
    users = users[["name", "email", "address.city"]].rename(columns={"address.city": "city"})
    users["dominio"] = users["email"].apply(lambda e: e.split("@")[1])
    print(users.head())

    # 7. posts por usuário
    posts = pd.DataFrame(requests.get(f"{URL}/posts", timeout=10).json())
    print(posts["userId"].value_counts().sort_index())

    # query params
    comentarios = requests.get(f"{URL}/comments", params={"postId": 1}, timeout=10).json()
    print(len(comentarios), "comentários no post 1")

    # 8. POST com JSON
    resp = requests.post(
        f"{URL}/posts",
        json={"title": "Revisão", "body": "Treinando API", "userId": 1},
        timeout=10,
    )
    print("POST →", resp.status_code)  # 201

except requests.exceptions.HTTPError as e:
    print("Erro HTTP:", e)
except requests.exceptions.ConnectionError:
    print("Sem conexão")
except requests.exceptions.Timeout:
    print("Demorou demais")
