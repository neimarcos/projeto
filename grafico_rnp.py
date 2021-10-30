import networkx as nx
import matplotlib.pyplot as plt


RNP = nx.read_graphml('Rnp.graphml.xml')
Geant = nx.read_graphml('Geant2012.graphml.xml')

Bet_rnp = nx.betweenness_centrality(RNP)
Bet_geant = nx.betweenness_centrality(Geant)

nx.draw(RNP)
nx.draw(Geant)

plt.tight_layout()
plt.axis("off")
plt.show()

