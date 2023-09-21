import networkx as nx #Biblioteca necessária para criação dos grafos
import funcoes
import matplotlib.pyplot as plt

def calcular_grau_do_vertice(graph, vertice):
    if graph.has_node(vertice):
        grau = graph.degree(vertice)
        return grau
    else:
        print(f"O vértice {vertice} não existe no grafo.")
        return None

# Exemplo de uso:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
vertice_alvo = 2

grau_do_vertice = calcular_grau_do_vertice(G, vertice_alvo)
if grau_do_vertice is not None:
    print(f"Grau do vértice {vertice_alvo}: {grau_do_vertice}")
    
vizinhos = funcoes.vizinhosDoVertice(G,vertice_alvo)
print(vizinhos)  

nx.draw(G, with_labels=True)
plt.show()  