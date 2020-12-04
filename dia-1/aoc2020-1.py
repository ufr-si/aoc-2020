with open("input.txt","r") as file:
    
    linhas = file.readlines() # le todas as linhas e armazena em um vetor

    # percorre todos os numeros
    achou = False
    for i in range(0,len(linhas)):
        primeiro = int(linhas[i][:-1]) #pega a string, MENOS o último caracter
        for j in range(i+1,len(linhas)):
            segundo = int(linhas[j][:-1])
            # se der 2020 a soma deles, multiplique 
            # e retorne o valor multiplicado
            if (primeiro+segundo == 2020):
                print("primeira estrela: ",primeiro*segundo)
                #exit()
        

    for i in range(0,len(linhas)):
        primeiro = int(linhas[i][:-1]) #pega a string, MENOS o último caracter
        for j in range(i+1,len(linhas)):
            segundo = int(linhas[j][:-1])
            for k in range(j+1,len(linhas)):
                terceiro = int(linhas[k][:-1])
                
                # se der 2020 a soma deles, multiplique 
                # e retorne o valor multiplicado
                if (primeiro+segundo+terceiro == 2020):
                    print("segunda estrela: ",primeiro*segundo*terceiro)
                    exit()