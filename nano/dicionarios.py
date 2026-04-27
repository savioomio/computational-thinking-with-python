def exibir_menu():
    print("\n" + "="*30)
    print("      SISTEMA DE USUÁRIOS")
    print("="*30)
    print("1. Cadastrar Novo")
    print("2. Editar Existente")
    print("3. Buscar Usuário")
    print("4. Remover Usuário")
    print("5. Listar Todos")
    print("6. Ver apenas Logins")
    print("7. Detalhes Técnicos")
    print("8. Limpar Tudo")
    print("0. Sair")
    print("="*30)

usuarios = {
    "admin": {"nome": "Administrador", "nivel": "total"},
    "savio": {"nome": "Sávio Omio", "nivel": "usuario"}
}

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            login = input("Novo Login: ").lower()
            if login in usuarios:
                print(f"Erro: O login '{login}' já existe!")
            else:
                nome = input("Nome Completo: ")
                nivel = input("Nível de acesso: ")
                usuarios[login] = {"nome": nome, "nivel": nivel}
                print(f"Usuário '{login}' cadastrado!")

        case "2":
            login = input("Login para editar: ").lower()
            if login in usuarios:
                dados = usuarios[login]
                print(f"\n--- Editando: {login} ---")
                nome = input(f"Novo Nome [{dados['nome']}]: ") or dados['nome']
                nivel = input(f"Novo Nível [{dados['nivel']}]: ") or dados['nivel']
                
                usuarios[login] = {"nome": nome, "nivel": nivel}
                print(f"Usuário '{login}' atualizado!")
            else:
                print("Erro: Usuário não encontrado para edição.")

        case "3":
            login = input("Login para busca: ").lower()
            usuario = usuarios.get(login)
            if usuario:
                print(f"Resultado: Nome: {usuario['nome']} | Nível: {usuario['nivel']}")
            else:
                print("Usuário não encontrado.")

        case "4":
            login = input("Login para remover: ").lower()
            if usuarios.pop(login, None):
                print(f"Usuário '{login}' removido.")
            else:
                print("Usuário inexistente.")

        case "5":
            if not usuarios:
                print("Vazio.")
            else:
                print("\n--- LISTA COMPLETA ---")
                for login, info in usuarios.items():
                    print(f"Login: {login} | Nome: {info['nome']}")

        case "6":
            print("\nLogins:", list(usuarios.keys()))

        case "7":
            print(f"\nTotal: {len(usuarios)}")
            print("Dados brutos:", list(usuarios.values()))

        case "8":
            if input("Apagar TUDO? (s/n): ").lower() == 's':
                usuarios.clear()
                print("Dicionário limpo!")

        case "0":
            print("Saindo...")
            break

        case _:
            print("Opção inválida!")
