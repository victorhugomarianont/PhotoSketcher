import funcs
import os
r = True
command = ""
def inform_file():
    f = input("informe o arquivo que passará \
    \n por alteração: (certifique-se de que esteja na raiz do programa)")
    if (os.path.isfile(f)):
        return f
    else:
        
        return 0

def menu():
    
    print("1. rascunho")
    print("2.Desenho")
    print("3.Efeito de foto antiga")
    print("4. Ajuda")
    print("5.Sair\n")
    
    print("Selecione alguma das opções acima para \
    \n modificar imagens ou sair: \n")
    return 1

def run_app():
    while r == True:
        menu()
        command = input("").lower()
        # Note que apenas a função sketch está devidamente hailitada
        if command == "1" or command == "rascunho":
            f = inform_file()
            print(f)
            if f != 0:
                funcs.sketch(f)
        elif command == "2" or command == "desenho":
            f = inform_file()
            print (f)
            if f != 0:
                funcs.colored_draw(f)
        elif command == "3" or command == "foto antiga":
            pass
        elif command == "4" or command == "ajuda":
            pass
            
        
    
print(run_app())