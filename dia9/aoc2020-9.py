
import helps as h # importa e chama de h
li = h.get_input("input.txt")

def processa_linha(linhas):
    res = []
    for li in linhas:
        res.append(int(li))
    return res

li = processa_linha(li)

#lazy way 
#começando em preambulo +1 e indo até o fim, verificar se dois números pra trás somam aquele valor, se sim, vai pro próximo, senao para.
def part1(pre):
    preambulo = pre
    i  = preambulo
    while(i<len(li)):
        num = li[i]
        #procurar dois números anteriores que somem o valor atual
        #fazer um for pros 25 números anteriores
        # duple for
        # print("num a pesquisar ",num)
        achou = False
        for j in range(i-1,i-preambulo,-1):
            # print("vendo : ",j)
            for k in range(j-1,i-preambulo-1,-1):
                # print("com : ",k)
                if (li[j]+li[k] == num):
                    achou = True
        if not achou:
            return num
        i=i+1

preambulo = 25
res = part1(preambulo)
print("part 1",res)

def soma(j,i,num):
    # a partir de 0, multiplica 2 números seguintes
    res = 0
    lista = []
    for k in range(i,len(li)): 
        #a partir de 0, tenta multiplicar os x seguintes
        # multiplica os x números seguintes

        if res == num:
            return lista
    return []

def part2(n):
        #procurar pos números que somados juntos dão esse valor
        i = 0
        # a partir do começo i =0
        atual = li[0]
        # isso é pra ver se eu cheguei no numero pq aí é impossível chegar
        while(atual != n and i<len(li)):
            
            #  j de 2 até (len(li) -i)
            # soma de 2 em 2, 3 em 3 até por exemplo 

            for m in range(2,len(li)-2):
                # multiplica de m em m (2 em 2, 3 em 3...)
                k = 0+m
                while (k<=len(li)):
                    vet = li[k-m:k]
                    if (sum(vet)== n):
                        print("achou")
                        res = min(vet)+max(vet)
                        print(vet)
                        print("part 2 ",res)
                        exit()
                    k = k+1

            
            i = i+1
            atual = li[i]
print("part 2: ",part2(res))
