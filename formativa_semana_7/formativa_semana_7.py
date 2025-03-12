import json

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

def incluir():
    with open("dados_semana_7.json","r") as r:
        dados = json.load(r)

    dados_aluno = {}
    print("\n\033[1;33m==== INCLUIR ====\033[m\n")

    nome = input("Nome do estudante: ")  # Escreve o nome
    input("Pressione \033[33mENTER\033[m para continuar...")  # Confirmação
    dados_aluno["nome"] = nome

    cpf = input("\nDigite seu CPF: ")
    input("Pressione \033[33mENTER\033[m para continuar...")
    dados_aluno['cpf'] = cpf

    while True: # Valida um código novo
        try:
            codigo_existe = False
            codigo = int(input("\nDigite o código do aluno: "))
            for aluno in dados['estudantes']:
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

    dados['estudantes'].append(dados_aluno)

    with open("dados_semana_7.json", "w") as w:
        json.dump(dados,w,indent=4)

def listar():
    with open("dados_semana_7.json","r") as r:
        dados = json.load(r)

    print("\n\033[1;33m==== LISTAR ====\033[m")

    if len(dados['estudantes']) > 0:
        for c in dados['estudantes']:  # Lista os alunos
            print(f"- {c}")
    else:  # Caso tenha alunos na lista
        print("\033[31mSem alunos cadastrados!\033[m")
    input("Pressione \033[33mENTER\033[m para continuar...")

    with open("dados_semana_7.json", "w") as w:
        json.dump(dados,w,indent=4)

def atualizar():
    with open("dados_semana_7.json","r") as r:
        dados = json.load(r)
    print("\n\033[1;33m==== ATUALIZAR ====\033[m")

    if len(dados['estudantes']) > 0:
        while True: #Verifica se o aluno existe pelo código
            try:
                codigo_existe = False
                codigo_aluno = int(input("\nCódigo do aluno: "))
                for aluno in dados['estudantes']:
                    if codigo_aluno == aluno['codigo']:
                        codigo_existe = True
                        break
                if codigo_existe:
                    input("Pressione \033[33mENTER\033[m para continuar...")
                    break
                print('\033[33mAluno não encontrado\033[m')
            except ValueError:
                print("\033[33mResposta inválida\033[m")

        for aluno in dados['estudantes']: #Procura o código do aluno correspondente na lista
            if aluno['codigo'] == codigo_aluno:
                aluno['nome'] = input("\nNovo nome: ")
                input("Pressione \033[33mENTER\033[m para continuar...")

                aluno['cpf'] = input("\nNovo CPF: ")
                input("Pressione \033[33mENTER\033[m para continuar...")

                while True:
                    try:
                        codigo_existe = False
                        codigo = int(input("\nNovo código: "))
                        for aluno in dados['estudantes']:
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

    with open("dados_semana_7.json", "w") as w:
        json.dump(dados,w,indent=4)

def excluir():
    with open("dados_semana_7.json","r") as r:
        dados = json.load(r)
    print("\n\033[1;33m==== EXCLUIR ====\033[m")

    if len(dados['estudantes']) > 0:
        while True:
            try:
                codigo_existe = False
                codigo_aluno = int(input("\nCódigo do aluno: "))
                for aluno in dados['estudantes']:
                    if codigo_aluno == aluno['codigo']:
                        codigo_existe = True
                        break
                if codigo_existe:
                    input("Pressione \033[33mENTER\033[m para continuar...")
                    break
                print('\033[33mAluno não encontrado\033[m')
            except ValueError:
                print("\033[33mResposta inválida\033[m")

        for aluno in dados['estudantes']:
            if aluno['codigo'] == codigo_aluno:
                dados['estudantes'].remove(aluno)

        print("\033[32mAluno excluído!\033[m")

    else:
        print("\033[31mSem alunos para excluir!\033[m")

    with open("dados_semana_7.json", "w") as w:
        json.dump(dados,w,indent=4)


## ------------------------------------- CODIGO ------------------------------------------------------ ##
opc_principal = 0
opc_operacoes = 0

while opc_principal != 9:
    opc_principal = menu_principal()

    if opc_principal != 9: # Se o usuário não escolheu sair
        while opc_operacoes != 9: # Repete que seja escolhido sair das operações

            if opc_principal == 1: # Escolha dos estudantes
                print("\n==== \033[33m[Estudantes]\033[m MENU DE OPERAÇÓES ====")
                opc_operacoes = menu_operacoes()

                if opc_operacoes == 1:
                    incluir()

                if opc_operacoes == 2:
                    listar()

                if opc_operacoes == 3:
                    atualizar()
                    
                if opc_operacoes == 4:
                    excluir()

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

