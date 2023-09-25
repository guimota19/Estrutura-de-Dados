def adicionar_linha(arquivo, linha):
    with open(arquivo, 'a') as f:
        f.write(linha + '\n')

def listar_linhas(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        for i, linha in enumerate(linhas):
            print(f"{i+1}. {linha.strip()}")

def alterar_linha(arquivo, numero_linha, nova_linha):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    if 0 <= numero_linha < len(linhas):
        linhas[numero_linha] = nova_linha + '\n'
        with open(arquivo, 'w') as f:
            f.writelines(linhas)
    else:
        print("Número de linha inválido.")

def excluir_linha(arquivo, numero_linha):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    if 0 <= numero_linha < len(linhas):
        del linhas[numero_linha]
        with open(arquivo, 'w') as f:
            f.writelines(linhas)
    else:
        print("Número de linha inválido.")
