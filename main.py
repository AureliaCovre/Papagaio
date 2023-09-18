
try:
    while True: 
        papagaio = input("Escolha a perna: ")
        if papagaio == "esquerda":
            print("Inglês")
        if papagaio == "direita":
            print("Francês")
        if papagaio == "nenhuma":
            print("Português")
        if papagaio == "ambas":
           print("Caiu")  
        else:
            break              
except Exception as e:
    print("ERRO no main:", str(e))
