def menu_principal():
    while True:  # Loop que termina apenas ao selecionar (9)Sair ou uma das opções váidas
        print("\n---- MENU PRINCIPAL ---")
        print('\033[33m(1) \033[34mGerenciar estudantes.\033[m')
        print("\033[33m(2) \033[34mGerenciar professores.\033[m")
        print("\033[33m(3) \033[34mGerenciar disciplinas.\033[m")
        print("\033[33m(4) \033[34mGerenciar turmas.\033[m")
        print("\033[33m(5) \033[34mGerenciar matrículas.\033[m")
        print("\033[33m(9) \033[34mSair.\033[m")

        try:  # Valida a respota do menu principal
            menu_principal = int(input("Informe a opção desejada: "))  # Escolha do menu principal
            if menu_principal > 0 and menu_principal < 6 or menu_principal == 9:  # Verifica se está no intervalo e no formato adequado
                break
            else:  # Erro quando a entrada está fora do intervalo
                print("\033[31mOpção inválida!\033[m")
        except:  # Erro quando digitado caractere não numérico
            print("\033[31mOpção inválida!\033[m")

    return menu_principal

def menu_operacoes():

    while True:  # Loop que repete até a escolha de uma opção válida ou (9)Sair
        print()
        print("\033[33m(1) \033[34mIncluir\033[m")
        print("\033[33m(2) \033[34mListar\033[m")
        print("\033[33m(3) \033[34mAtualizar\033[m")
        print("\033[33m(4) \033[34mExcluir\033[m")
        print("\033[33m(9) \033[34mVoltar ao menu principal\033[m")

        try:  # Valida a respota do menu de operações
            menu_operacoes = int(input("Informe a ação desejada: "))  # Escolha do menu de operações
            if menu_operacoes >= 1 and menu_operacoes <= 5 or menu_operacoes == 9:  # Verifica se está no intervalo e no formato adequado
                break
            else:  # Erro quando a entrada está fora do intervalo
                print("\033[31mOpção inválida!\033[m")
        except:  # Erro quando digitado caractere não numérico
            print("\033[31mOpção inválida!\033[m")

    return menu_operacoes

def incluir(lista):
    dados_aluno = {}
    print("\n\033[1;33m==== INCLUIR ====\033[m\n")

    nome = input("Nome do estudante: ")  # Escreve o nome
    input("Pressione \033[33mENTER\033[m para continuar...")  # Confirmação
    dados_aluno["nome"] = nome

    cpf = input("\nDigite seu CPF: ")
    input("Pressione \033[33mENTER\033[m para continuar...")
    dados_aluno['cpf'] = cpf

    while True:
        try:
            codigo_existe = False
            codigo = int(input("\nDigite o código do aluno: "))
            for aluno in lista:
                if codigo == aluno['codigo']:
                    codigo_existe = True
                    break
            if codigo_existe:
                print("\033[31mEste código já existe!\033[m")
            else:
                input("Pressione \033[33mENTER\033[m para continuar...")
                break
        except ValueError:
            print("\033[31mCódigo inválido\033[m")

    dados_aluno['codigo'] = codigo

    lista.append(dados_aluno)

    return lista

def listar(lista):
    print("\n\033[1;33m==== LISTAR ====\033[m")

    if len(lista) > 0:
        for c in lista:  # Lista os alunos
            print(f"- {c}")
    else:  # Caso tenha alunos na lista
        print("\033[31mSem alunos cadastrados!\033[m")
    input("Pressione \033[33mENTER\033[m para continuar...")

    return lista

def atualizar(lista):
    print("\n\033[1;33m==== ATUALIZAR ====\033[m")

    if len(lista) > 0:
        while True: #Verifica se o aluno existe pelo código
            try:
                codigo_existe = False
                codigo_aluno = int(input("\nCódigo do aluno: "))
                for aluno in lista:
                    if codigo_aluno == aluno['codigo']:
                        codigo_existe = True
                        break
                if codigo_existe:
                    input("Pressione \033[33mENTER\033[m para continuar...")
                    break
                print('\033[33mAluno não encontrado\033[m')
            except ValueError:
                print("\033[33mResposta inválida\033[m")

        for aluno in lista: #Procura o código do aluno correspondente na lista
            if aluno['codigo'] == codigo_aluno:
                aluno['nome'] = input("\nNovo nome: ")
                input("Pressione \033[33mENTER\033[m para continuar...")

                aluno['cpf'] = input("\nNovo CPF: ")
                input("Pressione \033[33mENTER\033[m para continuar...")

                while True:
                    try:
                        codigo_existe = False
                        codigo = int(input("\nNovo código: "))
                        for aluno in lista:
                            if codigo == aluno['codigo']:
                                codigo_existe = True
                                break
                        if codigo_existe:
                            print("\033[31mEste código já existe!\033[m")
                        else:
                            input("Pressione \033[33mENTER\033[m para continuar...")
                            break
                    except ValueError:
                        print("\033[31mCódigo inválido\033[m")

                aluno['codigo'] = codigo

    else:
        print("\033[31mSem alunos para atualizar!\033[m")

    return lista

def excluir(lista):
    print("\n\033[1;33m==== EXCLUIR ====\033[m")

    if len(lista) > 0:
        while True:
            try:
                codigo_existe = False
                codigo_aluno = int(input("\nCódigo do aluno: "))
                for aluno in lista:
                    if codigo_aluno == aluno['codigo']:
                        codigo_existe = True
                        break
                if codigo_existe:
                    input("Pressione \033[33mENTER\033[m para continuar...")
                    break
                print('\033[33mAluno não encontrado\033[m')
            except ValueError:
                print("\033[33mResposta inválida\033[m")

        for aluno in lista:
            if aluno['codigo'] == codigo_aluno:
                lista.remove(aluno)

        print("\033[32mAluno excluído!\033[m")

    else:
        print("\033[31mSem alunos para excluir!\033[m")

    return lista

## ------------------------------------- CODIGO ------------------------------------------------------ ##
opc_principal = 0
opc_operacoes = 0
lista_alunos = []

while opc_principal != 9:
    opc_principal = menu_principal()

    if opc_principal != 9: # Se o usuário não escolheu sair
        while opc_operacoes != 9: # Repete que seja escolhido sair das operações

            if opc_principal == 1: # Escolha dos estudantes
                print("\n==== \033[33m[Estudantes]\033[m MENU DE OPERAÇÓES ====")
                opc_operacoes = menu_operacoes()

                if opc_operacoes == 1:
                    lista_alunos = incluir(lista_alunos)
                if opc_operacoes == 2:
                    lista_alunos = listar(lista_alunos)
                if opc_operacoes == 3:
                    lista_alunos = atualizar(lista_alunos)
                if opc_operacoes == 4:
                    lista_alunos = excluir(lista_alunos)

                elif opc_operacoes == 9:
                    break
                elif opc_operacoes < 1 or opc_operacoes > 4:
                    print("\033[31mOpção inválida!\033[m")

            elif opc_principal == 2:  # Escolha dos professores: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Professores]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|" + "_" * 40 + "|")
                opc_operacoes = 9

            elif opc_principal == 3:  # Escolha das disciplinas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Disciplina]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|" + "_" * 40 + "|")
                opc_operacoes = 9

            elif opc_principal == 4:  # Escolha dos turmas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Turmas]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^35}\033[m|")
                print("|" + "_" * 35 + "|")
                opc_operacoes = 9

            elif opc_principal == 5:  # Escolha dos matrículas: 'EM DESENVOLVIMENTO'
                print("\n==== \033[33m[Matrículas]\033[m MENU DE OPERAÇÓES ====")
                print(f"|\033[32m{'Em desenvolvimento...':^40}\033[m|")
                print("|" + "_" * 40 + "|")
                opc_operacoes = 9

        opc_operacoes = 0

