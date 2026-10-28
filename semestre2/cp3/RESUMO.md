# Resumo para a prova CP3 – DataFrame, for, if, apply, lambda e zip

Cada exercício está em `exNN.py`. O DataFrame `vendas` vem de `base.py`.
Para rodar: `python ex06.py` (de dentro desta pasta).

Tudo aqui é o que vimos nas aulas (Aula 09, 10, 11, revisão CP3, `apply.py`, `aula3.py`).

---

## 1. DataFrame – o básico

```python
import pandas as pd

df = pd.DataFrame({
    "nome":  ["Ana", "Bruno"],
    "preco": [10.0, 20.0],
    "qtd":   [2, 3],
})

df["total"] = df["preco"] * df["qtd"]   # coluna calculada (sem for)
df[["nome", "total"]]                   # várias colunas -> colchete DUPLO
df.head(5)                              # 5 primeiras linhas
df.sort_values("total", ascending=False)  # ordena do maior pro menor
df["regiao"].value_counts()             # conta quantas vezes cada valor aparece
df["total"].sum() / .max() / .min()     # soma, maior, menor
len(df)                                 # quantidade de linhas
```

**Filtro simples** (pega só as linhas que atendem):
```python
sp = df[df["regiao"] == "SP"]
caros = df[df["total"] > 1000]
```

---

## 2. `for` + `zip` – percorrer várias colunas juntas

`zip` junta "lado a lado": 1º com 1º, 2º com 2º...

```python
for nome, idade in zip(nomes, idades):
    if idade > 30:
        print(nome)
```

> Quantas variáveis no `for` = quantas colunas dentro do `zip`.

---

## 3. Os padrões de `for` que mais caem

**a) Lista + append → vira coluna** (Aula 11 / revisão CP3 – É O MAIS COBRADO)
```python
status = []
for venda, meta in zip(df["vendas"], df["meta"]):
    if venda >= meta:
        status.append("Meta atingida")
    else:
        status.append("Abaixo da meta")
df["status"] = status
```
Com mais de uma condição: `if ... and ...:` / `elif ...:` / `else:`

**b) Contador** (ex08, ex14)
```python
contador = 0
for qtd in df["qtd"]:
    if qtd < 3:
        contador += 1
print(contador)
```

**c) Contador em dicionário** (ex09)
```python
contagem = {}
for r in df["regiao"]:
    if r not in contagem:
        contagem[r] = 1
    else:
        contagem[r] += 1
```

**d) Montar dicionário com zip** (ex07)
```python
meta_por_regiao = {}
for regiao, meta in zip(regioes, metas):
    meta_por_regiao[regiao] = meta

for chave, valor in meta_por_regiao.items():   # percorrer dicionário
    print(chave, valor)
```

**e) Acumulador + `break`** (ex17) – soma até chegar no valor e para.
```python
acumulado = 0
for total in df["total"]:
    acumulado += total
    if acumulado >= 20000:
        break
```

**f) Contar posição** (ex13) – variável que aumenta a cada volta.
```python
posicao = 1
for nome in df["nome"]:
    print(f"{posicao}º {nome}")
    posicao += 1
```

**g) Repetir para cada grupo** (ex12, ex19) – filtra e calcula.
```python
for regiao in ["SP", "RJ", "MG"]:
    grupo = df[df["regiao"] == regiao]
    print(regiao, grupo["total"].sum())
```

---

## 4. `def` + `apply` – função com if/elif/else (`apply.py`, Aula 10)

```python
def faixa_preco(preco):
    if preco < 200:
        return "Barato"
    elif preco < 1000:
        return "Médio"
    else:
        return "Caro"

df["faixa"] = df["preco"].apply(faixa_preco)   # SEM parênteses na função!
```

---

## 5. `lambda` – função de uma linha

```python
lambda t: "Alto" if t >= 3000 else "Baixo"
```
Formato: **`valor_se_sim if condição else valor_se_não`** (o `else` é obrigatório).

```python
df["nivel"] = df["total"].apply(lambda t: "Alto" if t >= 3000 else "Baixo")
```

---

## 6. `apply` com `axis=1` – quando a regra usa 2+ colunas

| Forma | A função recebe |
|---|---|
| `df["col"].apply(f)` | **um valor** por vez |
| `df.apply(f, axis=1)` | **a linha inteira** → acessa com `linha["coluna"]` |

```python
# com lambda (Aula 09)
df["frete"] = df.apply(
    lambda linha: 0 if linha["total"] > 1000 or linha["estado"] == "SP" else 25,
    axis=1)

# com def (Aula 10)
def avaliar(linha):
    if linha["pm25"] > 50 and linha["temperatura"] > 30:
        return "Crítico"
    else:
        return "Normal"

df["risco"] = df.apply(avaliar, axis=1)
```

Dentro de lambda/def usa `and` / `or` normais.

---

## 7. Filtro com duas condições (ex11)

```python
df[(df["regiao"] == "SP") & (df["total"] > 1000)]              # E
df[(df["regiao"] == "RJ") | (df["categoria"] == "Acessorio")]  # OU
df[~(df["categoria"] == "Informatica")]                        # NÃO
```

⚠️ Aqui **não** é `and`/`or`: é `&` e `|`, e **cada condição entre parênteses**.

---

## 8. `map` com dicionário (ex07)

```python
df["meta"] = df["regiao"].map({"SP": 15000, "RJ": 12000, "MG": 5000})
```
Troca cada valor da coluna pelo valor do dicionário.

---

## 9. Textos (Aula 09)

```python
texto.strip()     # tira espaços das pontas
texto.title()     # "ana souza" -> "Ana Souza"
texto.upper()     # "sp" -> "SP"
texto.split()     # "ana souza" -> ["ana", "souza"]
" ".join(lista)   # ["ana", "souza"] -> "ana souza"
df["col"].str.strip().str.title()   # o mesmo, direto na coluna
```

**f-string:**
```python
f"R$ {valor:.2f}"   # 2 casas decimais -> R$ 8400.00
round(x, 1)         # arredondar
```

---

## 10. Fórmulas que aparecem

- Desconto de 10%: `total * 0.10`
- Aumento de p%: `preco * (1 + p / 100)`
- Variação %: `(novo - antigo) / antigo * 100`
- Porcentagem: `parte / todo * 100`
- Amplitude: `maior - menor`

---

## Checklist antes de entregar

1. Criou a coluna `total`? Quase tudo depende dela.
2. A lista do `append` foi criada **antes** do `for` (`lista = []`)?
3. A regra usa 2+ colunas? → `axis=1`.
4. Lambda tem o `else`?
5. Filtro com 2 condições: `&`/`|` e parênteses em cada uma.
6. Passou a função no `apply` **sem** `()`?
