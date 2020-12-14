import helps as h # importa e chama de h
lines = h.get_input_diferente("input.txt")
lines = lines.split("\n\n")

def parte1():
    total = 0
    for l in lines:
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        total = len(alfabeto)
        for i in l:
            if (i in alfabeto):
                alfabeto.remove(i)
        soma = soma + (total-len(alfabeto))

    return soma        

def parte2():
    soma = 0
    for l in lines:
        alf_dict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        total = len(alfabeto)
        l = l.split("\n") #
        total_membros = len(l)
        # print(l)
        for item in l: 
            # abcdefg
            # abdfg
            for s in item:
                alf_dict[s] += 1
        alf_aux = alfabeto.copy()
        
        for a in alf_aux:
            if(alf_dict[a] == total_membros):
                alfabeto.remove(a)
        # print("grupo: ",total-len(alfabeto))
        # print("\n")
        soma = soma + (total-len(alfabeto))
    # esperado 3 + 0 + 1 + 1 + 1
    return soma        

print(parte1())
print(parte2())

