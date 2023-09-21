import networkx as nx

# Crie um grafo não direcionado (ou direcionado, se necessário)
G = nx.Graph()

# Adicione nós ao grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Adicione arestas ao grafo
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

vertice = 1

print(G.degree(vertice))