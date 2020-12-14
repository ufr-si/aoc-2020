def getnums(s, e):
    #which is higher? 
    if e>s:
        return list(range(s, e+1))
    else:
        return list(range(e, s+1))

def cross(linha1,linha2):
    # se são linhas paralelas não cruzam.
    # linhas paralelas são as duas horizontais ou duas verticais
    
    #linha1
    x1_1 = linha1["x1"]
    y1_1 = linha1["y1"]
    x2_1 = linha1["x2"]
    y2_1 = linha1["y2"]
    print("x11: ",x1_1,"y11: ",y1_1)
    print("x21: ",x2_1,"y21: ",y2_1)
    
    #linha2 
    x1_2 = linha2["x1"]
    y1_2 = linha2["y1"]
    x2_2 = linha2["x2"]
    y2_2 = linha2["y2"]
    print("x12: ",x1_2,"y12: ",y1_2)
    print("x22: ",x2_2,"y22: ",y2_2)

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
        print("linha 2 vertical")
        direcao2 = "V"
    elif(y1_2 == y2_2):
        # tá na horizontal
        # print("linha 2 H")
        direcao2 = "H"
    if direcao1 != direcao2:
        print(linha1)
        print(linha2)
        #agora é hora
        if(direcao1 =="H" and direcao2 == "V"):
            print("entrou HV")
            # print("range: ",range(y1_2,y2_2+1))
            print("y1_1:",y1_1)
            print("y1_2,y_2_2: ",y1_2,y2_2)
            if (y1_1 in getnums(y1_2,y2_2)):
                
                print("x1_1",x2_1," precisa estar entre ",x1_1," e ",x1_2)

                if(x1_1 in range(x2_1,x2_2)):
                    print("cruza")
                    if (x1_1 != 0 and  y1_1 != 0):
                        print("aonde cruza: ",x1_1,y1_1)
                        return x1_1,y1_1 #ou seja, cruza
                    else:
                        print("0,0")
                
            else:
                print("nao cruza")
        elif(direcao1 =="V" and direcao2 == "H"):
            if (x1_2 in getnums(x1_1,x2_1)):
                print("x1_1",x1_1)
                print("x1_2",x1_2)
                if(y1_1 in range(y1_2,y2_2)):
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

l1 =  {'x1': 3, 'y1': 5, 'x2': 8, 'y2': 5}
l2 =  {'x1': 6, 'y1': 3, 'x2': 6, 'y2': 7}
cross(l1,l2)