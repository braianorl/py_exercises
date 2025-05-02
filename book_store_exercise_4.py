print("--------------------------------------------")
print("Seja bem vindo à biblioteca Braian Vargas!!!")
print("--------------------------------------------")

lista_livro = []
id_global = 0

def cadastrar_livro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")

    book = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    lista_livro.append(book) #aqui adiciona o livro na lista

    print("-" * 40)
    print("Livro cadastrado com sucesso!")
    print("-" * 40)

while True:
    print(" ")
    print("Menu principal:")
    print("1 - Cadastrar livro")
    print("2 - Consultar livros")
    print("3 - Remover livro")
    print("4 - Sair")
    print(" ")
    
    opcao = input("Digite a opção desejada: ")
    print("-" * 40)
    
    if opcao == "1":       
        id_global += 1
        cadastrar_livro(id_global) #passa o id global para a função cadastrar_livro

    elif opcao == "2":
        while True:
            print("Opções de consulta:")
            print("1 - Consultar todos os livros")
            print("2 - Consultar livro por ID")
            print("3 - Consultar livro por autor")
            print("4 - Voltar ao menu principal")
            print(" ")

            opcao_consulta = input("Digite a opção desejada: ")
            print(" ")

            if opcao_consulta == "1":

                if len(lista_livro) == 0: # Verifica se a lista está vazia
                    print("Nenhum livro cadastrado.")
                    print(" ")
                    break

                else:
                    print("Livros cadastrados:")
                    print(" ")

                for livro in lista_livro:
                        print("ID:", livro["id"])
                        print("Nome do livro:", livro["nome"])
                        print("Autor:", livro["autor"])
                        print("Editora:", livro["editora"])
                        print(" ")
            
            elif opcao_consulta == "2":
                id_consulta = int(input("Digite o ID do livro: "))
                
                livro_encontrado = False 
                for livro in lista_livro:                   
                    if livro["id"] == id_consulta:
                        print(" ")
                        print("ID:", livro["id"])
                        print("Nome do livro:", livro["nome"])
                        print("Autor:", livro["autor"])
                        print("Editora:", livro["editora"])
                        print(" ")
                        livro_encontrado = True #muda o valor para True se o livro for encontrado
                        break
               
                if not livro_encontrado: #se o livro não for encontrado, imprime a mensagem
                    print("Livro não encontrado.")
                    print(" ")
                              
            elif opcao_consulta == "3":
                autor_consulta = input("Digite o nome do autor: ")
                
                livro_encontrado = False
                for livro in lista_livro:
                    if livro["autor"].lower() == autor_consulta.lower():
                        print(" ")
                        print("ID:", livro["id"])
                        print("Nome do livro:", livro["nome"])
                        print("Autor:", livro["autor"])
                        print("Editora:", livro["editora"])
                        print(" ")
                        livro_encontrado = True
                        
                if not livro_encontrado:
                    print("Livro não encontrado.")
                    print(" ")
                        
            elif opcao_consulta == "4":
                break #sai do loop para voltar ao menu principal

            else:
                print("Opção inválida, tente novamente.")
                continue    

    elif opcao == "3":
        id_remove = int(input("Digite o ID do livro que deseja remover: "))

        livro_encontrado = False
        for livro in lista_livro:
            if livro["id"] == id_remove: # Verifica se o ID do livro é igual ao ID informado
                lista_livro.remove(livro) #remove o livro da lista
                print("Livro removido com sucesso!")
                livro_encontrado = True
                break #precisa sair do loop após remover o livro para não dar ruim

        if not livro_encontrado:
            print("Livro não encontrado.")

    elif opcao == "4":
        break

    else:
        print("Opção inválida, tente novamente.")
        continue