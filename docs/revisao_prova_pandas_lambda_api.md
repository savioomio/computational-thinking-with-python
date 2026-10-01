# Revisão para a Prova – Pandas, Lambda e Consumo de API

Guia rápido com o que mais costuma cair. Os exemplos rodam em
[`revisao_pratica.py`](revisao_pratica.py).

```bash
pip install pandas requests
```

---

## 1. Lambda

Função anônima de **uma expressão só** (sem `return`, sem `if/else` em bloco).

```python
nome_da_func = lambda parametros: expressao
```

```python
dobro = lambda x: x * 2
dobro(5)                          # 10

soma = lambda a, b: a + b
soma(2, 3)                        # 5

# if/else vira expressão ternária
classifica = lambda n: "Par" if n % 2 == 0 else "Ímpar"
```

### Onde lambda aparece

| Função    | O que faz                                  | Exemplo                                        |
|-----------|--------------------------------------------|------------------------------------------------|
| `map`     | aplica a função em cada item               | `list(map(lambda x: x*2, [1,2,3]))` → `[2,4,6]` |
| `filter`  | mantém só itens em que retorna `True`      | `list(filter(lambda x: x>1, [1,2,3]))` → `[2,3]` |
| `sorted`  | `key=` define o critério de ordenação      | `sorted(lista, key=lambda p: p["preco"])`      |
| `max/min` | `key=` define o critério                   | `max(lista, key=lambda p: p["preco"])`         |
| pandas    | `apply`, `assign`, `map`, `loc`            | ver seção 2                                    |

> `map` e `filter` retornam **iteradores** — envolva com `list(...)` para ver o resultado.

---

## 2. Pandas

```python
import pandas as pd
```

### 2.1 Criando DataFrames

```python
# a partir de dicionário (chave = coluna, valor = lista)
df = pd.DataFrame({
    "nome":  ["Ana", "Bruno", "Carla", "Davi"],
    "idade": [20, 35, 28, 42],
    "nota":  [8.5, 6.0, 9.2, 7.1],
})

# a partir de lista de dicionários (cada dict = uma linha)
df = pd.DataFrame([{"nome": "Ana", "idade": 20}, {"nome": "Bruno", "idade": 35}])

# a partir de arquivos
df = pd.read_csv("arquivo.csv")
df = pd.read_json("arquivo.json")
df = pd.read_excel("arquivo.xlsx")
df.to_csv("saida.csv", index=False)
```

### 2.2 Explorando

```python
df.head()        # 5 primeiras linhas (head(10) para 10)
df.tail()        # 5 últimas
df.shape         # (linhas, colunas) – atributo, sem ()
df.columns       # nomes das colunas
df.dtypes        # tipo de cada coluna
df.info()        # resumo: tipos, nulos, memória
df.describe()    # estatísticas das colunas numéricas
df["col"].unique()        # valores distintos
df["col"].value_counts()  # contagem de cada valor
```

### 2.3 Selecionando

```python
df["nome"]               # uma coluna → Series
df[["nome", "nota"]]     # várias colunas → DataFrame (colchetes duplos!)

df.loc[0]                # linha pelo RÓTULO do índice
df.loc[0, "nome"]        # linha + coluna
df.iloc[0]               # linha pela POSIÇÃO
df.iloc[0:2, 0:2]        # fatia por posição (fim exclusivo)
```

`loc` = rótulo (fim **inclusivo**) · `iloc` = posição (fim **exclusivo**).

### 2.4 Filtrando (máscara booleana)

```python
df[df["idade"] > 25]
df[(df["idade"] > 25) & (df["nota"] > 7)]    # E  → &
df[(df["idade"] < 25) | (df["nota"] > 9)]    # OU → |
df[~(df["idade"] > 25)]                      # NÃO → ~
df[df["nome"].isin(["Ana", "Carla"])]
df[df["nome"].str.startswith("A")]
df.query("idade > 25 and nota > 7")
```

> Cada condição precisa de **parênteses**, e usa `&`/`|`, **não** `and`/`or`.

### 2.5 Criando e alterando colunas

```python
df["nota_final"] = df["nota"] * 1.1              # operação vetorizada
df["maior_idade"] = df["idade"] >= 18
df = df.rename(columns={"nota": "media"})
df = df.drop(columns=["maior_idade"])            # drop não altera o original sem atribuir
df = df.drop(index=0)                            # remove linha
```

### 2.6 `apply` + `lambda` (o ponto mais cobrado)

```python
# Series.apply → função recebe UM valor
df["situacao"] = df["nota"].apply(lambda n: "Aprovado" if n >= 7 else "Reprovado")

# função normal também serve (como em semestre2/apply.py)
def clas(a):
    if a < 30:
        return "Baixo"
    elif a < 40:
        return "Médio"
    return "Alto"

df["faixa"] = df["idade"].apply(clas)

# DataFrame.apply com axis=1 → função recebe a LINHA inteira
df["resumo"] = df.apply(lambda linha: f"{linha['nome']} ({linha['idade']})", axis=1)

# assign: cria coluna sem mutar o df original (encadeável)
df2 = df.assign(nota_10=lambda d: d["nota"] * 10)

# map: valor → valor (aceita dict)
df["sigla"] = df["situacao"].map({"Aprovado": "A", "Reprovado": "R"})
```

| Quero…                          | Use                          |
|---------------------------------|------------------------------|
| transformar cada valor da coluna| `df["col"].apply(lambda x: …)` |
| usar várias colunas da linha    | `df.apply(lambda l: …, axis=1)` |
| trocar valores por um dicionário| `df["col"].map({...})`       |
| operação simples (`*`, `+`)     | vetorizado: `df["a"] * 2` (mais rápido que apply) |

### 2.7 Ordenando

```python
df.sort_values("nota")                         # crescente
df.sort_values("nota", ascending=False)        # decrescente
df.sort_values(["idade", "nota"])              # por várias colunas
df.sort_values("nome", key=lambda s: s.str.lower())   # lambda em key
df.reset_index(drop=True)                      # refaz o índice 0..n
```

### 2.8 Agregações e `groupby`

```python
df["nota"].mean()    # média
df["nota"].sum()
df["nota"].max()
df["nota"].min()
df["nota"].count()   # ignora NaN

df.groupby("situacao")["nota"].mean()
df.groupby("situacao").agg({"nota": ["mean", "max"], "idade": "min"})
df.groupby("situacao").size()                  # contagem por grupo
df.groupby("situacao")["nota"].agg(lambda s: s.max() - s.min())   # lambda no agg
```

### 2.9 Valores nulos

```python
df.isnull().sum()            # nulos por coluna
df.dropna()                  # remove linhas com NaN
df.fillna(0)                 # preenche tudo com 0
df["nota"].fillna(df["nota"].mean())   # preenche com a média
```

### 2.10 Juntando DataFrames

```python
pd.concat([df1, df2], ignore_index=True)       # empilha linhas
df1.merge(df2, on="id", how="left")            # join (inner, left, right, outer)
```

---

## 3. Consumo de API

API REST = você faz uma **requisição HTTP** para uma URL e recebe uma
**resposta**, normalmente em JSON.

```python
import requests
```

### 3.1 Métodos HTTP

| Método   | Para quê          |
|----------|-------------------|
| `GET`    | buscar dados      |
| `POST`   | criar             |
| `PUT`/`PATCH` | atualizar    |
| `DELETE` | remover           |

### 3.2 Status codes

| Código | Significado                |
|--------|----------------------------|
| 200    | OK                         |
| 201    | Criado (POST)              |
| 400    | Requisição inválida        |
| 401/403| Não autenticado / proibido |
| 404    | Não encontrado             |
| 500    | Erro no servidor           |

### 3.3 GET básico

```python
url = "https://jsonplaceholder.typicode.com/posts"
resp = requests.get(url, timeout=10)

resp.status_code      # 200
resp.ok               # True se status < 400
resp.json()           # converte o corpo JSON → list/dict Python
resp.text             # corpo como string
resp.headers          # cabeçalhos
```

Sempre use `timeout` e trate erros:

```python
try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()          # levanta exceção se 4xx/5xx
    dados = resp.json()
except requests.exceptions.HTTPError as e:
    print("Erro HTTP:", e)
except requests.exceptions.ConnectionError:
    print("Sem conexão")
except requests.exceptions.Timeout:
    print("Demorou demais")
```

### 3.4 Parâmetros de query (`?chave=valor`)

```python
resp = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 1},            # vira ?postId=1
    timeout=10,
)
```

### 3.5 POST com JSON e headers

```python
payload = {"title": "Oi", "body": "texto", "userId": 1}
resp = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload,                    # serializa e põe Content-Type: application/json
    headers={"Authorization": "Bearer SEU_TOKEN"},
    timeout=10,
)
resp.status_code   # 201
```

### 3.6 Lendo o JSON

`.json()` devolve dicionários/listas — navegue com `[]`:

```python
usuario = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10).json()
usuario["name"]
usuario["address"]["city"]          # JSON aninhado = dict dentro de dict
usuario.get("phone", "sem telefone")  # .get evita KeyError
```

### 3.7 API → Pandas (a combinação que costuma cair)

```python
dados = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10).json()

df = pd.DataFrame(dados)                        # lista de dicts → DataFrame

# JSON aninhado → colunas planas (address.city, company.name, ...)
df = pd.json_normalize(dados)

df["cidade"] = df["address.city"]
df["dominio"] = df["email"].apply(lambda e: e.split("@")[1])
```

---

## 4. Exemplo completo (resumo da prova em 10 linhas)

```python
import requests
import pandas as pd

resp = requests.get("https://jsonplaceholder.typicode.com/todos", timeout=10)
resp.raise_for_status()

df = pd.DataFrame(resp.json())
df["status"] = df["completed"].apply(lambda c: "Feito" if c else "Pendente")

print(df.groupby("userId")["completed"].mean().sort_values(ascending=False).head())
```

---

## 5. Pegadinhas clássicas

- `df[["a", "b"]]` (colchetes **duplos**) para várias colunas; `df["a", "b"]` dá erro.
- Filtro combinado: `&` / `|` com **parênteses** — não `and` / `or`.
- `df.drop(...)`, `df.sort_values(...)`, `df.fillna(...)` **retornam um novo df**; atribua o resultado (ou use `inplace=True`).
- `df.shape` e `df.columns` são atributos (sem parênteses); `df.head()` e `df.info()` são métodos.
- `apply` em Series recebe **um valor**; `apply(axis=1)` em DataFrame recebe **uma linha**.
- `lambda` aceita só **uma expressão**: `lambda x: "A" if x > 5 else "B"` ✔ · `lambda x: if x > 5: ...` ✘.
- `map()`/`filter()` do Python precisam de `list(...)` para exibir.
- `resp.json()` é **método** (com parênteses); `resp.status_code` é atributo.
- `resp.status_code == 200` não levanta erro sozinho — use `raise_for_status()`.
- `params=` → query string; `json=` → corpo da requisição; `headers=` → cabeçalhos.
- `loc` fim inclusivo, `iloc` fim exclusivo.

---

## 6. Exercícios para treinar

1. Dado `df` com colunas `produto`, `preco`, `qtd`: crie a coluna `total = preco * qtd`.
2. Filtre os produtos com `total > 100` **e** `qtd < 10`, ordenados por `total` decrescente.
3. Crie a coluna `categoria` com `apply` + `lambda`: `"Caro"` se `preco > 50`, senão `"Barato"`.
4. Use `groupby("categoria")` para obter a soma de `total` por categoria.
5. Com `filter` + `lambda`, pegue só os números pares de `[1..20]`; com `map`, eleve-os ao quadrado.
6. Consuma `https://jsonplaceholder.typicode.com/users`, monte um DataFrame só com `name`, `email` e `city` (use `json_normalize`).
7. Consuma `/posts`, conte quantos posts cada `userId` tem (`value_counts` ou `groupby`).
8. Faça um `POST` em `/posts` com um JSON seu e imprima o status code (deve ser 201).

Gabarito em [`revisao_pratica.py`](revisao_pratica.py).
