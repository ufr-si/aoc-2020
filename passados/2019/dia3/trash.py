import helps as h # importa e chama de h
import numpy as np
linhas = h.get_input("input.txt")

#vamos criar uma matriz bem grandez
# Creates a list containing 50000 lists, each of 50000 items, all set to 0
tam = 80000
matrix = np.zeros((tam,tam))
meio = int(tam/2)
x = meio
y = meio
menorDist = 999999

def direita(x,y,passo):
    # percorre em +x,retorna posicoes novas
    x = x+1
    final = x+passo
    while(x<=final):
        print(matrix[x][y])
        if matrix[x][y] == 1.0:
            print("achou 1")
            #achei interseccao. ela é mais proxima do que eu ja achei? 
            #calcular aqui a distancia de manhatan pro centro
            dist =  abs(x-meio)+abs(y-meio)
            if dist < menorDist:
                menorDist = dist
        matrix[x][y]= matrix[x][y] +1.0
        x = x+1
    return x-1,y 

def esquerda(x,y,passo):
    
    # percore em -x
    x = x-1
    final = x-passo
    while(x<=final):
        print(matrix[x][y])
        if matrix[x][y] == 1.0:
            print("achou 1")
            #achei interseccao. ela é mais proxima do que eu ja achei? 
            #calcular aqui a distancia de manhatan pro centro
            dist =  abs(x-meio)+abs(y-meio)
            if dist < menorDist:
                menorDist = dist
        matrix[x][y]= matrix[x][y] +1.0 
        x = x-1
    return x+1,y

def cima(x,y,passo):

    #percorre em +y
    y = y+1
    final = y+passo
    while(y<=final):
        print(matrix[x][y])
        if matrix[x][y] == 1.0:
            print("achou 1")
            #achei interseccao. ela é mais proxima do que eu ja achei? 
            #calcular aqui a distancia de manhatan pro centro
            dist =  abs(x-meio)+abs(y-meio)
            if dist < menorDist:
                menorDist = dist
        matrix[x][y]= matrix[x][y] +1.0 
        y = y+1
    return x,y-1

def baixo(x,y,passo): 
    
    #percorre em -y
    y = y-1
    final = y-passo
    while(y<=final):
        print(matrix[x][y])
        if matrix[x][y] == 1.0:
            print("achou 1")
            #achei interseccao. ela é mais proxima do que eu ja achei? 
            #calcular aqui a distancia de manhatan pro centro
            dist =  abs(x-meio)+abs(y-meio)
            if dist < menorDist:
                menorDist = dist
        matrix[x][y]= matrix[x][y] +1.0 
        y = y-1
    return x,y+1

direcoes = {"R":direita,"L":esquerda,"U":cima,"D":baixo}

# fail 
def attempt1():
    for linha in linhas:
        linha = linha.split(",")
        x = meio
        y = meio
        for pos in linha:
            direcao = pos[:1] # R,L,U,D
            passos = int(pos[1:])
            # percorre até achar interseccao
            x, y= direcoes[direcao](x,y,passos)
        print("====")

    with open('outfile.txt','wb') as f:
        for line in matrix:
            np.savetxt(f, line, fmt='%.2f')
        

linha1 = []
# {x1,y1,x2,y2}
        

def attempt2():
    #para cada linha, crie um conjunto de "linhas"
    # linhas tem x1,y1,x2,y2


    # duas linhas se cruzam se 

