def mostrar_lista(lista):
    if lista:
        print("Lista atual:")
        for item in lista:
            print(item)
    else:
        print("A lista está vazia.")


def main():
    lista = []
    
    while True:
        print("\n--- Menu ---")
        print("1. Inserir novo item")
        print("2. Excluir item")
        print("3. Mostrar lista")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            novo_item = input("Digite o novo item: ")
            lista.append(novo_item)
            print(f"{novo_item} foi adicionado à lista.")
            mostrar_lista(lista)
        elif opcao == "2":
            if lista:
                item_a_excluir = input("Digite o item a ser excluído: ")
                if item_a_excluir in lista:
                    lista.remove(item_a_excluir)
                    print(f"{item_a_excluir} foi removido da lista.")
                    mostrar_lista(lista)
                else:
                    print("O item especificado não está na lista.")
            else:
                print("A lista está vazia.")
        elif opcao == "3":
            mostrar_lista(lista)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()