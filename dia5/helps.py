def get_input(entrada):    
    with open(entrada,"r") as file:
        linhas = file.readlines() # le todas as linhas e armazena em um vetor
    limpa =[]
    for linha in linhas:
        limpa.append(linha[:-1])
    return limpa