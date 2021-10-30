# Dicionário com os Membro da rede e suas conexões
rede = {
    "A": ["B","F"],
    "B": ["A","C","F"],
    "C": ["B","D","E","F"],
    "D": ["C","E"],
    "E": ["C","D","F"],
    "F": ["A","B","C","E"],
}

#Imprime os nós
#for nos in rede:
#    print(nos)

#Imprime os nós e as ligações
#for nos in rede:
#    for link in rede[nos]:
#        print("no:" + nos + "link:"+ link)
#
#for nos, links in rede.items():
#    print(nos, '->', links.count("A"))
#print("Número de Nós da rede:" +  str(len(rede.keys())))

#print(rede.keys())


#lista_nos = []
#num_nos = len(rede.keys())
#for numero in range(num_nos):{
#    lista_nos.append(numero)
#}
#print (lista_nos)

#print(rede.keys())

#k_list = list(rede.keys())
#print(k_list)


keys = list(rede)
print(keys[2])
print(rede[keys[2]])
print(rede[keys[2]].count(keys[4]))

#[(0, 1),(0, 5),(1, 2),(1, 5),(2, 3),(2, 4),(2, 5),(3, 4),(4, 5)]
posicao=0
for nos, links in rede.items():
    print (posicao) 
    for i in links:
        print(i) 
    print(nos + i )
    posicao+=1


