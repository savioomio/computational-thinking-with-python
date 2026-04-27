# Exemplos Simples de Funções em Python

# 1. Função sem parâmetros (Simples)
def exibir_mensagem():
    print("Olá! Esta é uma função simples que apenas exibe um texto.")

# Chamando a função
exibir_mensagem()


# 2. Função com parâmetros
def calcular_velocidade_media(distancia, tempo):
    velocidade = distancia / tempo
    print(f"A velocidade média é: {velocidade}")

# Chamando com valores
calcular_velocidade_media(100, 2)


# 3. Função com parâmetros padrão (Opcional)
def saudar(nome, mensagem="Seja bem-vindo"):
    print(f"{mensagem}, {nome}!")

# Chamando sem a mensagem (usa o padrão)
saudar("Savio")
# Chamando com uma mensagem diferente
saudar("Savio", "Bom dia")


# 4. Função com retorno (return)
# O return devolve o valor para quem chamou a função
def somar(a, b):
    resultado = a + b
    return resultado

# Guardando o resultado em uma variável
total = somar(10, 20)
print(f"O resultado da soma é: {total}")


# 5. Argumentos variáveis (*args)
# O asterisco permite passar quantos valores você quiser
def listar_frutas(*frutas):
    print("Sua lista de compras:")
    for fruta in frutas:
        print(f"- {fruta}")

listar_frutas("Maçã", "Banana", "Uva", "Morango")


# 6. Argumentos nomeados (**kwargs)
# Os dois asteriscos permitem passar nomes e valores (como um dicionário)
def exibir_dados_usuario(**dados):
    print("Dados do Usuário:")
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']}")

exibir_dados_usuario(nome="Savio", idade=20)
