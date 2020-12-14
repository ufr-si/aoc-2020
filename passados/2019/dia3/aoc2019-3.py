import helps as h # importa e chama de h
import numpy as np
linhas = h.get_input("tiny.txt")

#vamos criar uma matriz bem grandez
# Creates a list containing 50000 lists, each of 50000 items, all set to 0
tam = 80000
matrix = np.zeros((tam,tam))
meio = int(tam/2)
x = meio
y = meio
menorDist = 999999


def getnums(s, e):
    #which is higher? 
    if e>s:
        return list(range(s, e+1))
    else:
        return list(range(e, s+1))

linhas1 = []
linhas2 = []
# {x1,y1,x2,y2}
#     #linhas HORIZONTAIS tem Y1 = Y2
def cross(linha1,linha2):
    # se são linhas paralelas não cruzam.
    # linhas paralelas são as duas horizontais ou duas verticais
    
    #linha1
    x1_1 = linha1["x1"]
    y1_1 = linha1["y1"]
    x2_1 = linha1["x2"]
    y2_1 = linha1["y2"]
    
    #linha2 
    x1_2 = linha2["x1"]
    y1_2 = linha2["y1"]
    x2_2 = linha2["x2"]
    y2_2 = linha2["y2"]

    direcao1 = ""
    direcao2 = ""

    # l1 está na vertical ou horizontal? 
    if (x1_1 == x2_1):
        print("linha 1 vertical")
        #tá na vertical
        direcao1 = "V"
    elif(y1_1 == y2_1):
        # tá na horizontal
        print("linha 1 H")
        direcao1 = "H"

    if (x1_2 == x2_2):
        #tá na vertical
        # print("linha 2 vertical")
        direcao2 = "V"
    elif(y1_2 == y2_2):
        # tá na horizontal
        # print("linha 2 H")
        direcao2 = "H"
    if direcao1 != direcao2:
        # print(linha1)
        # print(linha2)
        #agora é hora
        if(direcao1 =="H" and direcao2 == "V"):
            # print("range: ",range(y1_2,y2_2+1))
            print(linha1)
            print(linha2)
            if (y1_1 in getnums(y1_2,y2_2)):
                print("x1_1",x1_1)
                print("x1_2",x1_2)
                if(x1_1 == x1_2):
                    print("cruza")
                    if (x1_1 != 0 and  y1_1 != 0):
                        print("aonde cruza: ",x1_1,y1_1)
                        return x1_1,y1_1 #ou seja, cruza
                    else:
                        print("0,0")
                print("nao cruza")
            else:
                print("nao cruza")
        elif(direcao1 =="V" and direcao2 == "H"):
            if (x1_2 in getnums(x1_1,x2_1)):
                print("x1_1",x1_1)
                print("x1_2",x1_2)
                if(y1_1 == y1_2):
                    print("cruza")
                    if (x1_2 != 0 and  y1_2 != 0):
                        print("aonde cruza: ",x1_2,y1_2)
                        return x1_2,y1_2
                    else:
                        print("0,0")
            else:
                print("nao cruza")
    # else:
    #     print("paralelas")
    # input()
    return -1,-1
            
    #linhas VERTICAIS   tem X1 = X2
    # se forem perpendiculares, podem se cruzar 
    # caso o X da linha VERTICAL esteja dentro da range x1 x2 da linha horizontal
    # e?/ou? caso y linha horizontal esteja dentro da range y1 y2 da linha vertical

def gera_linhas(n):
    l = linhas[n]
    res = []
    l = l.split(",")
    x = 0
    y = 0
    for info in l:
        direcao = info[:1] # R,L,U,D
        passos = int(info[1:])
        if(direcao =="R"):
            #anda +x
            novox = x+passos
            line = {"x1":x,"y1":y,"x2":novox,"y2":y}
            x = novox
        if(direcao == "L"):
            #anda -x
            novox = x-passos
            line = {"x1":novox,"y1":y,"x2":x,"y2":y}
            x = novox
        if(direcao == "U"):
            # +y
            novoy = y+passos
            line = {"x1":x,"y1":y,"x2":x,"y2":novoy}
            y = novoy
        if(direcao == "D"):
            # -y
            novoy = y-passos
            line = {"x1":x,"y1":novoy,"x2":x,"y2":y}
            y = novoy
        res.append(line)
    
    return res

def attempt2():
    #para cada linha, crie um conjunto de "linhas"
    # linhas tem x1,y1,x2,y2
    # pra cada linha
    linhas1 = gera_linhas(0)
    linhas2 = gera_linhas(1)
    # agora que gerei linhas, ver se cruza...
    menorDist = 999999
    x = 99999
    y = 99999
    v =  0
    print(linhas1)
    print(linhas2)
    for l1 in linhas1:
        for l2 in linhas2:
            x,y = cross(l1,l2)
            # calcula manhattan
            if (x != -1 and y != -1):
                print ("deu cross: ",x,y) 
                v = abs(0-x)+abs(0-y) #confirma isso aqui
                if (v < menorDist):
                    print("achou menor, x e y e v:",x,y,v)
                    menorDist = v
    print(menorDist)   

attempt2()
