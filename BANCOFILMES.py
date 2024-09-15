

#menu
def opção_menu():
    print(30*"-")
    print("PyFlix")
    print(30*"-")
    print("< 1 > - para adicionar filme :")
    print("< 2 > - para listar filme :")
    print("< 3 > - para buscar filme :")
    print("< 4 > - para atualizar filme :")
    print("< 5 > - para remover filme:")
    print(30*"-")
    opção=int(input("digite a opção que deseja executar :"))
    return(opção) 


#funções
def adicionar():
    
    titulo=input("digite o titulo do filme:")
    ano=input("digite o ano do filme :")
    genero=input("digite o genero do filme :")
    diretor=input("digite o nome do diretor :")
    print(30*"-")
    filme=[titulo,ano,genero,diretor]
    armazenamento_de_filmes.append(filme)
    print(f"o filme {titulo} foi adicionado com sucesso : ")
    print(f" nome do filme: {titulo} \n Ano de lançamento: {ano}\n Genero: {genero}\n diretor: {diretor}")
    



def listar():
    for filme in armazenamento_de_filmes:
        print(f" informações:\n\n titulo: {filme[0]}\n o ano: {filme[1]}\n genero: {filme[2]}\n diretor: {filme[3]} ")
    if armazenamento_de_filmes ==[]:
            print("o catalogo esta vazio :")
    
    









def buscar():
    pass
    
    
    





def atualizar():
    titulo = input("digite o filme que deseja atualizar: ")
    for filme in armazenamento_de_filmes:
        if filme[0].lower() == titulo.lower():
            novo_titulo = input("digite o novo título do filme: ")
            novo_ano = input("digite o novo ano do filme: ")
            novo_genero = input("digite o novo gênero do filme: ")
            novo_diretor = input("digite o novo diretor do filme: ")

            filme[0] = novo_titulo
            filme[1] = novo_ano
            filme[2] = novo_genero
            filme[3] = novo_diretor

            print(f"Filme {titulo} atualizado com sucesso")
            return

    print("Filme não encontrado")
                  
    

       

    
    


    
        



def remover():
    nova_lista = armazenamento_de_filmes.copy()
    for filme in nova_lista:
        filme_removido = str(input("digite o filme que deseja remover: " )).lower()
        for filme in nova_lista:
                if filme[0] == filme_removido:
                    nova_lista = nova_lista.remove(filme[0])
                return nova_lista
        else:
            print("filme não existente")
            
        
     
    


    
        

            
    
        
    
   
    



#lista


armazenamento_de_filmes=[]


while True:
    p = opção_menu()
    
    if p == 1:
        adicionar()
    if p == 2:
        listar()
    if p == 3:
        buscar()
    if p == 4:
        atualizar()
    if p == 5:
        remover()

