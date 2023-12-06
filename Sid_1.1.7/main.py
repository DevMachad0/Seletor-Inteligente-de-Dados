import time
#Menu

def sid_menu():

    print("================ Menu SID ======================")
    print("1 Para realizar solicitação(Dia 1)")
    print("2 para realizar solicitação(Dia 2)")
    print("3 Para realizar download")
    print("4 Para sair")
    print("Versão 1.1.7")
    print("================================================")

while True:
    sid_menu()
    choice = input("Digite o número da opção desejada: ")

    if choice == "1":
        

            print("====Selecione o modulo====")
            print("1 Procuração CNPJ")
            print("2 Procuração CPF")
            print("3 SeletorT")
            print("=========================")
            key = input("Digite o número da opção desejada: ")

            if key == "1":
                import Solicitadores.solicitar_cnpj as sc
                sc.main()
                break
            elif key == "2":
                import Solicitadores.solicitar_cpf as sf
                sf.main()
                break
            elif key == "3":
                import Solicitadores.solicitarT as st
                st.main()
                break
            else:
                print("Número invalido. Digite um número entre 1 e 3.")
    elif choice == "2":
            print("====Selecione o modulo====")
            print("1 Procuração CNPJ")
            print("2 Procuração CPF")
            print("3 SeletorT")
            print("=========================")
            key2 = input("Digite o número da opção desejada: ")

            if key2 == "1":
                 import solicitadores_dia_dois.solicitar2_cnpj as sc2
                 sc2.main()
                 break
            elif key2 == "2":
                 import solicitadores_dia_dois.solicitar2_cpf as sf2
                 sf2.main
                 break
            elif key2 == "3":
                 import solicitadores_dia_dois.solicitar2_T as st
                 st.main()
                 break
            else:
                 print("Número invalido. Digite um número entre 1 e 3.")
                 
    elif choice == "3":
            print("====Selecione o modulo====")
            print("1 Procuração CNPJ")
            print("2 Procuração CPF")
            print("3 SeletorT")
            print("=========================")
            key3 = input("Digite o número da opção desejada: ")
            
            if key3 == "1":
                 import Download.download_cnpj as dc
                 dc.main()
            elif key3 == "2":
                import Download.download_cpf as df
                df.main()
            elif key3 == "3":
                 import Download.download_seletorT as ds
                 ds.main() 
            else:
                print("Número invalido. Digite um número entre 1 e 3.")
    elif choice == "4":
         print ("Obrigado por usar o SID :)")
         time.sleep(5)
         quit()
        
    else:
        print("Número invalido. Digite um número entre 1 e 3.")