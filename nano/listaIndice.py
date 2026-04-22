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

print(name)
print(sku)
print(price)

print(f"\n======================\n")

for indice in range(0, len(name)):
   print("ID.....: ", (indice+1))
   print("Name...: ", name[indice])
   print("SKU....: ", sku[indice])
   print("Price..: ", price[indice])
   print(f"\n--------------\n")