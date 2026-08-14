
# feira = {
#     'maçã': 3,
#     'uva': 3,
#     'laranja': 5
# }

# for fruta, quantidade in feira.items():
#     if quantidade > 4:
#         print(f"{fruta}: {quantidade} unidades")


# Alunos = {
#     'Bolsonaro': {
#         'nota1': 7,
#         'nota2': 6
#     },

#     'Lula': {
#         'nota1': 8,
#         'nota2': 7
#     },

#     'Ciro Gomes': {
#         'nota1': 9,
#         'nota2': 8
#     }
# }

# for aluno, notas in Alunos.items():
#     for prova, valor in notas.items():
#         print(f"{aluno} - {prova}: {valor}")

# for i,(nome, notas) in enumerate(Alunos.items()):
#     print(f"{i+1} - {nome}: {notas['nota1']}, {notas['nota2']}")


# carrinho = {}
# product = ""
     
# while True:
#     product = input("Digite o nome do produto (ou 'sair' para encerrar): ")
#     if product.lower() == "sair":
#         break
#     quantity = int(input(f"Digite a quantidade de {product}: "))
#     carrinho[product] = quantity
#     print(f"Produto: {product}, Quantidade: {quantity}")

# print("\nItens no carrinho:")
# for product, quantity in carrinho.items():
#     print(f"{product}: {quantity}")


alunos = {}
nome = ""
notas = 0
     
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    for i in range(0, 3):
        nota = int(input(f"Digite a nota {i+1} de {nome}: "))
        notas += nota

    media = notas / 3

    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"

    alunos[nome] = media

    print(f"Aluno: {nome}, Média: {media:.2f}")

print("\nItens no alunos:")
for nome, media in alunos.items():
    print(f"{nome}: {media:.2f} - {status}")