#-------------------- Raciocínio Computacional ------------------------- #
# Nome: Bruno Eiky Yamamoto                                              #
# Curso: Superior de Tecnologia em Análise e Desenvolvimento de Sistemas # 
# ---------------------------------------------------------------------- #

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
            if menu_principal == 1:                                                             # Escolha dos estudantes

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

                if menu_operacoes == 1:                                                         # Inclui um nome a lista de alunos
                    print("\n\033[1;33m==== INCLUSÃO ====\033[m\n")
                    lista_alunos.append(input("Nome do estudante: "))                           # Escreve o nome 
                    input("Pressione \033[33mENTER\033[m para continuar...")                    #Confirmação 

                if menu_operacoes == 2:                                                         # Lista todos os nomes da lista de alunos
                    print("\n\033[1;33m==== LISTAGEM ====\033[m") 
                    if len(lista_alunos) > 0:                                                   # Caso a lista esteja vazia
                        for c in lista_alunos:                                                  # Lista os alunos 
                            print(f"- {c}")
                    else:                                                                       # Caso tenha alunos na lista 
                        print("\033[31mSem alunos cadastrados!\033[m")
                    input("Pressione \033[33mENTER\033[m para continuar...")                    #Confirmação 

                if menu_operacoes == 3: #
                    print("\n\033[1;33m==== ATUALIZANDO ====\033[m")
                    print("\033[32mEm desenvolvimento...\033[m")

                if menu_operacoes == 4:
                    print("\n\033[1;33m==== EXCLUINDO ====\033[m")
                    print("\033[32mEm desenvolvimento...\033[m")

                elif menu_operacoes == 9:
                    break

                elif menu_operacoes < 1 or menu_operacoes > 4:
                    print("\033[31mOpção inválida!\033[m")


            if menu_principal == 2:                                                              # Escolha dos professores: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Professores]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|"+"_" * 40 + "|")
                menu_operacoes = 9

            if menu_principal == 3:                                                              # Escolha das disciplinas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Disciplina]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|"+"_" * 40 + "|")
                menu_operacoes = 9

            if menu_principal == 4:                                                              # Escolha dos turmas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Turmas]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^35}\033[m|")
                print("|"+"_" * 35 + "|")
                menu_operacoes = 9

            if menu_principal == 5:                                                              # Escolha dos matrículas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Matrículas]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|"+"_" * 40 + "|")
                menu_operacoes = 9



        menu_operacoes = 0                                                                       # Zera a escolha do menu de operações após sair, para poder entrar novamente na proxíma vez 

