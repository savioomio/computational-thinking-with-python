res = "s"
pergunta = "\nQuer mais alguma coisa? \n\n s = Voltar para menu \n n = Ir para pagamento \n\nDigite (s ou n): "
total = 0

while res == "s":

    print("\n1. Lanche")
    print("2. Bebida")
    print("3. Sobremesa\n")

    opc = int(input("Escolher opção: "))
    
    match opc:
        case 1:
            print("\n1. Cachorro Quente: R$ 15,00")
            print("2. Hanburguer: R$ 20,00\n")

            opcl = int(input("Qual vai querer: "))

            match opcl:
                case 1:
                    valorPedido = 15
                    opclQuantidade = float(input("Qual a quantidade: "))
                    valor = float(valorPedido) * opclQuantidade
                    total += valor 

                case 2:
                    valorPedido = 20
                    opclQuantidade = float(input("Qual a quantidade: "))
                    valor = float(valorPedido) * opclQuantidade
                    total += valor 

        case 2:
            print("\n1. Refrigerante: R$ 6,00")
            print("2. Suco Natural: R$ 10,00 \n")

            opcl = int(input("Qual vai querer: "))

            match opcl:
                case 1:
                    valorPedido = 6
                    opclQuantidade = float(input("Qual a quantidade: "))
                    valor = float(valorPedido) * opclQuantidade
                    total += valor 

                case 2:
                    valorPedido = 10
                    opclQuantidade = float(input("Qual a quantidade: "))
                    valor = float(valorPedido) * opclQuantidade
                    total += valor 

        case 3:
            print("\n1. Açair: R$ 25,00")
            print("2. Sorvete: R$ 18,00\n")

            opcl = int(input("Qual vai querer: "))

            match opcl:
                case 1:
                    valorPedido = 25
                    opclQuantidade = float(input("Qual a quantidade: "))
                    valor = float(valorPedido) * opclQuantidade
                    total += valor 

                case 2:
                    valorPedido = 18
                    opclQuantidade = float(input("Qual a quantidade: "))
                    valor = float(valorPedido) * opclQuantidade
                    total += valor 

        case _:
            print("\nOpção invalida")
              
    res = input(pergunta)

if opc >= 1 and opc <= 3 and res == "n":
    print(f"\nValor total: R${total:0.2f} Reais")