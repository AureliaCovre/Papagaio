""" Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português.
Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, amigo de
Humberto, ficou fascinado com o animal. Em sua emoção disse: “E quando ele levanta as duas?”. Antes que Humberto
pudesse responder, o papagaio restrito: “Aí eu caio, idiota!”. Entrada: A entrada consiste de diversos casos de 
teste . Cada caso de teste consiste em uma string informando qual a situação de levantamento de pernas do 
papagaio. Saída: Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará.
Caso ele levante ambas as pernas, imprima “caiu”. Quebre uma linha a cada caso de teste.
 
 Entrada   |   Saída 
 esquerda --> inglês
 direita  --> francesa 
 nenhuma  --> portugues 
 ambas    --> caiu       """

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
