menu_principal=0
menu_operacoes=0
lista_alunos = []


while menu_principal != 9:
    while True:                                                                                 # Loop que termina apenas ao selecionar (9)Sair ou uma das opções váidas 
        print("\n---- MENU PRINCIPAL ---")
        print('\033[33m(1) \033[34mGerenciar estudantes.\033[m') 
        print("\033[33m(2) \033[34mGerenciar professores.\033[m")
        print("\033[33m(3) \033[34mGerenciar disciplinas.\033[m")
        print("\033[33m(4) \033[34mGerenciar turmas.\033[m")
        print("\033[33m(5) \033[34mGerenciar matrículas.\033[m")
        print("\033[33m(9) \033[34mSair.\033[m")

        try:                                                                                    # Valida a respota do menu principal
            menu_principal = int(input("Informe a opção desejada: "))                           # Escolha do menu principal
            if menu_principal > 0 and menu_principal < 6 or menu_principal == 9:                # Verifica se está no intervalo e no formato adequado
                break 
            else:                                                                               # Erro quando a entrada está fora do intervalo 
                print("\033[31mOpção inválida!\033[m")
        except:                                                                                 # Erro quando digitado caractere não numérico 
            print("\033[31mOpção inválida!\033[m")

    if menu_principal != 9:                                                                     # Só será rodado se não foi escolhido a opção (9)Sair 

        while menu_operacoes != 9:                                                              # Loop que se repete até escolher (9)Sair, voltando para o menu principal
            if menu_principal == 1:                                                             

                print("\n==== \033[33m[Estudantes]\033[m MENU DE OPERAÇÓES ====")

                while True:                                                                     #Loop que repete até a escolha de uma opção válida ou (9)Sair
                    print()
                    print("\033[33m(1) \033[34mIncluir\033[m")
                    print("\033[33m(2) \033[34mListar\033[m")
                    print("\033[33m(3) \033[34mAtualizar\033[m")
                    print("\033[33m(4) \033[34mExcluir\033[m")
                    print("\033[33m(9) \033[34mVoltar ao menu principal\033[m")

                    try:                                                                        # Valida a respota do menu de operações 
                        menu_operacoes = int(input("Informe a ação desejada: "))                #Escolha do menu de operações 
                        if menu_operacoes >= 1 and menu_operacoes <= 5 or menu_operacoes == 9:  # Verifica se está no intervalo e no formato adequado
                            break
                        else:                                                                   # Erro quando a entrada está fora do intervalo 
                            print("\033[31mOpção inválida!\033[m")
                    except:                                                                     # Erro quando digitado caractere não numérico
                        print("\033[31mOpção inválida!\033[m")

                if menu_operacoes == 1:     
                    dados_aluno={}                                               
                    print("\n\033[1;33m==== INCLUIR ====\033[m\n")

                    nome = input("Nome do estudante: ")                                         # Escreve o nome 
                    input("Pressione \033[33mENTER\033[m para continuar...")                                  #Confirmação
                    dados_aluno["nome"] = nome

                    cpf = input("\nDigite seu CPF: ")
                    input("Pressione \033[33mENTER\033[m para continuar...")  
                    dados_aluno['cpf'] = cpf

                    while True:
                        try: 
                            codigo_existe = False
                            codigo = int(input("\nDigite o código do aluno: "))
                            for aluno in lista_alunos:
                                if codigo == aluno['codigo'] :
                                    codigo_existe =True 
                                    break
                            if codigo_existe:
                                print("\033[31mEste código já existe!\033[m")
                            else:
                                input("Pressione \033[33mENTER\033[m para continuar...")
                                break
                        except ValueError:
                            print("\033[31mCódigo inválido\033[m")
                        
                    dados_aluno['codigo'] = codigo
                    
                    lista_alunos.append(dados_aluno)                                               

                if menu_operacoes == 2:                                                         # Lista todos os nomes da lista de alunos
                    print("\n\033[1;33m==== LISTAR ====\033[m") 

                    if len(lista_alunos) > 0:                                                   # Caso a lista esteja vazia
                        for c in lista_alunos:                                                  # Lista os alunos 
                            print(f"- {c}")
                    else:                                                                       # Caso tenha alunos na lista 
                        print("\033[31mSem alunos cadastrados!\033[m")
                    input("Pressione \033[33mENTER\033[m para continuar...")

                if menu_operacoes == 3: 
                    print("\n\033[1;33m==== ATUALIZAR ====\033[m")

                    if len(lista_alunos) > 0:
                        while True:
                            try:
                                codigo_aluno = int(input("\nCódigo do aluno: "))
                                for aluno in lista_alunos:
                                    if codigo_aluno == aluno['codigo'] :
                                        codigo_existe = True 
                                        break
                                if codigo_existe:
                                    input("Pressione \033[33mENTER\033[m para continuar...")
                                    break
                                print('\033[33mAluno não encontrado\033[m')
                            except ValueError:
                                print("\033[33mResposta inválida\033[m")
                        
                        for aluno in lista_alunos:
                            if aluno['codigo'] == codigo_aluno:
                                aluno['nome'] = input("\nNovo nome: ")
                                input("Pressione \033[33mENTER\033[m para continuar...")

                                while True:
                                    try: 
                                        codigo_existe = False
                                        codigo = int(input("\nNovo código: "))
                                        for aluno in lista_alunos:
                                            if codigo == aluno['codigo'] :
                                                codigo_existe =True 
                                                break
                                        if codigo_existe:
                                            print("\033[31mEste código já existe!\033[m")
                                        else:
                                            input("Pressione \033[33mENTER\033[m para continuar...")
                                            break
                                    except ValueError:
                                        print("\033[31mCódigo inválido\033[m")
                                
                                aluno['codigo'] = codigo
                                aluno['cpf'] = input("\nNovo CPF: ")
                                input("Pressione \033[33mENTER\033[m para continuar...")
                    else:
                        print("\033[31mSem alunos para atualizar!\033[m")

                if menu_operacoes == 4:
                    print("\n\033[1;33m==== EXCLUIR ====\033[m")

                    if len(lista_alunos) > 0:
                        while True:
                            try:
                                codigo_aluno = int(input("\nCódigo do aluno: "))
                                for aluno in lista_alunos:
                                    if codigo_aluno == aluno['codigo'] :
                                        codigo_existe = True 
                                        break
                                if codigo_existe:
                                    input("Pressione \033[33mENTER\033[m para continuar...")
                                    break
                                print('\033[33mAluno não encontrado\033[m')
                            except ValueError:
                                print("\033[33mResposta inválida\033[m")
                        
                        for aluno in lista_alunos:
                            if aluno['codigo'] == codigo_aluno:
                                lista_alunos.remove(aluno)

                        print("\033[32mAluno excluído!\033[m")
                        
                    else:
                        print("\033[31mSem alunos para excluir!\033[m")

                elif menu_operacoes == 9:
                    break

                elif menu_operacoes < 1 or menu_operacoes > 4:
                    print("\033[31mOpção inválida!\033[m")


            elif menu_principal == 2:                                                              # Escolha dos professores: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Professores]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|"+"_" * 40 + "|")
                menu_operacoes = 9

            elif menu_principal == 3:                                                              # Escolha das disciplinas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Disciplina]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|"+"_" * 40 + "|")
                menu_operacoes = 9

            elif menu_principal == 4:                                                              # Escolha dos turmas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Turmas]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^35}\033[m|")
                print("|"+"_" * 35 + "|")
                menu_operacoes = 9

            elif menu_principal == 5:                                                              # Escolha dos matrículas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Matrículas]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|"+"_" * 40 + "|")
                menu_operacoes = 9



        menu_operacoes = 0     