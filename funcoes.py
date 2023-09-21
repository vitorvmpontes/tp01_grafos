import networkx as nx #Biblioteca necessária para criação dos grafos
import matplotlib.pyplot as plt #Biblioteca necessária para plotar o grafo

def inicializaGrafo(arquivoGrafo):
    grafo = arquivoGrafo
    G = nx.Graph()
    G = nx.read_graphml(grafo)
    return G


#Retornar a ordem do grafo
def ordem(grafo):
    ordem = grafo.number_of_nodes()
    return ordem
    
#Retornar o tamanho do grafo
def tamanho(grafo):
    tamanho = grafo.number_of_edges()
    return tamanho

#Retornar os vizinhos de um vértice fornecido
def vizinhosDoVertice(graph, vertice):
    if graph.has_node(vertice):
        vizinhos = list(graph.neighbors(vertice))
        return vizinhos
    else:
        print(f"O vértice {vertice} não existe no grafo.")
        return []
    

#Determinar o grau de um vértice fornecido
def CalcularGrau(graph, vertice):
    if graph.has_node(vertice):
        grau = graph.degree(vertice)
        return grau
    else:
        print(f"O vértice {vertice} não existe no grafo.")
        return None

#Retornar a sequência de graus do grafo

#Determinar a excentricidade de um vértice

#Determinar o raio do grafo

#Determinar o diâmetro do grafo

#Determinar o centro do grafo

#Determinar a sequência de vértices visitados na busca em largura e informar a(s)
#aresta(s) que não faz(em) parte da árvore de busca em largura. OBS: a árvore de
#largura deve ser gerada também em formato GraphML.
#Determinar distância e caminho mínimo

#Determinar a centralidade de proximidade C de um vértice x, dada por1:

#Desenha o grafo na tela
def desenharGrafo(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black', font_weight='bold')
    plt.show()    