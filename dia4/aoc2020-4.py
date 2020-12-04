import re

def get_input(input):

    with open(input,"r") as file:
        linhas = file.read() # le todas as linhas e armazena em um vetor
    return linhas



# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)

def verifica_campos(passaporte):

    check = 0

    for item in passaporte: 
        item = item.split(":")
        # ["byr","1920"]
        chave = item[0]
        valor = item[1]

        if(chave=="byr" and int(valor) >=1920 and int(valor) <=2002):
            # byr (Birth Year) - four digits; 
            # at least 1920 and at most 2002.
            check = check+1
        if(chave=="iyr" and int(valor) >=2010 and int(valor) <=2020):
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.    
            check = check+1
        if(chave=="eyr" and int(valor) >=2020 and int(valor) <=2030):
            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            check = check+1
        if(chave =="hgt" and (valor[-2:] in ["cm","in"])):
            # print(chave,valor)
            # hgt (Height) - a number followed by either cm or in:
            medida = valor[-2:] #cm ou in
            v = int(valor[:-2])
            # print(v,medida)
            if(medida == "cm" and v>=150 and v<=193):
                # If cm, the number must be at least 150 and at most 193.
                check = check+1
            else: 
                if(medida =="in" and v>=59 and v<=76):
                    # If in, the number must be at least 59 and at most 76.        
                    check=check+1
        if(chave=="hcl" and valor[:1] == "#" and len(valor[1:])==6):
            # hcl (Hair Color) - a # followed by exactly
            # six characters 0-9 or a-f.
            print()
            p = re.compile('([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])')
            if(p.match(valor[1:]) != None):
                check= check+1
        cores = ["amb","blu","brn", "gry", "grn", "hzl","oth"]
        if(chave == "ecl" and valor in cores):
            check = check + 1
            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if(chave == "pid" and len(valor)==9):
            # pid (Passport ID) - a nine-digit number, including leading zeroes.
            p = re.compile('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
            if(p.match(valor) != None):
                check=check+1
    
    if(check==7):
        return 1
    return 0

# cid (Country ID)


# print("validos 1:",dados_validos)
lista_passaportes = get_input("input.txt")
lista_passaportes = lista_passaportes.split("\n\n")

passaporte_valido = 0
for passaporte in lista_passaportes:
    passaporte = passaporte.replace("\n"," ")
    passaporte = passaporte.split(" ")
    # print(passaporte)
    #['byr:2001',
    #  'iyr:2011', 
    # 'ecl:brn', 
    # 'pid:487702556', 
    # 'hcl:#602927', 
    # 'hgt:167cm',
    # 'eyr:2026']
    
    dados_verificados =  ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    # print("dados verif ", dados_verificados)
    for item in passaporte:
        item = item.split(":")
        # print("dado: ",item)
        # ['byr',"2001"]
        if(item[0] in dados_verificados):
            #  print("item a remover:", item[0])
            #  print("dados_ver: ",dados_verificados)
             dados_verificados.remove(item[0])
            #  print("dados_ver depois: ",dados_verificados)

    if(len(dados_verificados)==0):
        passaporte_valido = passaporte_valido + verifica_campos(passaporte)

print(passaporte_valido)










