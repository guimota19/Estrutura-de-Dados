import os

# Função para exibir o menu
def exibir_menu():
    print("=== MENU ===")
    print("(1) Listar todos os produtos")
    print("(2) Listar produto pelo ID")
    print("(3) Listar todos os produtos ordenados (A/Z)")
    print("(4) Cadastrar novo produto")
    print("(5) Editar produto")
    print("(6) Excluir produto")
    print("(7) Sair do programa")
    return input("Escolha uma opção: ")

# Função para listar os produtos
def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(produto)

# Função listar produto pelo ID
def listar_produto_por_id(produtos, produto_id):
    for produto in produtos:
        if produto['id'] == produto_id:
            print(produto)
            return
    print("Produto não encontrado.")

# Função listar os produtos ordenados
def listar_produtos_ordenados(produtos, ordem):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    if ordem == 'A':
        produtos.sort(key=lambda x: x['descricao'])
    elif ordem == 'Z':
        produtos.sort(key=lambda x: x['descricao'], reverse=True)
    else:
        print("Opção inválida.")
        return

    listar_produtos(produtos)

# Função para cadastrar novo produto
def cadastrar_produto(produtos):
    produto = {}
    produto['id'] = len(produtos) + 1  # ID autoincrementado
    produto['descricao'] = input("Digite a descrição do produto: ")
    produto['peso'] = input("Digite o peso do produto: ")
    produto['valor'] = input("Digite o valor do produto: ")
    produto['fornecedor'] = input("Digite o fornecedor do produto: ")
    produtos.append(produto)
    print("Produto cadastrado com sucesso.")

# Função editar um produto
def editar_produto(produtos, produto_id):
    for produto in produtos:
        if produto['id'] == produto_id:
            produto['descricao'] = input("Digite a nova descrição do produto: ")
            produto['peso'] = input("Digite o novo peso do produto: ")
            produto['valor'] = input("Digite o novo valor do produto: ")
            produto['fornecedor'] = input("Digite o novo fornecedor do produto: ")
            print("Produto editado com sucesso.")
            return
    print("Produto não encontrado.")

# Função excluir um produto
def excluir_produto(produtos, produto_id):
    for produto in produtos:
        if produto['id'] == produto_id:
            produtos.remove(produto)
            print("Produto excluído com sucesso.")
            return
    print("Produto não encontrado.")

# Função para autenticar o usuário
def autenticar_usuario():
    usuario_arquivo = "usuario.txt"
    if not os.path.exists(usuario_arquivo):
        print("Arquivo de usuário não encontrado. Crie o arquivo 'usuario.txt' com usuário e senha.")
        return False

    with open(usuario_arquivo, 'r') as file:
        linha = file.readline().strip()
        usuario, senha = linha.split(',')
    
    input_usuario = input("Digite o usuário: ")
    input_senha = input("Digite a senha: ")

    if input_usuario == usuario and input_senha == senha:
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False

# Main
def main():
    if not autenticar_usuario():
        return

    produtos_arquivo = "produtos.txt"
    produtos = []

    if os.path.exists(produtos_arquivo):
        with open(produtos_arquivo, 'r') as file:
            for linha in file:
                produto = eval(linha.strip())
                produtos.append(produto)

    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            listar_produtos(produtos)
        elif opcao == '2':
            produto_id = int(input("Digite o ID do produto: "))
            listar_produto_por_id(produtos, produto_id)
        elif opcao == '3':
            ordem = input("Digite 'A' para ordem crescente ou 'Z' para ordem decrescente: ").upper()
            listar_produtos_ordenados(produtos, ordem)
        elif opcao == '4':
            cadastrar_produto(produtos)
        elif opcao == '5':
            produto_id = int(input("Digite o ID do produto a ser editado: "))
            editar_produto(produtos, produto_id)
        elif opcao == '6':
            produto_id = int(input("Digite o ID do produto a ser excluído: "))
            excluir_produto(produtos, produto_id)
        elif opcao == '7':
            with open(produtos_arquivo, 'w') as file:
                for produto in produtos:
                    file.write(str(produto) + '\n')
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
