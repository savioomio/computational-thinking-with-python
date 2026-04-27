import json

agenda = {}


def incluir_contato():
    nome = input("Digite o nome do contato: ").strip().title()

    if not nome:
        print("Erro: O nome do contato não pode ser vazio.")
        return

    if nome in agenda:
        print("Contato já existe na agenda.")
        return

    agenda[nome] = []
    exportar_json() # Salva automaticamente
    print(f"Contato '{nome}' incluído com sucesso.")



def incluir_forma_contato():
    nome = input("Digite o nome do contato: ").strip().title()

    if nome not in agenda:
        print("Contato não encontrado.")
        return

    forma = input("Digite a forma de contato (telefone, email, endereço): ").strip().lower()
    valor = input("Digite a informação: ").strip()

    agenda[nome].append({"tipo": forma, "valor": valor})
    exportar_json() # Salva automaticamente
    print("Forma de contato adicionada com sucesso.")



def alterar_nome_contato():
    nome_antigo = input("Digite o nome atual do contato: ").strip().title()

    if nome_antigo not in agenda:
        print("Contato não encontrado.")
        return

    nome_novo = input("Digite o novo nome do contato: ").strip().title()
    
    if not nome_novo:
        print("Erro: O novo nome não pode ser vazio.")
        return

    agenda[nome_novo] = agenda.pop(nome_antigo)
    exportar_json() # Salva automaticamente
    print("Nome alterado com sucesso.")



def alterar_forma_contato():
    nome = input("Digite o nome do contato: ").strip()

    if nome not in agenda:
        print("Contato não encontrado.")
        return

    for i, item in enumerate(agenda[nome], start=1):
        print(f"{i} - {item['tipo']}: {item['valor']}")

    indice = int(input("Escolha o número da forma de contato que deseja alterar: ")) - 1

    if indice < 0 or indice >= len(agenda[nome]):
        print("Opção inválida.")
        return

    novo_valor = input("Digite o novo valor: ").strip()
    agenda[nome][indice]["valor"] = novo_valor
    exportar_json() # Salva automaticamente

    print("Forma de contato alterada com sucesso.")



def exibir_contato():
    nome = input("Digite o nome do contato: ").strip().title()

    if nome not in agenda:
        print("Contato não encontrado.")
        return

    print(f"\nContato: {nome}")
    for item in agenda[nome]:
        print(f"- {item['tipo']}: {item['valor']}")



def exibir_agenda():
    if not agenda:
        print("Agenda vazia.")
        return

    for nome, contatos in agenda.items():
        print(f"\nContato: {nome}")
        for item in contatos:
            print(f"- {item['tipo']}: {item['valor']}")



def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ").strip().title()

    if nome not in agenda:
        print("Contato não encontrado.")
        return

    confirmar = input(f"Tem certeza que deseja excluir o contato '{nome}'? (s/n): ").strip().lower()
    if confirmar == 's':
        del agenda[nome]
        exportar_json() # Salva automaticamente
        print("Contato excluído com sucesso.")
    else:
        print("Exclusão cancelada.")



def exportar_txt():
    with open("nano/project/agenda.txt", "w", encoding="utf-8") as arquivo:
        for nome, contatos in agenda.items():
            arquivo.write(f"Contato: {nome}\n")
            for item in contatos:
                arquivo.write(f"- {item['tipo']}: {item['valor']}\n")
            arquivo.write("\n")

    print("Agenda exportada para TXT com sucesso.")



def exportar_json():
    with open("nano/project/agenda.json", "w", encoding="utf-8") as arquivo:
        json.dump(agenda, arquivo, ensure_ascii=False, indent=4)

    print("Agenda exportada para JSON com sucesso.")



def importar_json():
    global agenda

    try:
        with open("nano/project/agenda.json", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if not conteudo:
                agenda = {}
            else:
                agenda = json.loads(conteudo)
        print("Agenda importada com sucesso.")
    except (FileNotFoundError, json.JSONDecodeError):
        agenda = {}
        print("Aviso: Arquivo de agenda novo ou vazio. Iniciando agenda limpa.")



def menu():
    importar_json() # Carrega os dados automaticamente ao abrir
    while True:
        print("\n===== AGENDA VIRTUAL =====")
        print("1 - Incluir contato")
        print("2 - Incluir forma de contato")
        print("3 - Alterar nome do contato")
        print("4 - Alterar forma de contato")
        print("5 - Exibir um contato")
        print("6 - Exibir toda a agenda")
        print("7 - Excluir contato")
        print("8 - Exportar para TXT")
        print("9 - Exportar para JSON")
        print("10 - Importar de JSON")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                incluir_contato()
            case "2":
                incluir_forma_contato()
            case "3":
                alterar_nome_contato()
            case "4":
                alterar_forma_contato()
            case "5":
                exibir_contato()
            case "6":
                exibir_agenda()
            case "7":
                excluir_contato()
            case "8":
                exportar_txt()
            case "9":
                exportar_json()
            case "10":
                importar_json()
            case "0":
                print("Encerrando o programa...")
                break
            case _:
                print("Opção inválida.")

menu()