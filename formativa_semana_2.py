print("---- MENU PRINCIPAL ---")
escolha_dados = int(input("""
\033[33m(1) \033[34mGerenciar estudantes.\033[m
\033[33m(2) \033[34mGerenciar professores.\033[m
\033[33m(3) \033[34mGerenciar disciplinas.\033[m
\033[33m(4) \033[34mGerenciar turmas.\033[m
\033[33m(5) \033[34mGerenciar matrículas.\033[m
\033[33m(9) \033[34mSair.\033[m

Informe a opção desejada: """))

print()
if escolha_dados == 1:
    print("==== \033[33m[Estudantes]\033[m MENU DE OPERAÇÓES ====")
if escolha_dados == 2:
    print("==== \033[33m[Professores]\033[m MENU DE OPERAÇÓES ====")
if escolha_dados == 3:
    print("==== \033[33m[Disciplina]\033[m MENU DE OPERAÇÓES ====")
if escolha_dados == 4:
    print("==== \033[33m[Turmas]\033[m MENU DE OPERAÇÓES ====")
if escolha_dados == 5:
    print("==== \033[33m[Matrículas]\033[m MENU DE OPERAÇÓES ====")

crud = int(input("""
\033[33m(1) \033[34mIncluir\033[m
\033[33m(2) \033[34mListar\033[m
\033[33m(3) \033[34mAtualizar\033[m
\033[33m(4) \033[34mExcluir\033[m
\033[33m(9) \033[34mVoltar ao menu principal\033[m

Informe a ação desejada: """))
if crud == 1:
    print("\n\033[1;33m==== INCLUINDO ====\033[m")
if crud == 2:
    print("\n\033[1;33m==== LISTANDO ====\033[m")
if crud == 3:
    print("\n\033[1;33m==== ATUALIZANDO ====\033[m")
if crud == 4:
    print("\n\033[1;33m==== EXCLUINDO ====\033[m")
print("\033[32mFinalizando aplicação...\033[m")


