# 1. Escreva um programa para solicitar as notas de duas provas. Faça uma função que receba as duas
# notas por parâmetro e exibe a mensagem “Você foi Aprovado!” ou “Você foi Reprovado!”. Considere
# 6.0 a média mínima para aprovação.

def veredito(nota1, nota2):
  mAp = "Você foi Aprovado!"
  mRe = "Você foi Reprovado!"

  media = (nota1 + nota2)/2

  if media > 6:
    return mAp
  else:
    return mRe

# print(veredito(3, 6))

#==========================

# 2. Faça uma função que receba como parâmetro o número de lados de um polígono e:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO.
# - Se o número de lados for igual a 4, escrever QUADRILÁTERO.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# - Se o número de lados for diferente de 3, 4 ou 5, escrever VALOR INVÁLIDO.

def ladosPoligono(lados):
  if lados == 3:
    return "TRIÂNGULO"
  elif lados == 4:
    return "QUADRILÁTERO"
  elif lados == 5:
    return "PENTÁGONO"
  else:
    return "VALOR INVÁLIDO"

# print(ladosPoligono(5))

#==========================

# 3. Crie uma função que recebe como parâmetro um número inteiro e retorna o seu dobro.

def returDobro(nInt):
  if isinstance(nInt, int):
    dobro = nInt + nInt
    return dobro

# print(returDobro(30))

#==========================

# 4. Faça uma função que recebe um número inteiro por parâmetro e retorna True se for par e False se
# for ímpar.


def isPar(valor):
  if isinstance(valor, int) and valor % 2 == 0:
    return True
  else:
    return False

# print(isPar(31))

# 5. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada area que calcula e retorna a área do círculo e outra função chamada perimetro que calcula e retorna o  perímetro do círculo. Utilize as fórmulas abaixo
# Área = π * r2
# Perímetro = π * 2 * r


def area(raio):
  area = 3.14 * (raio * raio)
  return f"Área: {area}"


def perimetro(raio):
  perimetro = 3.14 * 2 * raio
  return f"Perimetro: {perimetro:.2f}"

# raio = 40
# print(f"{perimetro(raio)}, \n {area(raio)}")

# ===================

# 6. Implementar uma função que recebe como parâmetro a altura em metros (exemplo: 1.70) e o sexo ('M' para masculino e 'F' para feminino) de uma pessoa e retorne o seu peso ideal, sendo que:
# Peso Ideal (para homens) = (72.7 * altura) - 58
# Peso Ideal (para mulheres) = (62.1 * altura) - 44.70

def pesoIdeal(altura, sexo):
  if sexo == "M":
    isIdeal = (72.7 * altura) - 58
    return round(isIdeal)
  elif sexo == "F":
    isIdeal = (62.1 * altura) - 44.70
    return round(isIdeal)
  else:
    return "Genero invalido"

# print(pesoIdeal(1.70, "M"))