
paises = []


def criar_pais():
    nome = input("Digite o nome do país que deseja adicionar: ")
    paises.append(nome)
    print(f"{nome} foi adicionado à lista de países.")


def listar_paises():
    print("Lista de países:")
    for i, pais in enumerate(paises, start=1):
        print(f"{i}. {pais}")


def atualizar_pais():
    listar_paises()
    indice = int(input("Digite o número do país que deseja atualizar: ")) - 1
    if 0 <= indice < len(paises):
        novo_nome = input("Digite o novo nome do país: ")
        paises[indice] = novo_nome
        print("País atualizado com sucesso.")
    else:
        print("Índice inválido. País não encontrado.")


def excluir_pais():
    listar_paises()
    indice = int(input("Digite o número do país que deseja excluir: ")) - 1
    if 0 <= indice < len(paises):
        pais_removido = paises.pop(indice)
        print(f"{pais_removido} foi removido da lista de países.")
    else:
        print("Índice inválido. País não encontrado.")


while True:
    print("\nOpções:")
    print("1. Adicionar país")
    print("2. Listar países")
    print("3. Atualizar país")
    print("4. Excluir país")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_pais()
    elif opcao == "2":
        listar_paises()
    elif opcao == "3":
        atualizar_pais()
    elif opcao == "4":
        excluir_pais()
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
