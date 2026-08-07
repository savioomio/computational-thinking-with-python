carro = []
continuar = 0

while continuar < 4:

    print("Carro numero: ", continuar + 1)

    marca = str(input("Digite a marca do carro: "))
    vercao = str(input("Digite a versão do carro: "))
    ano = int(input("Digite o ano do carro: "))
    cor = str(input("Digite a cor do carro: "))
    ipva = int(input("Digite o valor do IPVA do carro: "))

    carro.append([marca, vercao, ano, cor])
    continuar += 1

print("\nCarros cadastrados: ")
print(carro)

print("\nCarros cadastrados: ")
for i in range(len(carro)):
    print("Carro numero: ", i + 1)
    print("Marca: ", carro[i][0])
    print("Versão: ", carro[i][1])
    print("Ano: ", carro[i][2])
    print("Cor: ", carro[i][3])
    print("IPVA: ", carro[i][4])
    print("\n")

# carro [0] = ["Fiat", "Uno", 2010, "Preto"]
# carro [1] = ["Chevrolet", "Onix", 2020, "Branco"]
# carro [2] = ["Volkswagen", "Gol", 2015, "Prata"]
# carro [3] = ["Ford", "Ka", 2018, "Vermelho"]
# carro [4] = ["Renault", "Sandero", 2019, "Azul"]