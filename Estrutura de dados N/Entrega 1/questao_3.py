jogadores = {}

while len(jogadores) < 20:
    print("\n1. Adicionar jogador")
    print("2. Ver jogadores")
    print("3. Atualizar jogador")
    print("4. Remover jogador")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        numero_camisa = input("Digite o número da camisa do jogador: ")
        nome = input("Digite o nome do jogador: ")
        jogadores[numero_camisa] = nome
        
    elif opcao == '2':
        for numero_camisa, nome in jogadores.items():
            print(f"Camisa {numero_camisa}: {nome}")
            
    elif opcao == '3':
        numero_camisa = input("Digite o número da camisa do jogador que deseja atualizar: ")
        if numero_camisa in jogadores:
            novo_nome = input("Digite o novo nome do jogador: ")
            jogadores[numero_camisa] = novo_nome
        else:
            print("Número de camisa inválido.")
            
    elif opcao == '4':
        numero_camisa = input("Digite o número da camisa do jogador que deseja remover: ")
        if numero_camisa in jogadores:
            del jogadores[numero_camisa]
        else:
            print("Número de camisa inválido.")
            
    elif opcao == '5':
        break
        
    else:
        print("Opção inválida.")
