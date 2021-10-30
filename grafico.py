#!sudo pulptest
import matplotlib.pyplot as plt
import networkx as nx


# Dicionário com os Membro da rede e suas conexões
rede = {
    "A": ["B","F"],
    "B": ["A","C","F"],
    "C": ["B","D","E","F"],
    "D": ["D","E"],
    "E": ["C","D","F"],
    "F": ["A","B","C","E"],
}

lista_nos = []
lista_nos_label = {}

k_list = list(rede.keys())
num_nos = len(rede.keys())

for numero in range(num_nos):
  lista_nos.append(numero)
  lista_nos_label[numero]= str(k_list[numero])

G = nx.cubical_graph()
pos = nx.spring_layout(G, seed=3432423433)  # positions for all nodes
#pos = {0: (0,0), 1:(5,3) , 2: (10,3), 3: (15, 0), 4: (10, -3), 5: (5, -3)}

# nodes
options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
nx.draw_networkx_nodes(G, pos, lista_nos, node_color="tab:red", **options)

# edges
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(0, 1),(0, 5),(1, 2),(1, 5),(2, 3),(2, 4),(2, 5),(3, 4),(4, 5)],
    width=3,
    alpha=0.5,
    edge_color="tab:green",
)

nx.draw_networkx_labels(G, pos, lista_nos_label, font_size=22, font_color="whitesmoke")

#plt.tight_layout()
#plt.axis("off")
plt.show()
