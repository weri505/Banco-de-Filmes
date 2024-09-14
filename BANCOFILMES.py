

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
    print(30*"-")
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
    titulo = str(input("digite o filme que deseja atualizar: "))
    ano = int(input("digite o filme que deseja atualizar: "))
    genero = str(input("digite o filme que deseja atualizar: "))
    diretor = str(input("digite o filme que deseja atualizar: "))
    filme = [titulo, ano, genero, diretor]

    if ano > 2024:
        print("ano inválido")

    armazenamento_de_filmes = armazenamento_de_filmes.append(filme)
    print("filme atualizado com sucesso!")

    opção_menu()

    
    


    
        



def remover():
    global armazenamento_de_filmes
    
    
    for filme in armazenamento_de_filmes:
        filme_removido = str(input("digite o filme que deseja remover:"))
        if filme_removido in armazenamento_de_filmes:
           armazenamento_de_filmes = armazenamento_de_filmes.remove(filme_removido)
        else:
            print("filme não existente")
            opção_menu()

    return print(armazenamento_de_filmes) 
        

            
    
        
    
   
    



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

