import helps as h # importa e chama de h
linhas = h.get_input("input.txt")




# assentos_ocupados = []
mapa_assentos = []
for i in range(0,128):
    mapa_assentos.append([0,0,0,0,0,0,0,0])

lista_ids = []
for linha in linhas:
    fileira = linha[:7]
    assento = linha[7:]

    
    #particionamento binário de espaços
    # 128 fileiras
    # 0 a 127    
    inicio = 0
    fim = 127 

    tamanho = 128
    for f in fileira:
        if(f == "B"):
            inicio = inicio+(tamanho/2)
        else:
            if(f =="F"):
                fim = fim - tamanho/2
        tamanho = tamanho/2
       
    n_fileira = int(fim)
    
    inicio = 0
    fim = 7 
    tamanho = 8
    
    
    for a in assento:
        if(a == "R"):
            inicio = inicio + (tamanho/2)
        else:
            if(a =="L"):
                fim = fim - tamanho/2
        tamanho = tamanho/2
    n_assento = int(fim)

    mapa_assentos[n_fileira][n_assento] = 1



for i in range(0,128):
    print("i:",i)
    print(mapa_assentos[i])
    chaveia = False
    print("") 
    for j in range(0,8):
        if(not chaveia):
            if(mapa_assentos[i][j]==1):
                chaveia=True
        elif(mapa_assentos[i][j]==0):
            print("assento disponível: ",i,j)
            res = i*8+j
            print("resultado: ",res)
            exit()
    
    
        # Every seat also has a unique seat ID:
        # multiply the row by 8,
        # then add the column.
    res = (n_fileira *8)+n_assento
    
    lista_ids.append(res)
    
print("resultado final: ",max(lista_ids))

