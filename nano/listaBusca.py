name = []
sku = []
price = []

resposta = "S"

while resposta == "S":
   name.append(str(input("\nName: "))) 
   sku.append(int(input("SKU: "))) 
   price.append(float(input("Price: ")))
   resposta = input("Digite \"S\" para continuar: ").upper() 

print(f"\n======================\n")

reBusca = "S"

while reBusca == "S":
   busca = str(input("Qual o nome do produto deseja buscar: ").capitalize())
   for indice in range(0, len(name)):
      if name[indice].capitalize() == busca: 
         print("ID.....: ", (indice+1))
         print("Name...: ", name[indice])
         print("SKU....: ", sku[indice])
         print("Price..: ", price[indice])
         print(f"\n--------------\n")
   reBusca = input("Digite \"S\" para Buscar de novo: ").upper() 