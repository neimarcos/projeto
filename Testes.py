# Dicionário com os Membro da rede e suas conexões
rede = {
    "A": ["B","F"],
    "B": ["A","C","F"],
    "C": ["B","D","E","F"],
    "D": ["D","E"],
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

for nos, links in rede.items():
    print(nos, '->', links.count("A"))
print("Número de Nós da rede:" +  str(len(rede.keys())))

