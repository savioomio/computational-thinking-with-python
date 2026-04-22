itens = []

resposta = "S"

while resposta == "S":
   itens.append(str(input("\nName: "))) 
   itens.append(int(input("SKU: "))) 
   itens.append(float(input("Price: ")))
   resposta = input("Digite \"S\" para continuar: ").upper() 

print(f"\n======================\n")

print(itens)