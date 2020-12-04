def get_input(input):
    
    with open(input,"r") as file:
        linhas = file.readlines() # le todas as linhas e armazena em um vetor
    limpa =[]
    for linha in linhas:
        limpa.append(linha[:-1])
    return limpa

linhas = get_input("input.txt")

new_linha = []
for linha in linhas:
    linha = linha*100
    new_linha.append(linha)

linhas = new_linha


#tamanho_linha = len(linhas[0])

def verifica_arvores(linhas,direita,baixo):
    limite = len(linhas)
    i = 0
    posicao = 0 
    total_arvores = 0 
    

    while i < limite-1:
        # 3 posicoes pra direita, 1 pra baixo
        
        # contando quantas arvores tem 3 posicoes
        # pra direita
        # total_arvores = linha.count("#",posicao+1,posicao+4)
        
        posicao = posicao +direita

        # if (posicao > tamanho_linha-1):
        #     #"zerar" posicao
        #     print("zerando")
        #     posicao = tamanho_linha-posicao
        i = i+baixo
        #contando quantas arvores tem 1 pra baixo
        linha = linhas[i]
        # print(posicao)

        # Right 1, down 1.
        # Right 3, down 1. (This is the slope you already checked.)
        # Right 5, down 1.
        # Right 7, down 1.
        # Right 1, down 2.

        if(linha[posicao] == "#"):
            total_arvores = total_arvores+1
    return total_arvores

#In the above example, 
# these slopes would 
# find 2, 7, 3, 4, and
#  2 tree(s) respectively; multiplied together,
#  these produce the answer 336.

total = verifica_arvores(linhas,1,1)*verifica_arvores(linhas,3,1)*verifica_arvores(linhas,5,1)*verifica_arvores(linhas,7,1)*verifica_arvores(linhas,1,2)

print(total)