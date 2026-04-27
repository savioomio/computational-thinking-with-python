# Python - Capítulo 5 - Funções

## Sumário

1.  É hora de modularizar\
    1.1 O que são funções e por que é importante criá-las?\
    1.2 Funções sem parâmetros\
    1.3 Funções com parâmetros\
    1.3.1 Funções com parâmetros padrão\
    1.3.2 Funções com argumentos variáveis (\*args)\
    1.3.3 Funções com argumentos variáveis nomeados (\*\*kwargs)\
    1.4 Funções com `return`\
    1.5 Um script de funções\
    1.6 É bom documentar!

------------------------------------------------------------------------

## 1. É hora de modularizar

### 1.1 O que são funções e por que é importante criá-las?

Funções são trechos do programa isolados dos demais e que só são
executados quando são chamados.

Elas ajudam no reaproveitamento de código, reduzem esforço e tornam
possível resolver problemas que exigem repetição da mesma lógica várias
vezes.

Exemplo prático: em uma rede de fast food, o funcionário não "reescreve"
o processo de montar um lancho toda vez --- ele apenas executa a função
já pronta.

------------------------------------------------------------------------

### 1.2 Funções sem parâmetros

Exemplo sem função:

``` python
nome = input("Por favor, informe seu nome: ")

print(f"Olá, {nome}! É muito bom saber que o Python te faz feliz!")
```

Sintaxe de uma função:

``` python
def nome_da_funcao(parametros):
    instrucoes
```

Exemplo:

``` python
def exibe_saudacao():
    print(f"Olá, {nome}! É muito bom saber que o Python te faz feliz!")

nome = input("Por favor, informe seu nome: ")

exibe_saudacao()
```

------------------------------------------------------------------------

### 1.3 Funções com parâmetros

Parâmetros são valores que a função precisa receber para executar sua
tarefa.

Exemplo:

``` python
def calcular_velocidade_media(distancia, tempo):
    velocidade_media = distancia / tempo
    print(f"A velocidade média é {velocidade_media}")

dist_digitada = float(input("Digite a distância percorrida "))
tempo_digitado = float(input("Digite o tempo da viagem "))

calcular_velocidade_media(dist_digitada, tempo_digitado)
```

Também é possível indicar tipo:

``` python
def calcular_velocidade_media(distancia: float, tempo: float):
    velocidade_media = distancia / tempo
    print(f"A velocidade média é {velocidade_media}")
```

------------------------------------------------------------------------

### 1.3.1 Parâmetros padrão

Parâmetros opcionais podem receber valores padrão.

``` python
def calcular_velocidade_media(distancia: float, tempo: float, unidade_medida="km/h"):
    velocidade_media = distancia / tempo
    print(f"A velocidade média é {velocidade_media} {unidade_medida}")
```

Chamadas:

``` python
calcular_velocidade_media(200, 10)
calcular_velocidade_media(200, 10, "m/s")
```

------------------------------------------------------------------------

### 1.3.2 Argumentos variáveis (\*args)

Permite receber vários valores em um único parâmetro.

``` python
def exibe_promocao(*clientes):
    for cliente in clientes:
        print(f"Olá, {cliente}!")
```

Exemplo:

``` python
exibe_promocao("Luke", "Leia", "Yoda")
```

Com lista:

``` python
lista = ["Luke", "Leia", "Yoda"]
exibe_promocao(*lista)
```

------------------------------------------------------------------------

### 1.3.3 Argumentos nomeados (\*\*kwargs)

Permite receber argumentos variáveis nomeados.

``` python
def exibe_saudacao(**cliente):
    print(f"Bem-vindo, {cliente['nome']} {cliente['sobrenome']}")
```

Chamada:

``` python
exibe_saudacao(nome="André", sobrenome="David")
```

Isso cria um dicionário internamente.

------------------------------------------------------------------------

### 1.4 Funções com return

O `return` devolve um valor e encerra a função.

Sem return:

``` python
def soma(a, b):
    resultado = a + b
    print(resultado)
```

Com return:

``` python
def soma(a, b):
    resultado = a + b
    return resultado
```

Uso:

``` python
resposta = soma(10, 20)
print(resposta)
```

------------------------------------------------------------------------

### 1.5 Um script de funções

Exemplo com várias funções:

-   Exibir menu
-   Calcular velocidade média
-   Converter temperatura
-   Controlar o fluxo principal

Exemplo:

``` python
def exibir_menu():
    print("1 - Velocidade média")
    print("2 - Converter temperatura")
    print("3 - Sair")
```

Essas funções podem ser organizadas em arquivos como:

-   `funcoes.py`
-   `main.py`

Isso melhora organização e reutilização.

------------------------------------------------------------------------

### 1.6 É bom documentar

Podemos documentar funções com três aspas (`"""`):

``` python
def somar(a: float, b: float):
    """Recebe dois valores float e retorna a soma."""
    return a + b
```

Consultar documentação:

``` python
print(somar.__doc__)
help(somar)
```

------------------------------------------------------------------------

## Referências

-   LUTZ, M. Learning Python. O'Reilly Media Inc, 2013.\
-   PUGA, S.; RISSETI, G. Lógica de programação e estrutura de dados com
    aplicações em Java. Pearson, 2009.
