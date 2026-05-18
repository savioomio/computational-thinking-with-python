# ============================================================
# GUIA COMPLETO DE VALIDAÇÕES EM PYTHON
# ============================================================
# Este arquivo contém exemplos didáticos de TODAS as validações
# mais comuns que você vai usar no dia a dia programando.
# ============================================================


# Inteiros — try/except, intervalo, positivo, par/ímpar
# Floats — com vírgula brasileira, intervalo (notas)
# Strings — obrigatórias, tamanho, só letras, só números
# Opções/Menu — sim/não, opções fixas
# Email — validação simples e com regex
# CPF — com cálculo dos dígitos verificadores
# Senha — força (maiúscula, minúscula, número, especial)
# Datas — com datetime, cálculo de idade
# Telefone — DDD e quantidade de dígitos
# Listas/Dicionários — busca, duplicatas
# Tipos — isinstance
# Exceções — try/except/else/finally completo
# Assert — validação em modo debug
# Exemplo completo — cadastro juntando tudo

# ============================================================
# 1. VALIDAÇÃO DE NÚMEROS INTEIROS
# ============================================================
print("=" * 60)
print("1. VALIDAÇÃO DE NÚMEROS INTEIROS")
print("=" * 60)

# Forma básica: try/except
def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: digite um número inteiro válido!")

# Exemplo de uso (descomente para testar):
# idade = ler_inteiro("Digite sua idade: ")
# print(f"Idade: {idade}")


# Validação com intervalo (entre min e max)
def ler_inteiro_intervalo(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Erro: digite um valor entre {minimo} e {maximo}!")
        except ValueError:
            print("Erro: digite um número inteiro válido!")

# Exemplo:
# idade = ler_inteiro_intervalo("Idade (0-120): ", 0, 120)


# Validar se é positivo
def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("Erro: o número deve ser positivo!")
        except ValueError:
            print("Erro: digite um número inteiro!")


# Validar se é par
def eh_par(numero):
    return numero % 2 == 0

# print(eh_par(4))   # True
# print(eh_par(7))   # False


# ============================================================
# 2. VALIDAÇÃO DE NÚMEROS DECIMAIS (FLOAT)
# ============================================================
print("\n" + "=" * 60)
print("2. VALIDAÇÃO DE NÚMEROS DECIMAIS")
print("=" * 60)

def ler_float(mensagem):
    while True:
        try:
            # replace troca vírgula por ponto (formato brasileiro)
            valor = float(input(mensagem).replace(",", "."))
            return valor
        except ValueError:
            print("Erro: digite um número decimal válido!")

# Exemplo: altura = ler_float("Altura (m): ")


# Float em um intervalo (ex: nota de 0 a 10)
def ler_nota():
    while True:
        try:
            nota = float(input("Nota (0-10): ").replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            print("Erro: nota deve estar entre 0 e 10!")
        except ValueError:
            print("Erro: valor inválido!")


# ============================================================
# 3. VALIDAÇÃO DE STRINGS (TEXTO)
# ============================================================
print("\n" + "=" * 60)
print("3. VALIDAÇÃO DE STRINGS")
print("=" * 60)

# Validar se a string NÃO está vazia
def ler_texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()  # strip remove espaços nas pontas
        if texto:  # string vazia é False em Python
            return texto
        print("Erro: campo obrigatório!")


# Validar tamanho mínimo e máximo
def ler_nome(min_chars=2, max_chars=50):
    while True:
        nome = input("Nome: ").strip()
        if min_chars <= len(nome) <= max_chars:
            return nome
        print(f"Nome deve ter entre {min_chars} e {max_chars} caracteres!")


# Validar se contém apenas letras
def validar_apenas_letras(texto):
    # isalpha() retorna True se todos os caracteres forem letras
    # replace remove espaços para permitir nomes compostos
    return texto.replace(" ", "").isalpha()

# print(validar_apenas_letras("João Silva"))  # True
# print(validar_apenas_letras("João 123"))    # False


# Validar se contém apenas números
def validar_apenas_numeros(texto):
    return texto.isdigit()

# print(validar_apenas_numeros("12345"))  # True
# print(validar_apenas_numeros("12a45"))  # False


# Validar se é alfanumérico (letras e números)
def validar_alfanumerico(texto):
    return texto.isalnum()


# ============================================================
# 4. VALIDAÇÃO DE OPÇÕES (MENU / SIM-NÃO)
# ============================================================
print("\n" + "=" * 60)
print("4. VALIDAÇÃO DE OPÇÕES")
print("=" * 60)

# Sim ou Não
def confirmar(mensagem):
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ["s", "sim", "y", "yes"]:
            return True
        elif resposta in ["n", "nao", "não", "no"]:
            return False
        print("Responda com 's' ou 'n'!")


# Menu com opções específicas
def menu_principal():
    opcoes_validas = ["1", "2", "3", "4"]
    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Sair")
        opcao = input("Escolha: ").strip()
        if opcao in opcoes_validas:
            return opcao
        print("Opção inválida!")


# ============================================================
# 5. VALIDAÇÃO DE EMAIL
# ============================================================
print("\n" + "=" * 60)
print("5. VALIDAÇÃO DE EMAIL")
print("=" * 60)

# Validação simples (sem regex)
def validar_email_simples(email):
    # Regras básicas: tem @, tem ponto depois do @, não tem espaços
    if " " in email:
        return False
    if email.count("@") != 1:
        return False
    parte_local, dominio = email.split("@")
    if not parte_local or not dominio:
        return False
    if "." not in dominio:
        return False
    return True

# print(validar_email_simples("teste@email.com"))  # True
# print(validar_email_simples("teste.com"))        # False
# print(validar_email_simples("a@b.c"))            # True


# Validação com regex (mais robusta)
import re

def validar_email_regex(email):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(padrao, email))

# print(validar_email_regex("savio@gmail.com"))  # True


# ============================================================
# 6. VALIDAÇÃO DE CPF (BRASIL)
# ============================================================
print("\n" + "=" * 60)
print("6. VALIDAÇÃO DE CPF")
print("=" * 60)

def validar_cpf(cpf):
    # Remove pontos, traços e espaços
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")

    # CPF deve ter 11 dígitos
    if len(cpf) != 11:
        return False

    # Deve conter apenas números
    if not cpf.isdigit():
        return False

    # CPFs com todos os dígitos iguais são inválidos (111.111.111-11)
    if cpf == cpf[0] * 11:
        return False

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):
        return False

    return True

# print(validar_cpf("111.444.777-35"))  # True (CPF válido fictício)
# print(validar_cpf("111.111.111-11"))  # False


# ============================================================
# 7. VALIDAÇÃO DE SENHA
# ============================================================
print("\n" + "=" * 60)
print("7. VALIDAÇÃO DE SENHA")
print("=" * 60)

def validar_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("- Deve ter pelo menos 8 caracteres")

    if not any(c.isupper() for c in senha):
        erros.append("- Deve ter pelo menos uma letra MAIÚSCULA")

    if not any(c.islower() for c in senha):
        erros.append("- Deve ter pelo menos uma letra minúscula")

    if not any(c.isdigit() for c in senha):
        erros.append("- Deve ter pelo menos um número")

    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in caracteres_especiais for c in senha):
        erros.append("- Deve ter pelo menos um caractere especial")

    return erros  # lista vazia = senha válida

# erros = validar_senha("abc123")
# if erros:
#     print("Senha inválida:")
#     for e in erros: print(e)
# else:
#     print("Senha forte!")


# ============================================================
# 8. VALIDAÇÃO DE DATAS
# ============================================================
print("\n" + "=" * 60)
print("8. VALIDAÇÃO DE DATAS")
print("=" * 60)

from datetime import datetime

def validar_data(data_str, formato="%d/%m/%Y"):
    try:
        datetime.strptime(data_str, formato)
        return True
    except ValueError:
        return False

# print(validar_data("17/05/2026"))  # True
# print(validar_data("32/05/2026"))  # False (dia inválido)
# print(validar_data("17-05-2026"))  # False (formato errado)


def ler_data():
    while True:
        data = input("Data (dd/mm/aaaa): ").strip()
        if validar_data(data):
            return datetime.strptime(data, "%d/%m/%Y")
        print("Data inválida!")


# Calcular idade a partir de data de nascimento
def calcular_idade(data_nascimento_str):
    nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    hoje = datetime.now()
    idade = hoje.year - nascimento.year
    # Ajuste: se ainda não fez aniversário este ano
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade

# print(calcular_idade("17/05/2000"))


# ============================================================
# 9. VALIDAÇÃO DE TELEFONE
# ============================================================
print("\n" + "=" * 60)
print("9. VALIDAÇÃO DE TELEFONE")
print("=" * 60)

def validar_telefone(telefone):
    # Remove caracteres não numéricos
    numeros = "".join(c for c in telefone if c.isdigit())

    # Telefone brasileiro: 10 dígitos (fixo) ou 11 (celular com 9)
    if len(numeros) not in [10, 11]:
        return False

    # DDD válido (11 a 99)
    ddd = int(numeros[:2])
    if ddd < 11 or ddd > 99:
        return False

    return True

# print(validar_telefone("(11) 98765-4321"))  # True
# print(validar_telefone("11 1234"))          # False


# ============================================================
# 10. VALIDAÇÃO USANDO LISTAS E DICIONÁRIOS
# ============================================================
print("\n" + "=" * 60)
print("10. VALIDAÇÃO COM ESTRUTURAS DE DADOS")
print("=" * 60)

# Verificar se um valor está em uma lista
estados_validos = ["SP", "RJ", "MG", "RS", "PR", "SC", "BA"]

def validar_estado(estado):
    return estado.upper() in estados_validos


# Verificar duplicatas em uma lista
def tem_duplicatas(lista):
    return len(lista) != len(set(lista))

# print(tem_duplicatas([1, 2, 3, 4]))     # False
# print(tem_duplicatas([1, 2, 3, 1]))     # True


# Verificar se chave existe no dicionário
def buscar_usuario(usuarios, nome):
    if nome in usuarios:
        return usuarios[nome]
    return None

# usuarios = {"savio": 25, "maria": 30}
# print(buscar_usuario(usuarios, "savio"))  # 25
# print(buscar_usuario(usuarios, "joao"))   # None


# ============================================================
# 11. VALIDAÇÃO DE TIPOS (TYPE CHECKING)
# ============================================================
print("\n" + "=" * 60)
print("11. VALIDAÇÃO DE TIPOS")
print("=" * 60)

# isinstance verifica se a variável é de um tipo
def processar_valor(valor):
    if isinstance(valor, int):
        return f"Inteiro: {valor}"
    elif isinstance(valor, float):
        return f"Decimal: {valor}"
    elif isinstance(valor, str):
        return f"Texto: {valor}"
    elif isinstance(valor, list):
        return f"Lista com {len(valor)} itens"
    elif isinstance(valor, dict):
        return f"Dicionário com {len(valor)} chaves"
    else:
        return "Tipo desconhecido"

# print(processar_valor(10))
# print(processar_valor("oi"))
# print(processar_valor([1, 2, 3]))


# ============================================================
# 12. TRATAMENTO DE EXCEÇÕES (try/except completo)
# ============================================================
print("\n" + "=" * 60)
print("12. TRATAMENTO DE EXCEÇÕES")
print("=" * 60)

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero!"
    except TypeError:
        return "Erro: tipos incompatíveis!"
    except Exception as e:
        # Exception captura QUALQUER outro erro
        return f"Erro inesperado: {e}"
    else:
        # Executa SE não houve erro
        return f"Resultado: {resultado}"
    finally:
        # SEMPRE executa (com ou sem erro)
        print("Operação finalizada")

# print(dividir(10, 2))   # Resultado: 5.0
# print(dividir(10, 0))   # Erro: divisão por zero!
# print(dividir(10, "a")) # Erro: tipos incompatíveis!


# ============================================================
# 13. VALIDAÇÃO COM ASSERT (modo debug)
# ============================================================
print("\n" + "=" * 60)
print("13. VALIDAÇÃO COM ASSERT")
print("=" * 60)

def calcular_media(notas):
    # assert lança AssertionError se a condição for False
    assert len(notas) > 0, "A lista não pode estar vazia"
    assert all(0 <= n <= 10 for n in notas), "Notas devem estar entre 0 e 10"
    return sum(notas) / len(notas)

# print(calcular_media([8, 9, 7]))  # 8.0
# print(calcular_media([]))         # AssertionError


# ============================================================
# 14. EXEMPLO COMPLETO: CADASTRO DE USUÁRIO
# ============================================================
print("\n" + "=" * 60)
print("14. EXEMPLO COMPLETO: CADASTRO")
print("=" * 60)

def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")

    # Nome (obrigatório, só letras)
    while True:
        nome = input("Nome completo: ").strip()
        if len(nome) < 3:
            print("Nome muito curto!")
            continue
        if not validar_apenas_letras(nome):
            print("Nome deve conter apenas letras!")
            continue
        break

    # Idade (entre 0 e 120)
    while True:
        try:
            idade = int(input("Idade: "))
            if 0 < idade < 120:
                break
            print("Idade inválida!")
        except ValueError:
            print("Digite um número!")

    # Email
    while True:
        email = input("Email: ").strip().lower()
        if validar_email_simples(email):
            break
        print("Email inválido!")

    # CPF
    while True:
        cpf = input("CPF: ").strip()
        if validar_cpf(cpf):
            break
        print("CPF inválido!")

    return {
        "nome": nome,
        "idade": idade,
        "email": email,
        "cpf": cpf
    }

# usuario = cadastrar_usuario()
# print(usuario)


# ============================================================
# DICAS FINAIS
# ============================================================
# 1. SEMPRE use try/except ao converter input() para int/float
# 2. Use .strip() para remover espaços indesejados nas pontas
# 3. Use .lower() ou .upper() para normalizar comparações
# 4. while True + break é o padrão para "pedir até dar certo"
# 5. Funções de validação devem retornar True/False
# 6. Separe a VALIDAÇÃO da AÇÃO (uma função valida, outra processa)
# 7. Mensagens de erro devem ser CLARAS para o usuário
# ============================================================
