
def get_input():
    
    with open("input.txt","r") as file:
        linhas = file.readlines() # le todas as linhas e armazena em um vetor
    limpa =[]
    for linha in linhas:
        limpa.append(linha[:-1])
    return limpa


linhas = get_input()
senhas_validas = 0
senhas_validas_p_2 = 0
for linha in linhas:
    #5-12 x: dqkllgbtbrnqxgxvmj
    # min - max letra: senha
    linha_separada = linha.split(" ")
    
    #['1-2', 'w:', 'tmwqqfc']
    # 0,1,2
    aux = linha_separada[0].split("-") # min e max
    minimo = int(aux[0]) #min
    maximo = int(aux[1]) #max
    letra = linha_separada[1][:-1] # letra:
    senha = linha_separada[2] # senha
    #pesquisar na senha a quantidade de letras e chamar de n
    # SE n tiver entre min e max (inclusive)
    # senha ok
    # caso contrário, não valida
    n = senha.count(letra)
    if( n >= minimo and n <= maximo):
        senhas_validas = senhas_validas+1

    # minimo e maximo são posicoes
    pos_um = minimo
    pos_dois = maximo

    if(senha[pos_um-1] == letra):
        if(senha[pos_dois-1] != letra):
            senhas_validas_p_2 = senhas_validas_p_2+1
        
    else:
        if(senha[pos_um-1] != letra):
            if(senha[pos_dois-1] == letra):
                senhas_validas_p_2 = senhas_validas_p_2+1
    

print("parte 1:",senhas_validas)
print("parte 2:",senhas_validas_p_2)







    