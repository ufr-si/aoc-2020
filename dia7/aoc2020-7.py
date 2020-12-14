import helps as h # importa e chama de h
li = h.get_input("small.txt")

def organiza_input(linha):
    linha = linha.split("contain")
    #['dull white bags ', ' no other bags.']
    #['drab fuchsia bags ',
    # ' 5 dark violet bags, 1 shiny gold bag, 3 pale cyan bags.']
    cor_mala = linha[0].replace("bags","").strip()
    lista_conteudo = linha[1][1:].split(", ")
    i = 0
    for i in range(0,len(lista_conteudo)):
        lista_conteudo[i] = lista_conteudo[i].replace("bags.","").replace("bags","").replace("bag.","").replace("bag","")
    
    return cor_mala,lista_conteudo

        
def linha_dict(linhas):
    li_dict = {}
    for linha in linhas:
        cor_mala,lista_conteudo = organiza_input(linha)
        # print("cor mala",cor_mala)
        # print("lista",lista_conteudo)
        li_dict[cor_mala] = {}
        for item in lista_conteudo:
            # pega cor, pega qtde
            
            if ( "no other " != item):
                chave = item[1:].strip()
                valor = item[:1].strip()
                # print("chave: ",chave)
                # print("valor: ",valor)
                li_dict[cor_mala][chave] = int(valor)
    return li_dict
        
def verificar_uma_cor(cor,linhas):
    
    #l_aux = linhas.copy()
    #pegar sempre a lista atualizada)
    j= 0
    cores = []
    #print("procurando por: ",cor)
    while(j<len(linhas)):
        cor_mala, lista_conteudo = organiza_input(linhas[j])
        # print("cor_mala ",cor_mala)
        # print("lista_conteudo: ", lista_conteudo)
        #pra cada cor do lado direito...
        
        for i in range(0,len(lista_conteudo)):
            lista_conteudo[i] = lista_conteudo[i].replace(" bags.","")
            lista_conteudo[i] = lista_conteudo[i].replace(" bag.","")
            lista_conteudo[i] = lista_conteudo[i].replace(" bags","")
            lista_conteudo[i] = lista_conteudo[i].replace(" bag","")
            # print(lista_conteudo[i])
            # print(item)
            # se não achar nenhum com cor, não chama mais verificar_uma_cor
            if(lista_conteudo[i][2:] == cor):
                    # print("achei!")        
                    # achei uma cor do lado direito, agora vou 
                    # adicionar a cor do lado esquerdo e pesquisar quem tem
                    # print("adicionando",cor_mala)
                    cores.append(cor_mala) # adicionei cor do lado esquerdo
                    # print("verificando próximos")
                    novas = verificar_uma_cor(cor_mala,linhas)
                    cores = cores + novas # verifique se acho mais
                    # aqui só vou achar cores do lado direito...
                    # print(len(l_aux))
                    # print("indice j",j)
                    # e se eu retornar as cores ao invés do contador, e DEPOIS contar só os não repetidos ;) 
            i+=1       
        # depois de achar e pegar todas as cores, vai pesquisar nas outras cores
        j+=1
    if len(cor)==0: 
        print("nao achei mais, voltando")
    return cores

# SAIDA: uma lista de cores de mala que contém shiny gold
print("Começando...")
# resultado = verificar_uma_cor("shiny gold",li)
#agora só remover repetidos
new_list = []
# print("result :",resultado)
# for r in resultado:
#     #só adiciona se não tiver
    
#     if( not(r in new_list)):
        
#         new_list.append(r)

# print("resultado: ",len(new_list)) 

# agora ao inves de olha pra tras, olha pra frente a partir de shiny gold
def verificar_pra_frente(cor,linhas):
    print("procurando ",cor)
    
    cont = 0
    for l in linhas:
        
        # pra cada linha verifique se é a cor esperada e compute
        if l ==  cor:
            linha = linhas[l]
            for l2 in linha:
                print("cor = ",l2)
                print("somando",linha[l2])
                #conte o que já veio + 0 valor de l2 multiplicado pelo que encontrar pela frente
                cont = cont + (linha[l2] + (linha[l2]*verificar_pra_frente(l2,linhas)))
                #l2 é a cor com qtde
    return cont

res = linha_dict(li)
count = verificar_pra_frente("shiny gold",res)
print(count)

# verificar_pra_frente("shiny gold",linhas) #tem que retornar valor
