#!sudo pulptest
import matplotlib.pyplot as plt
import networkx as nx

G = nx.cubical_graph()
#pos = nx.spring_layout(G, seed=3432423433)  # positions for all nodes
pos = {0: (0,0), 1:(5,3) , 2: (10,3), 3: (15, 0), 4: (10, -3), 5: (5, -3)}

# nodes
options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
nx.draw_networkx_nodes(G, pos, nodelist=[ 0, 1, 2, 3, 4 ,5], node_color="tab:red", **options)



# edges
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(0, 1),(0, 5),(1, 2),(1, 5),(2, 3),(2, 4),(2, 5),(3, 4),(4, 5)],
  
    width=3,
    alpha=0.5,
    edge_color="tab:green",
)


#    G,
##    pos,
 #   edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
 #   width=8,
  #  alpha=0.5,
  #  edge_color="tab:blue",
#)



# some math labels
labels = {}
labels[0] = r"$A$"
labels[1] = r"$B$"
labels[2] = r"$C$"
labels[3] = r"$D$"
labels[4] = r"$E$"
labels[5] = r"$F$"


nx.draw_networkx_labels(G, pos, labels, font_size=22, font_color="whitesmoke")

plt.tight_layout()
plt.axis("off")
plt.show()
