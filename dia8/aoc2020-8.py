import helps as h # importa e chama de h
li = h.get_input("input.txt")

def processa_linha(linhas):
    res = []
    for linha in linhas:
        linha = linha.split(" ")
        opcode = linha[0]
        val = linha[1]
        res.append([opcode,val])
    return res


def part1(linhas):
    i= 0
    acc = 0
    lines_run=set()
    while(i<len(linhas)):
        if (not (i in lines_run)):
            lines_run.add(i)
            opcode = linhas[i][0]
            val = linhas[i][1]
            if opcode =="acc":
                acc = acc+ int(val)
                i +=1
            elif opcode == "jmp":
                i = i + int(val)

            elif opcode =="nop":
                i +=1
        else:
            return acc
    return acc


def part2(linhas):
    i= 0
    acc = 0
    lines_run = set()
    while(i<len(linhas)):
        if (not (i in lines_run)):
            
            lines_run.add(i)
            opcode = linhas[i][:3]
            val = linhas[i][4:]
            if opcode =="acc":
                
                acc = acc + int(val)
                i +=1
            elif opcode == "jmp":
                
                i = i + int(val)
            elif opcode =="nop":
                i +=1
        else:
            return "loop"
    return acc

### main 
print("parte 1: ",part1(processa_linha(li)))

# pra cada linha, se for jmp faça uma copia e troque o jmp por nop e teste
for i in range(0,len(li)):
    opcode = li[i][:3]
    val = li[i][4:]
    if(opcode == "jmp"):
        #cria copia e testa 
        copia = li[:]
        #troca jmp por nop
        copia[i] = copia[i].replace("jmp","nop")
        #roda
        res = part2(copia)
        if res !="loop":
            print("part2 ",res)
            exit()


    elif(opcode == "nop"):
        #cria copia e testa 
        copia = li[:]
        #troca jmp por nop
        copia[i] = copia[i].replace("nop","jmp")
        #roda
       
        res = part2(copia)
        if res !="loop":
            print("part2 ",res)
            exit()
       



