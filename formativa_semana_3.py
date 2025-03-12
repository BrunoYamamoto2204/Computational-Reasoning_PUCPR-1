

menu_principal=0
menu_operacoes=0

while menu_principal != 9:
    while True:
        print("---- MENU PRINCIPAL ---")
        try:
            menu_principal = int(input("""
\033[33m(1) \033[34mGerenciar estudantes.\033[m
\033[33m(2) \033[34mGerenciar professores.\033[m
\033[33m(3) \033[34mGerenciar disciplinas.\033[m
\033[33m(4) \033[34mGerenciar turmas.\033[m
\033[33m(5) \033[34mGerenciar matrículas.\033[m
\033[33m(9) \033[34mSair.\033[m

Informe a opção desejada: """))
            if menu_principal > 0 and menu_principal < 6 or menu_principal == 9:
                break 
            else:
                print("\033[31mOpção inválida!\033[m")
        except:
            print("\033[31mOpção inválida!\033[m")

    if menu_principal != 9:
        print()
        if menu_principal == 1:
            print("==== \033[33m[Estudantes]\033[m MENU DE OPERAÇÓES ====")
        if menu_principal == 2:
            print("==== \033[33m[Professores]\033[m MENU DE OPERAÇÓES ====")
        if menu_principal == 3:
            print("==== \033[33m[Disciplina]\033[m MENU DE OPERAÇÓES ====")
        if menu_principal == 4:
            print("==== \033[33m[Turmas]\033[m MENU DE OPERAÇÓES ====")
        if menu_principal == 5:
            print("==== \033[33m[Matrículas]\033[m MENU DE OPERAÇÓES ====")

        while menu_operacoes != 9:
            try:
                menu_operacoes = int(input("""
\033[33m(1) \033[34mIncluir\033[m
\033[33m(2) \033[34mListar\033[m
\033[33m(3) \033[34mAtualizar\033[m
\033[33m(4) \033[34mExcluir\033[m
\033[33m(9) \033[34mVoltar ao menu principal\033[m

Informe a ação desejada: """))            

                if menu_operacoes < 1 or menu_operacoes < 5:
                    if menu_operacoes == 1:
                        print("\n\033[1;33m==== INCLUINDO ====\033[m")
                        print("\033[32mAplicação Finalizada...\033[m")
                    if menu_operacoes == 2:
                        print("\n\033[1;33m==== LISTANDO ====\033[m")
                        print("\033[32mAplicação Finalizada...\033[m")
                    if menu_operacoes == 3:
                        print("\n\033[1;33m==== ATUALIZANDO ====\033[m")
                        print("\033[32mAplicação Finalizada...\033[m")
                    if menu_operacoes == 4:
                        print("\n\033[1;33m==== EXCLUINDO ====\033[m")
                        print("\033[32mAplicação Finalizada...\033[m")
                elif menu_operacoes == 9:
                    break
                else:
                    print("\033[31mOpção inválida!\033[m")

            except:
                print("\033[31mOpção inválida!\033[m")

