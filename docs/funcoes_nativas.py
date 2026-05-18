# ============================================================
# GUIA COMPLETO DE FUNÇÕES NATIVAS E ÚTEIS DO PYTHON
# ============================================================
# Funções built-in (já vêm com o Python) + módulos padrão
# que vão te ajudar MUITO no dia a dia.
# ============================================================

# Built-ins (já vêm no Python):

# min, max, sum, abs, round, pow, divmod
# int, float, str, bool, list, tuple, set, dict
# type, isinstance, len, id, dir, help
# range, enumerate, zip, reversed, sorted
# all, any, map, filter
# Módulos da biblioteca padrão:

# math — pi, sqrt, floor, ceil, factorial, log, sin/cos
# random — randint, choice, choices, sample, shuffle, seed
# statistics — mean, median, mode, stdev
# datetime — now, strftime, timedelta
# os / sys — diretório, plataforma
# collections — Counter (conta ocorrências), defaultdict, deque
# string — constantes de letras/dígitos

# ============================================================
# 1. FUNÇÕES MATEMÁTICAS BÁSICAS (built-in)
# ============================================================
print("=" * 60)
print("1. FUNÇÕES MATEMÁTICAS BÁSICAS")
print("=" * 60)

# min() — menor valor
print(min(3, 7, 1, 9))              # 1
print(min([10, 20, 5, 30]))          # 5 (funciona com lista)
print(min("python"))                 # 'h' (menor letra alfabeticamente)

# max() — maior valor
print(max(3, 7, 1, 9))              # 9
print(max([10, 20, 5, 30]))          # 30

# min/max com key (critério personalizado)
nomes = ["Ana", "Bernardo", "Léo"]
print(max(nomes, key=len))           # Bernardo (mais longo)
print(min(nomes, key=len))           # Léo (mais curto)

# sum() — soma de uma lista
print(sum([1, 2, 3, 4, 5]))         # 15
print(sum([1, 2, 3], 10))           # 13 (10 é o valor inicial)

# abs() — valor absoluto (sem sinal)
print(abs(-7))                       # 7
print(abs(3.14))                     # 3.14

# round() — arredondar
print(round(3.7))                    # 4
print(round(3.14159, 2))             # 3.14 (2 casas decimais)
print(round(2.5))                    # 2 (arredondamento bancário!)

# pow() — potência
print(pow(2, 10))                    # 1024 (igual a 2 ** 10)
print(pow(2, 10, 1000))              # 24 ((2^10) % 1000)

# divmod() — retorna (quociente, resto) de uma só vez
print(divmod(17, 5))                 # (3, 2)  →  17 = 3*5 + 2


# ============================================================
# 2. MÓDULO math (matemática avançada)
# ============================================================
print("\n" + "=" * 60)
print("2. MÓDULO MATH")
print("=" * 60)

import math

print(math.pi)                       # 3.141592653589793
print(math.e)                        # 2.718281828459045
print(math.sqrt(16))                 # 4.0 (raiz quadrada)
print(math.floor(3.7))               # 3 (arredonda para baixo)
print(math.ceil(3.2))                # 4 (arredonda para cima)
print(math.trunc(3.9))               # 3 (corta a parte decimal)
print(math.factorial(5))             # 120 (5! = 5*4*3*2*1)
print(math.gcd(12, 18))              # 6 (Maior Divisor Comum)
print(math.log(100, 10))             # 2.0 (log base 10)
print(math.sin(math.pi / 2))         # 1.0 (seno de 90°)
print(math.cos(0))                   # 1.0
print(math.isnan(float("nan")))      # True (verifica se é "not a number")
print(math.inf)                      # inf (infinito)


# ============================================================
# 3. MÓDULO random (números e escolhas aleatórias)
# ============================================================
print("\n" + "=" * 60)
print("3. MÓDULO RANDOM")
print("=" * 60)

import random

# random() — float entre 0.0 e 1.0
print(random.random())               # ex: 0.7345...

# randint(a, b) — inteiro aleatório de a até b (inclusivo)
print(random.randint(1, 10))         # ex: 7

# randrange(a, b) — igual ao range (b NÃO incluso)
print(random.randrange(1, 10))       # 1 a 9
print(random.randrange(0, 100, 5))   # múltiplos de 5

# uniform(a, b) — float entre a e b
print(random.uniform(1.5, 9.9))      # ex: 4.2872...

# choice() — escolhe UM item de uma lista
frutas = ["maçã", "banana", "uva", "pera"]
print(random.choice(frutas))         # ex: 'uva'

# choices() — escolhe VÁRIOS (com repetição possível)
print(random.choices(frutas, k=3))   # ex: ['uva', 'maçã', 'uva']

# sample() — escolhe VÁRIOS SEM repetir
print(random.sample(frutas, 2))      # ex: ['banana', 'pera']

# shuffle() — embaralha a lista (modifica a original!)
baralho = [1, 2, 3, 4, 5]
random.shuffle(baralho)
print(baralho)                       # ex: [3, 1, 5, 2, 4]

# seed() — fixa a "semente" (resultados reproduzíveis)
random.seed(42)
print(random.randint(1, 100))        # sempre dará o mesmo valor com seed 42


# ============================================================
# 4. FUNÇÕES DE CONVERSÃO DE TIPO
# ============================================================
print("\n" + "=" * 60)
print("4. CONVERSÃO DE TIPOS")
print("=" * 60)

print(int("42"))                     # 42
print(int(3.99))                     # 3 (corta a parte decimal)
print(int("ff", 16))                 # 255 (hexadecimal para int)
print(int("1010", 2))                # 10 (binário para int)

print(float("3.14"))                 # 3.14
print(float(5))                      # 5.0

print(str(123))                      # "123"
print(str(3.14))                     # "3.14"

print(bool(0))                       # False
print(bool(1))                       # True
print(bool(""))                      # False (string vazia)
print(bool("oi"))                    # True
print(bool([]))                      # False (lista vazia)
print(bool([0]))                     # True (lista com 1 item)

print(list("python"))                # ['p','y','t','h','o','n']
print(tuple([1, 2, 3]))              # (1, 2, 3)
print(set([1, 1, 2, 2, 3]))          # {1, 2, 3} (remove duplicatas!)
print(dict([("a", 1), ("b", 2)]))    # {'a': 1, 'b': 2}


# ============================================================
# 5. FUNÇÕES DE INSPEÇÃO (descobrir coisas sobre objetos)
# ============================================================
print("\n" + "=" * 60)
print("5. INSPEÇÃO DE OBJETOS")
print("=" * 60)

x = [1, 2, 3]

print(type(x))                       # <class 'list'>
print(type(x) == list)               # True
print(isinstance(x, list))           # True (forma recomendada)
print(isinstance(x, (list, tuple)))  # True (pode ser várias)

print(len(x))                        # 3 (tamanho)
print(len("python"))                 # 6
print(len({"a": 1, "b": 2}))         # 2

# id() — endereço de memória do objeto
print(id(x))                         # ex: 140234567

# dir() — lista TUDO que o objeto tem (métodos e atributos)
# print(dir("texto"))                # mostra todos métodos de string

# help() — abre documentação (em terminal real)
# help(print)


# ============================================================
# 6. FUNÇÕES DE ITERAÇÃO (loops e sequências)
# ============================================================
print("\n" + "=" * 60)
print("6. ITERAÇÃO")
print("=" * 60)

# range() — gera sequência de números
print(list(range(5)))                # [0, 1, 2, 3, 4]
print(list(range(2, 8)))             # [2, 3, 4, 5, 6, 7]
print(list(range(0, 10, 2)))         # [0, 2, 4, 6, 8] (passo 2)
print(list(range(10, 0, -1)))        # contagem regressiva

# enumerate() — pega índice + valor ao mesmo tempo
for i, fruta in enumerate(["maçã", "banana", "uva"]):
    print(f"{i}: {fruta}")
# 0: maçã / 1: banana / 2: uva

# enumerate começando de outro número
for i, fruta in enumerate(["a", "b"], start=1):
    print(f"{i}: {fruta}")           # 1: a / 2: b

# zip() — combina duas listas par a par
nomes = ["Ana", "Beto", "Cris"]
idades = [20, 25, 30]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# zip transformando em dicionário
print(dict(zip(nomes, idades)))      # {'Ana': 20, 'Beto': 25, 'Cris': 30}

# reversed() — inverte
print(list(reversed([1, 2, 3])))     # [3, 2, 1]
print("".join(reversed("python")))   # 'nohtyp'

# sorted() — ordena (retorna NOVA lista, não modifica original)
print(sorted([3, 1, 4, 1, 5, 9, 2])) # [1, 1, 2, 3, 4, 5, 9]
print(sorted([3, 1, 4], reverse=True)) # [4, 3, 1]
print(sorted(["banana", "Ana"], key=str.lower))  # ignora case


# ============================================================
# 7. FUNÇÕES DE TESTE LÓGICO
# ============================================================
print("\n" + "=" * 60)
print("7. TESTES LÓGICOS")
print("=" * 60)

# all() — True se TODOS forem verdadeiros
print(all([True, True, True]))       # True
print(all([True, False, True]))      # False
print(all([1, 2, 3]))                # True (todos diferentes de 0)
print(all([]))                       # True (lista vazia!)

# Útil para validar várias condições
notas = [7, 8, 9, 6]
print(all(n >= 6 for n in notas))    # True (todos passaram)

# any() — True se PELO MENOS UM for verdadeiro
print(any([False, False, True]))     # True
print(any([0, 0, 0]))                # False
print(any([]))                       # False (lista vazia)

# Útil: existe algum negativo na lista?
print(any(n < 0 for n in [1, 2, -3, 4]))  # True


# ============================================================
# 8. FUNÇÕES DE TRANSFORMAÇÃO (map, filter)
# ============================================================
print("\n" + "=" * 60)
print("8. MAP E FILTER")
print("=" * 60)

# map() — aplica uma função em cada item
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)                     # [1, 4, 9, 16, 25]

# map com função normal
print(list(map(str, [1, 2, 3])))     # ['1', '2', '3']
print(list(map(abs, [-1, -2, 3])))   # [1, 2, 3]

# filter() — filtra itens que passam no teste
pares = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(pares)                         # [2, 4, 6]

# Equivalente com list comprehension (mais "pythônico"):
quadrados2 = [x**2 for x in numeros]
pares2 = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]


# ============================================================
# 9. STRINGS — MÉTODOS ÚTEIS
# ============================================================
print("\n" + "=" * 60)
print("9. MÉTODOS DE STRING")
print("=" * 60)

s = "  Olá, Mundo Python!  "

print(s.strip())                     # remove espaços das pontas
print(s.lstrip())                    # só da esquerda
print(s.rstrip())                    # só da direita
print(s.lower())                     # minúscula
print(s.upper())                     # MAIÚSCULA
print(s.title())                     # Primeira Letra Maiúscula
print(s.capitalize())                # Apenas a primeira de tudo
print(s.swapcase())                  # inverte maiúsc/minúsc

print("python".replace("p", "P"))    # 'Python'
print("a,b,c".split(","))            # ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))     # 'a-b-c'

print("python".startswith("py"))     # True
print("python".endswith("on"))       # True
print("python".count("o"))           # 1
print("python".find("th"))           # 2 (posição) — -1 se não achar
print("python".index("th"))          # 2 — ERRO se não achar

# Verificações de conteúdo
print("123".isdigit())               # True (só dígitos)
print("abc".isalpha())               # True (só letras)
print("abc123".isalnum())            # True (letras+números)
print("   ".isspace())               # True (só espaços)
print("Hello".istitle())             # True (formato título)

# Formatação
nome = "Sávio"
idade = 25
print(f"{nome} tem {idade} anos")    # f-string (RECOMENDADO)
print("{} tem {} anos".format(nome, idade))
print("%s tem %d anos" % (nome, idade))

# Alinhamento e preenchimento
print("abc".ljust(10, "."))          # 'abc.......'
print("abc".rjust(10, "."))          # '.......abc'
print("abc".center(10, "-"))         # '---abc----'
print("5".zfill(3))                  # '005'


# ============================================================
# 10. LISTAS — MÉTODOS ÚTEIS
# ============================================================
print("\n" + "=" * 60)
print("10. MÉTODOS DE LISTA")
print("=" * 60)

lista = [3, 1, 4, 1, 5, 9, 2, 6]

# Adicionar
lista.append(10)                     # adiciona no final
lista.insert(0, 99)                  # insere na posição 0
lista.extend([7, 8])                 # adiciona vários

# Remover
lista.remove(1)                      # remove a PRIMEIRA ocorrência de 1
ultimo = lista.pop()                 # remove e retorna o último
primeiro = lista.pop(0)              # remove e retorna o da posição 0
# del lista[0]                       # apaga por índice
# lista.clear()                      # esvazia tudo

# Buscar
print([1, 2, 3].index(2))            # 1 (posição)
print([1, 2, 2, 3].count(2))         # 2 (quantas vezes aparece)
print(2 in [1, 2, 3])                # True

# Ordenar
lista2 = [3, 1, 4, 1, 5]
lista2.sort()                        # ordena na própria lista
lista2.sort(reverse=True)            # ordem decrescente
copia_ordenada = sorted(lista2)      # retorna NOVA lista

# Inverter
lista2.reverse()

# Cópia
copia = lista2.copy()                # cópia rasa
copia2 = lista2[:]                   # mesmo efeito


# ============================================================
# 11. DICIONÁRIOS — MÉTODOS ÚTEIS
# ============================================================
print("\n" + "=" * 60)
print("11. MÉTODOS DE DICIONÁRIO")
print("=" * 60)

d = {"nome": "Sávio", "idade": 25, "cidade": "SP"}

print(d.keys())                      # dict_keys(['nome', 'idade', 'cidade'])
print(d.values())                    # dict_values(['Sávio', 25, 'SP'])
print(d.items())                     # pares (chave, valor)

# get() — pega valor SEM erro se a chave não existir
print(d.get("nome"))                 # 'Sávio'
print(d.get("telefone"))             # None
print(d.get("telefone", "N/A"))      # 'N/A' (valor padrão)

# update() — junta outro dicionário
d.update({"idade": 26, "email": "x@y.com"})

# pop() — remove e retorna o valor
idade = d.pop("idade")
# d.popitem()                        # remove o último adicionado
# d.clear()                          # esvazia

# setdefault — pega valor; se não existir, cria
d.setdefault("hobby", "ler")

# Iterando
for chave, valor in d.items():
    print(f"{chave} = {valor}")


# ============================================================
# 12. MÓDULO statistics (estatísticas)
# ============================================================
print("\n" + "=" * 60)
print("12. MÓDULO STATISTICS")
print("=" * 60)

import statistics

dados = [10, 20, 30, 40, 50]

print(statistics.mean(dados))        # 30 (média aritmética)
print(statistics.median(dados))      # 30 (mediana)
print(statistics.mode([1, 1, 2, 3])) # 1 (mais frequente)
print(statistics.stdev(dados))       # desvio padrão
print(statistics.variance(dados))    # variância


# ============================================================
# 13. MÓDULO datetime (datas e horas)
# ============================================================
print("\n" + "=" * 60)
print("13. MÓDULO DATETIME")
print("=" * 60)

from datetime import datetime, date, timedelta

agora = datetime.now()
print(agora)                         # 2026-05-17 14:30:00.000
print(agora.year, agora.month, agora.day)
print(agora.hour, agora.minute)

# Formatar data como texto
print(agora.strftime("%d/%m/%Y"))    # '17/05/2026'
print(agora.strftime("%H:%M:%S"))    # '14:30:00'

# Texto para data
nasc = datetime.strptime("17/05/2000", "%d/%m/%Y")
print(nasc)

# Operações com datas
hoje = date.today()
amanha = hoje + timedelta(days=1)
ano_passado = hoje - timedelta(days=365)
diferenca = (hoje - date(2000, 1, 1)).days
print(f"Vivi {diferenca} dias desde 01/01/2000")


# ============================================================
# 14. MÓDULO os e sys (sistema operacional)
# ============================================================
print("\n" + "=" * 60)
print("14. MÓDULOS OS E SYS")
print("=" * 60)

import os
import sys

print(os.getcwd())                   # diretório atual
# os.listdir(".")                    # lista arquivos
# os.makedirs("nova_pasta")          # cria pasta
# os.path.exists("arquivo.txt")      # verifica se existe
# os.path.join("pasta", "arq.txt")   # junta caminhos (multiplataforma)

print(sys.version)                   # versão do Python
print(sys.platform)                  # win32, linux, darwin
# sys.exit()                         # encerra o programa


# ============================================================
# 15. MÓDULO collections (estruturas extras)
# ============================================================
print("\n" + "=" * 60)
print("15. MÓDULO COLLECTIONS")
print("=" * 60)

from collections import Counter, defaultdict, deque

# Counter — conta ocorrências automaticamente
votos = ["A", "B", "A", "C", "A", "B"]
contador = Counter(votos)
print(contador)                      # Counter({'A': 3, 'B': 2, 'C': 1})
print(contador.most_common(2))       # [('A', 3), ('B', 2)]

# Contar letras em uma string
print(Counter("banana"))             # Counter({'a': 3, 'n': 2, 'b': 1})

# defaultdict — dicionário com valor padrão
dd = defaultdict(list)
dd["frutas"].append("maçã")          # não precisa criar a chave antes!
dd["frutas"].append("uva")
print(dd)                            # {'frutas': ['maçã', 'uva']}

# deque — lista otimizada para adicionar/remover nas pontas
fila = deque([1, 2, 3])
fila.appendleft(0)                   # adiciona no início (rápido!)
fila.append(4)                       # adiciona no final
print(fila)                          # deque([0, 1, 2, 3, 4])


# ============================================================
# 16. INPUT E PRINT (com truques)
# ============================================================
print("\n" + "=" * 60)
print("16. INPUT E PRINT")
print("=" * 60)

# print com separador e fim personalizados
print("a", "b", "c", sep="-")        # a-b-c
print("sem quebra de linha", end=" ")
print("continua aqui")

# print colorido (no Windows pode precisar de colorama)
print("\033[91mTexto vermelho\033[0m")
print("\033[92mTexto verde\033[0m")
print("\033[93mTexto amarelo\033[0m")

# input com múltiplos valores na mesma linha
# nome, idade = input("Nome e idade: ").split()
# numeros = list(map(int, input("Numeros: ").split()))


# ============================================================
# 17. EXEMPLO PRÁTICO: SORTEIO DE BINGO
# ============================================================
print("\n" + "=" * 60)
print("17. EXEMPLO: SORTEIO DE BINGO")
print("=" * 60)

def sortear_bingo():
    numeros_disponiveis = list(range(1, 76))  # 1 a 75
    random.shuffle(numeros_disponiveis)
    sorteados = []
    for i, n in enumerate(numeros_disponiveis[:10], start=1):
        sorteados.append(n)
        print(f"Rodada {i}: número {n}")
    print(f"\nMaior sorteado: {max(sorteados)}")
    print(f"Menor sorteado: {min(sorteados)}")
    print(f"Média: {statistics.mean(sorteados):.1f}")
    print(f"Soma: {sum(sorteados)}")

sortear_bingo()


# ============================================================
# 18. EXEMPLO: GERADOR DE SENHA ALEATÓRIA
# ============================================================
print("\n" + "=" * 60)
print("18. EXEMPLO: GERADOR DE SENHA")
print("=" * 60)

import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = "".join(random.choices(caracteres, k=tamanho))
    return senha

print(f"Senha gerada: {gerar_senha()}")
print(f"Senha gerada: {gerar_senha(16)}")

# string tem várias constantes úteis:
print(string.ascii_lowercase)        # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)        # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)                 # 0123456789
print(string.punctuation)            # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# ============================================================
# DICAS FINAIS
# ============================================================
# 1. Use min/max/sum em vez de fazer loops manuais
# 2. enumerate() é melhor que "for i in range(len(lista))"
# 3. zip() é o jeito limpo de iterar duas listas juntas
# 4. sorted() não modifica a lista; .sort() modifica
# 5. random.seed() ajuda a DEBUGAR código com aleatoriedade
# 6. f-strings são a melhor forma de formatar texto
# 7. Counter resolve 90% dos problemas de "contar coisas"
# 8. Use list comprehension em vez de map/filter quando puder
# ============================================================
