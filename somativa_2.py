#-------------------- Raciocínio Computacional ------------------------- #
# Nome: Bruno Eiky Yamamoto                                              #
# Curso: Superior de Tecnologia em Análise e Desenvolvimento de Sistemas # 
# ---------------------------------------------------------------------- #

# (O ARQUIVO .JSON É CRIADO AO INICIAR O CÓDIGO) #

import json 

def criar_arquivo():
    dados = {
                "estudantes": [],
                "professores":[],
                "disciplinas":[],
                "turmas":[],
                "matriculas":[]
            }
    
    with open("somativa_2.json","w") as w:
        json.dump(dados,w,indent=4)

def operacao(opc_operacoes,opc_principal):

    if opc_operacoes == 1:
        incluir(opc_principal)

    if opc_operacoes == 2:
        listar(opc_principal)

    if opc_operacoes == 3:
        atualizar(opc_principal)
        
    if opc_operacoes == 4:
        excluir(opc_principal)

    elif opc_operacoes == 9:
        return 9

    elif opc_operacoes < 1 or opc_operacoes > 4:
        print("\033[31mOpção inválida!\033[m")
        
## ------------------------------------- MENUS ------------------------------------------------------ ##

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


## ------------------------------------- CODIGOS ------------------------------------------------------ ##

def codigo_existente(esc):
    with open("somativa_2.json","r") as r:
        dados = json.load(r)

    palavra = esc #Apenas para formatar o nome da categoria escolhida
    if esc == "professores":
        palavra = palavra.rstrip('es')
    else:
        palavra = palavra.rstrip('s')

    while True: #Verifica se o aluno existe pelo código
            try:
                codigo_existe = False
                codigo_aluno = int(input(f"\nCódigo do(a) \033[1;4m{palavra}\033[m: "))
                for categoria in dados[esc]:
                    if codigo_aluno == categoria['codigo']:
                        codigo_existe = True
                        break
                if codigo_existe:
                    input("Pressione \033[33mENTER\033[m para continuar...")
                    break
                print(f'\033[33m{palavra} não encontrado(a)\033[m')
            except ValueError:
                print("\033[33mResposta inválida\033[m")

    return codigo_aluno

def codigo_novo(esc):
    with open("somativa_2.json","r") as r:
        dados = json.load(r)

    palavra = esc #Apenas para formatar o nome da categoria escolhida
    if esc == "professores":
        palavra = palavra.rstrip('es')
    else:
        palavra = palavra.rstrip('s')

    while True: # Valida um código novo
        try:
            codigo_existe = False
            codigo = int(input(f"\nDigite o código do(a) \033[1;4m{palavra}\033[m: "))
            for categoria in dados[esc]:
                if codigo == categoria['codigo']:
                    codigo_existe = True
                    break
            if codigo_existe:
                print("\033[31mEste código já existe!\033[m")
            else:
                input("Pressione \033[33mENTER\033[m para continuar...")
                break
        except ValueError:
            print("\033[31mCódigo inválido\033[m")

    return codigo
## ------------------------------------- INCLUIR ------------------------------------------------------ ##

def incluir(categoria):
    with open("somativa_2.json","r") as r:
        dados = json.load(r)
    print("\n\033[1;33m==== INCLUIR ====\033[m\n")

    if categoria == 1:
        dados_aluno = {}
        
        nome = input("Nome do estudante: ")  # Escreve o nome
        input("Pressione \033[33mENTER\033[m para continuar...")  # Confirmação
        dados_aluno["nome"] = nome

        cpf = input("\nDigite seu CPF: ")
        input("Pressione \033[33mENTER\033[m para continuar...")
        dados_aluno['cpf'] = cpf

        codigo = codigo_novo("estudantes")
        dados_aluno['codigo'] = codigo

        dados['estudantes'].append(dados_aluno)

    elif categoria == 2:
        dados_professor = {}

        nome = input("Nome do professor: ")  # Escreve o nome
        input("Pressione \033[33mENTER\033[m para continuar...")  # Confirmação
        dados_professor["nome"] = nome

        cpf = input("\nDigite seu CPF: ")
        input("Pressione \033[33mENTER\033[m para continuar...")
        dados_professor['cpf'] = cpf

        codigo = codigo_novo("professores")
        dados_professor['codigo'] = codigo

        dados['professores'].append(dados_professor)

    elif categoria == 3:
        dados_disciplinas = {}

        nome = input("Nome do disciplinas: ")  # Escreve o nome
        input("Pressione \033[33mENTER\033[m para continuar...")  # Confirmação
        dados_disciplinas["nome"] = nome

        codigo = codigo_novo("disciplinas")
        dados_disciplinas['codigo'] = codigo

        dados['disciplinas'].append(dados_disciplinas)

    elif categoria == 4:
        if len(dados['professores']) > 0 and len(dados['disciplinas']) > 0:

            dados_turmas = {}

            codigo_turma = codigo_novo("turmas")
            dados_turmas['codigo'] = codigo_turma

            codigo_professor = codigo_existente("professores")
            dados_turmas['codigo_professor'] = codigo_professor

            codigo_disciplina = codigo_existente("disciplinas")
            dados_turmas['codigo_disciplina'] = codigo_disciplina

            dados['turmas'].append(dados_turmas)
        else:
            print(f"\033[31mNecessário o cadastro de pelo menos 1 professor/disciplina!\033[m")

    elif categoria == 5:
        if len(dados['turmas']) > 0 and len(dados['estudantes']) > 0:

            dados_turmas = {}
            dados_matricula = {}

            codigo_turma = codigo_existente("turmas")
            dados_matricula['codigo_turma'] = codigo_turma

            codigo_estudante = codigo_existente("estudantes")
            dados_matricula['codigo'] = codigo_estudante 

            dados['matriculas'].append(dados_matricula)
        else:
            print(f"\033[31mNecessário o cadastro de pelo menos 1 turma/estudante!\033[m")

    with open("somativa_2.json", "w") as w:
        json.dump(dados,w,indent=4)
## ------------------------------------- LISTAR ------------------------------------------------------ ##

def listar(categoria):
    with open("somativa_2.json","r") as r:
        dados = json.load(r)

    print("\n\033[1;33m==== LISTAR ====\033[m")

    if categoria == 1:

        if len(dados['estudantes']) > 0:
            print(f"\033[34m{'Cod.':<5}{'CPF':<15}{'Nome'}\033[m")

            for c in dados['estudantes']:  # Lista os alunos
                print(f"{c['codigo']:<5}{c['cpf']:<15}{c['nome']}")

        else:  # Caso tenha alunos na lista
            print("\033[31mSem alunos cadastrados!\033[m")
        input("Pressione \033[33mENTER\033[m para continuar...")

    elif categoria == 2:

        if len(dados['professores']) > 0:
            print(f"\033[34m{'Cod.':<5}{'CPF':<15}{'Nome'}\033[m")

            for c in dados['professores']:  # Lista os professores
                print(f"{c['codigo']:<5}{c['cpf']:<15}{c['nome']}")

        else:  # Caso tenha professores na lista
            print("\033[31mSem professores cadastrados!\033[m")
        input("Pressione \033[33mENTER\033[m para continuar...")

    elif categoria == 3:

        if len(dados['disciplinas']) > 0:
            print(f"\033[34m{'Cod.':<5}{'Nome'}\033[m")

            for c in dados['disciplinas']:  # Lista os professores
                print(f"{c['codigo']:<5}{c['nome']}")

        else:  # Caso tenha disciplinas na lista
            print("\033[31mSem disciplinas cadastradas!\033[m")
        input("Pressione \033[33mENTER\033[m para continuar...")
    
    elif categoria == 4:

        if len(dados['turmas']) > 0:
            print(f"\033[34m{'Cod.Turma':<12}{'Cod.Prof':<10}{'Cod.Disciplina'}\033[m")

            for c in dados['turmas']:  # Lista os professores
                print(f"{c['codigo']:<12}{c['codigo_professor']:<10}{c['codigo_disciplina']}")

        else:  # Caso tenha turmas na lista
            print("\033[31mSem turmas cadastradas!\033[m")
        input("Pressione \033[33mENTER\033[m para continuar...")

    elif categoria == 5: 

        if len(dados['matriculas']) > 0:
            print(f"\033[34m{'Cod.Turma':<12}{'Cod.Estudante':<10}\033[m")

            for c in dados['matriculas']:  # Lista os professores
                print(f"{c['codigo_turma']:<12}{c['codigo']}")

        else:  # Caso tenha matriculas na lista
            print("\033[31mSem matriculas cadastradas!\033[m")
        input("Pressione \033[33mENTER\033[m para continuar...")

    with open("somativa_2.json", "w") as w:
        json.dump(dados,w,indent=4)
## ------------------------------------- ATUALIZAR ------------------------------------------------------ ##

def atualizar(categoria):
    with open("somativa_2.json","r") as r:
        dados = json.load(r)
    print("\n\033[1;33m==== ATUALIZAR ====\033[m")

    if categoria == 1:
        if len(dados['estudantes']) > 0:
            codigo_aluno = codigo_existente("estudantes")

            for aluno in dados['estudantes']: #Procura o código do aluno correspondente na lista
                if aluno['codigo'] == codigo_aluno:
                    aluno['nome'] = input("\nNovo nome: ")
                    input("Pressione \033[33mENTER\033[m para continuar...")

                    aluno['cpf'] = input("\nNovo CPF: ")
                    input("Pressione \033[33mENTER\033[m para continuar...")

                    codigo = codigo_novo('estudantes')
                    aluno['codigo'] = codigo
        else:
            print("\033[31mSem alunos para atualizar!\033[m")

    elif categoria == 2:
        if len(dados['professores']) > 0:
            codigo_professor = codigo_existente("professores")

            for professor in dados['professores']: #Procura o código do professor correspondente na lista
                if professor['codigo'] == codigo_professor:
                    professor['nome'] = input("\nNovo nome: ")
                    input("Pressione \033[33mENTER\033[m para continuar...")

                    professor['cpf'] = input("\nNovo CPF: ")
                    input("Pressione \033[33mENTER\033[m para continuar...")

                    codigo = codigo_novo('professores')
                    professor['codigo'] = codigo
        else:
            print("\033[31mSem professores para atualizar!\033[m")

    elif categoria == 3:
        if len(dados['disciplinas']) > 0:
            codigo_disciplina = codigo_existente("disciplinas")

            for disciplina in dados['disciplinas']: #Procura o código da disciplina correspondente na lista
                if disciplina['codigo'] == codigo_disciplina:
                    disciplina['nome'] = input("\nNova disciplina: ")
                    input("Pressione \033[33mENTER\033[m para continuar...")

                    codigo = codigo_novo('disciplinas')
                    disciplina['codigo'] = codigo
        else:
            print("\033[31mSem disciplinas para atualizar!\033[m")

    elif categoria == 4:
            
        if len(dados['professores']) > 0 and len(dados['disciplinas']) > 0:

            if len(dados['turmas']) > 0:
                codigo_turma = codigo_existente("turmas")

                for turma in dados['turmas']: #Procura o código da turma correspondente na lista
                    if turma['codigo'] == codigo_turma:
                        codigo = codigo_novo('turmas')
                        turma['codigo'] = codigo

                        codigo_professor = codigo_existente('professores')
                        turma['codigo_professor'] = codigo_professor

                        codigo_disciplina = codigo_existente('disciplinas')
                        turma['codigo_disciplina'] = codigo_disciplina
            else:
                print("\033[31mSem disciplinas para atualizar!\033[m")
                
        else:
            print(f"\033[31mNecessário o cadastro de pelo menos 1 professor/disciplina!\033[m")

    elif categoria == 5:
        
        if len(dados['turmas']) > 0 and len(dados['estudantes']) > 0:

            if len(dados['matriculas']) > 0:
                codigo_matricula = codigo_existente("matriculas")

                for matricula in dados['matriculas']: #Procura o código da matricula correspondente na lista
                    if matricula['codigo'] == codigo_matricula:
                        codigo = codigo_existente('turmas')
                        matricula['codigo_turma'] = codigo

                        codigo_professor = codigo_existente('estudantes')
                        matricula['codigo'] = codigo_professor
            else:
                print("\033[31mSem matriculas para atualizar!\033[m")

        else:
            print(f"\033[31mNecessário o cadastro de pelo menos 1 turma/estudante!\033[m")


    with open("somativa_2.json", "w") as w:
        json.dump(dados,w,indent=4)

## ------------------------------------- EXCLUIR ------------------------------------------------------ ##

def excluir(categoria):
    with open("somativa_2.json","r") as r:
        dados = json.load(r)
    print("\n\033[1;33m==== EXCLUIR ====\033[m")

    if categoria == 1:
        if len(dados['estudantes']) > 0:
            codigo_aluno = codigo_existente('estudantes')

            for aluno in dados['estudantes']:
                if aluno['codigo'] == codigo_aluno:
                    dados['estudantes'].remove(aluno)

            print("\033[32mAluno excluído!\033[m")

        else:
            print("\033[31mSem alunos para excluir!\033[m")
    
    elif categoria == 2:
        if len(dados['professores']) > 0:
            codigo_professor = codigo_existente('professores')

            for professor in dados['professores']:
                if professor['codigo'] == codigo_professor:
                    dados['professores'].remove(professor)

            print("\033[32mProfessor excluído!\033[m")

        else:
            print("\033[31mSem professores para excluir!\033[m")
    
    elif categoria == 3:
        if len(dados['disciplinas']) > 0:
            codigo_disciplina = codigo_existente('disciplinas')

            for disciplina in dados['disciplinas']:
                if disciplina['codigo'] == codigo_disciplina:
                    dados['disciplinas'].remove(disciplina)

            print("\033[32mDisciplina excluída!\033[m")

        else:
            print("\033[31mSem disciplinas para excluir!\033[m")

    elif categoria == 4:
        if len(dados['turmas']) > 0:
            codigo_turma = codigo_existente('turmas')

            for turma in dados['turmas']:
                if turma['codigo'] == codigo_turma:
                    dados['turmas'].remove(turma)

            print("\033[32mTurma excluída!\033[m")

        else:
            print("\033[31mSem turmas para excluir!\033[m")

    elif categoria == 5:
        if len(dados['matriculas']) > 0:
            codigo_matricula = codigo_existente('matriculas')

            for matricula in dados['matriculas']:
                if matricula['codigo'] == codigo_matricula:
                    dados['matriculas'].remove(matricula)

            print("\033[32mMatricula excluída!\033[m")

        else:
            print("\033[31mSem matriculas para excluir!\033[m")


    with open("somativa_2.json", "w") as w:
        json.dump(dados,w,indent=4)

## ------------------------------------- MAIN ------------------------------------------------------ ##
opc_principal = 0
opc_operacoes = 0

try:
    with open("somativa_2.json","r") as r:
        dados = json.load(r)
except FileNotFoundError:
    criar_arquivo()

while opc_principal != 9:
    opc_principal = menu_principal()

    if opc_principal != 9: # Se o usuário não escolheu sair
        while opc_operacoes != 9: # Repete que seja escolhido sair das operações

            if opc_principal == 1: # Escolha dos estudantes
                print("\n==== \033[33m[Estudantes]\033[m MENU DE OPERAÇÓES ====")
                opc_operacoes = menu_operacoes()

                operacoes = operacao(opc_operacoes,opc_principal)

                if operacoes == 9:
                    break

            elif opc_principal == 2:  # Escolha dos professores
                print("\n==== \033[33m[Professores]\033[m MENU DE OPERAÇÓES ====")
                opc_operacoes = menu_operacoes()

                operacoes = operacao(opc_operacoes,opc_principal)

                if operacoes == 9:
                    break

            elif opc_principal == 3:  # Escolha das disciplinas
                print("\n==== \033[33m[Disciplina]\033[m MENU DE OPERAÇÓES ====")
                opc_operacoes = menu_operacoes()

                operacoes = operacao(opc_operacoes,opc_principal)

                if operacoes == 9:
                    break

            elif opc_principal == 4:  # Escolha dos turmas
                print("\n==== \033[33m[Turmas]\033[m MENU DE OPERAÇÓES ====")
                opc_operacoes = menu_operacoes()

                operacoes = operacao(opc_operacoes,opc_principal)

                if operacoes == 9:
                    break

            elif opc_principal == 5:  # Escolha dos matrículas
                print("\n==== \033[33m[Matrículas]\033[m MENU DE OPERAÇÓES ====")
                opc_operacoes = menu_operacoes()

                operacoes = operacao(opc_operacoes,opc_principal)

                if operacoes == 9:
                    break

        opc_operacoes = 0


