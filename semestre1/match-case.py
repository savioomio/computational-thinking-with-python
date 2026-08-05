print("")
print("1. Lanche")
print("2. Bebida")
print("3. Sobremesa")
print("4. Sair")
print("")

opc = int(input("Escolher opção: "))

print("")

match opc:
    case 1:
        print("1. Cachorro Quente: R$ 15,00")
        print("2. Hanburguer: R$ 20,00")
        print("")

        opcl = int(input("Qual vai querer: "))

        match opcl:
            case 1:
                valorPedido = 15
                opclQuantidade = float(input("Qual a quantidade: "))
                valor = float(valorPedido) * opclQuantidade
            case 2:
                valorPedido = 20
                opclQuantidade = float(input("Qual a quantidade: "))
                valor = float(valorPedido) * opclQuantidade

    case 2:
        print("1. Refrigerante: R$ 6,00")
        print("2. Suco Natural: R$ 10,00")
        print("")

        opcl = int(input("Qual vai querer: "))

        match opcl:
            case 1:
                valorPedido = 6
                opclQuantidade = float(input("Qual a quantidade: "))
                valor = float(valorPedido) * opclQuantidade
            case 2:
                valorPedido = 10
                opclQuantidade = float(input("Qual a quantidade: "))
                valor = float(valorPedido) * opclQuantidade

    case 3:
        print("1. Açair: R$ 25,00")
        print("2. Sorvete: R$ 18,00")
        print("")

        opcl = int(input("Qual vai querer: "))


        match opcl:
            case 1:
                valorPedido = 25
                opclQuantidade = float(input("Qual a quantidade: "))
                valor = float(valorPedido) * opclQuantidade
            case 2:
                valorPedido = 18
                opclQuantidade = float(input("Qual a quantidade: "))
                valor = float(valorPedido) * opclQuantidade
    case 4:
        print("Volte sempre !!!")
    case _:
        print("opção invalida")

if opc >= 1 and opc <= 3:
    print("")
    print(f"Valor total: R${valor:0.2f} Reais")
