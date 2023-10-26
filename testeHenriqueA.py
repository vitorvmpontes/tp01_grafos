import funcoes

grafo = funcoes.criarGrafo("grafosTeste/grafo3.graphml")

#teste para função de caminho minimo e distancia ()
caminho1 = funcoes.caminhoMinimoDijkstra(grafo, "0", "5")
print(f"caminho: {caminho1}")

distancia1 = funcoes.distanciaMinimaDijkstra(grafo, "0", "5")
print(f"distancia {distancia1}")