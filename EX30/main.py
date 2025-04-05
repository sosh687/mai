def main():
    cadastros = carregar_cadastros()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")  

        if opcao == "1":
            cadastrar_pessoa(cadastros)
        elif opcao == "2":
            ver_pessoas(cadastros)
        elif opcao == "3":
            print("Obrigado por utilizar o sistema de cadastro!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()