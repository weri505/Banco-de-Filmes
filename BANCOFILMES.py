def opção_menu():
    print(30*"-")
    print("            PyFlix")
    print(30*"-")
    print("< 1 > - para adicionar filme :")
    print("< 2 > - para listar filme :")
    print("< 3 > - para buscar filme :")
    print("< 4 > - para atualizar filme :")
    print("< 5 > - para remover filme:")
    print(30*"-")
    opção=(input("digite a opção que deseja executar :"))      #Recebemos o valor referente a opção que for desejada.
    
    if opção.isnumeric():                                      #Se o valor recebido for numérico, faremos o que explicarei abaixo.
            opção = int(opção)                                 #Tranformamos o valor numérico em um inteiro, só pra garantir.
            return opção                                       #Retorna a opção
        
    else:                                                      #Se não for numérico, printamos "Opção inválida.".
            print("Opção inválida.")        

        

        
    


#funções
def adicionar():
    print(30*"-")
    titulo     = input("digite o titulo do filme:")            #Recebemos o novo título.
    ano       = input("digite o ano do filme :")               #Recebemos o novo ano.
    genero = input("digite o genero do filme :")               #Recebemos o novo gênero.
    diretor  = input("digite o nome do diretor :")             #Recebemos o novo diretor.
    print(30*"-")
    filme     = [titulo,ano,genero,diretor]                    #Aqui acrescentamos os valores recebidos em uma lista.
    armazenamento_de_filmes.append(filme)                      #Aqui mandamos essa lista para a lista principal de filmes.
    print(f"o filme {titulo} foi adicionado com sucesso : ")
    print(f" nome do filme: {titulo} \n Ano de lançamento: {ano}\n Genero: {genero}\n diretor: {diretor}")
    



def listar():                                                  #Aqui listaremos todos os filmes e suas informações.
    for filme in armazenamento_de_filmes:                      #"Correremos" no armazenamento principal de filmes para lista-los.
        print(f" informações:\n\n titulo: {filme[0]}\n o ano: {filme[1]}\n genero: {filme[2]}\n diretor: {filme[3]} ")   #Aqui listamos as informações.
    if armazenamento_de_filmes ==[]:
            print("o catalogo esta vazio. \n\n ")              #Se não tiver nada no armazenamento, printamos isso.
    
    









def buscar():                                                  #Função de pesquisa de filmes.
    print(30*"-")
    titulo = input("Digite o título do filme a ser pesquisado (para cancelar digite [p]): ").lower() 
    
    if titulo == "p":
        print("Você cancelou a operação.")
    

    titulo_min = titulo.lower()                                #Tranformamos o titulo para minúsculo.


    filmes_encontrados = []                                    #Criamos uma lista 
    for filme in armazenamento_de_filmes:
        titulo_filme_min = filme[0].lower() #Aqui transformamos o titulo do filme em minúsculo.
    if titulo_min in titulo_filme_min:
        filmes_encontrados.append(filme)
        return print(f" informações:\n\n titulo: {filme[0]}\n o ano: {filme[1]}\n genero: {filme[2]}\n diretor: {filme[3]} ")  #Se o título minúsculo estiver dentro da variável que recebe os filmes minúsculo, ele vai adicionar o filme e printar as informações.


    
 
    else:
        print("Filmes não encontrados.")


    





def atualizar():     #Aqui vamos atualizar os filmes.
    titulo = str(input("digite o filme que deseja atualizar: "))
    ano = int(input("Digite o novo ano: "))
    genero = str(input("Digite o novo gênero: "))
    diretor = str(input("Digite o novo diretor: "))
    filme = [titulo, ano, genero, diretor]#Até agora só recebemos as informações e acrescentamos na lista "filme".

    if ano > 2024:
        print("ano inválido") #Evitando datas mentirosas.

    armazenamento_de_filmes = armazenamento_de_filmes.append(filme)
    print("filme atualizado com sucesso!")   #Agora acrescentamos as informações do filme na lista principal de armazenamento dos filmes.

    opção_menu()

    
    


    
        



def remover():
    global armazenamento_de_filmes
    
    
    for filme in armazenamento_de_filmes:
        filme_removido = str(input("digite o filme que deseja remover:"))
        if filme_removido in armazenamento_de_filmes:
           armazenamento_de_filmes = armazenamento_de_filmes.remove(filme_removido)
        else:
            print("filme não existente")   #Bom, pedimos para o usuário digitar o filme que deseja remover e, se estiver no armazenamento de filmes, o filme será removido. O global permitiu que alterassemos o valor global do armazenamento
            opção_menu()

    return print(armazenamento_de_filmes) 
        

            
    
        
    
   
    



#lista

armazenamento_de_filmes=[]
while True:
    p = opção_menu()
    
    if p == 1:
        adicionar()   #Redirecionamos para a função adicionar.
    if p == 2:
        listar()          #Redirecionamos para a função listar.
    if p == 3:
        buscar()       #Redirecionamos para a função buscar.
    if p == 4:
        atualizar()    #Redirecionamos para a função atualizar.
    if p == 5:
        remover()     #Redirecionamos para a função remover.



