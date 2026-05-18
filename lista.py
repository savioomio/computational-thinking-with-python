# Exercício 01
# Preencha uma lista com 10 números aleatórios únicos (sorteados de 1 a 20), ou seja,
# sem elementos repetidos.

# import random 
# ale = random.sample(range(1, 21), 10)
# print(ale)

# ======================

# Exercício 02
# Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
# A partir dessa lista, gere uma nova lista contendo apenas os números primos da lista.

# import random 
# n = random.sample(range(1, 51), 30)

# primos = []
# for num in n:
#    if num > 1:
#       primo = True
#       for i in range(2, num):
#          if num % i == 0:
#             primo = False
#             break
#       if primo:
#          primos.append(num)

# print(n)
# print("Primos:", primos)

# ======================

# Exercício 03
# Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
# A seguir solicite um número inteiro e multiplique todos os itens da lista por esse número.


# import random 
# n = random.sample(range(1, 51), 30)

# print(f"Antes: {n}")

# mult = int(input("Numero que vai multiplicar a lista: "))

# calc = []
# for a in n:
#    calc.append(a * mult)
   
# print(f"Depois: {calc}")


# ======================