def criar_item():
   itens = []
   resposta = "S"

   while resposta == "S":
      item = [
         str(input("Name....: ")),
         int(input("SKU.....: ")),
         float(input("Price...: "))
      ]
      itens.append(item)
      resposta = input("Digite \"S\" para continuar: ").upper() 

   return itens

def listar_item(itens):
   print(f"======================\n")
   for item in itens:
      print("Name...: ", item[0])
      print("SKU....: ", item[1])
      print("Price..: ", item[2])
      print("--------------")


def buscar_item(itens):
   busca = str(input("Qual o nome do produto deseja buscar: ").capitalize())
   for item in itens:
      if item[0].capitalize() == busca:
         print("\n--------------")
         print("Name...: ", item[0])
         print("SKU....: ", item[1])
         print("Price..: ", item[2])
         print("--------------\n")

def remover_item(itens):
   busca = str(input("Qual o nome do produto deseja remover: ").capitalize())
   for item in itens:
      if item[0].capitalize() == busca:
         itens.remove(item)
         print("\n--------------")
         print("Produto removido com sucesso!")
         print("--------------\n")

def atualizar_item(itens):
   busca = str(input("Qual o nome do produto deseja atualizar: ").capitalize())
   for item in itens:
      if item[0].capitalize() == busca:
      
         novo_name = input("Name (Enter para pular): ")
         novo_sku = input("SKU (Enter para pular): ")
         novo_price = input("Price (Enter para pular): ")
         
         if novo_name != "":
            item[0] = str(novo_name)
         if novo_sku != "":
            item[1] = int(novo_sku)
         if novo_price != "":
            item[2] = float(novo_price)
         
         print("\n--------------")
         print("Produto atualizado com sucesso!")
         print("--------------\n") 
         break

def menu():
   itens = criar_item()

   reMenu = "S"

   while reMenu == "S":
      print(
         "\n======================",
         "\n \t1 - Listar produtos",
         "\n \t2 - Buscar produto",
         "\n \t3 - Remover produto",
         "\n \t4 - Atualizar produto",
         "\n \t5 - Sair",
         "\n======================\n"
      )
      opcoes = int(input("Qual função você quer usar: "))
      print("\n")
      match opcoes:
         case 1:
            listar_item(itens)
         case 2:
            buscar_item(itens)
         case 3:
            remover_item(itens)
         case 4:
            atualizar_item(itens)
         case 5:
            print("--------------")
            print("Saindo...")
            print("--------------\n")
            break

         case _:
            print("--------------")
            print("Opção inválida")
            print("--------------\n")
   
      reMenu = input("\nDigite \"S\" para continuar: ").upper()