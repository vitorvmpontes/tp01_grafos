import funcoes

grafo = funcoes.inicializaGrafo("grafosTeste/grafo1.graphml")

#Teste para função ordem()
ordem = funcoes.ordem(grafo)
print("Ordem: " + str(ordem))

#Teste para a função tamanho()
tamanho = funcoes.tamanho(grafo)
print("Tamanho: " + str(tamanho))

#Teste para função vizinhosDoVertice()
verticeAlvo = 0
vizinhos = funcoes.vizinhosDoVertice(grafo,verticeAlvo)
print(vizinhos)

#Teste para a função CalcularGrau()
grau = funcoes.CalcularGrau(grafo,verticeAlvo)
print("O grau do vértice " + str(verticeAlvo)+ " é: " + str(grau))

#Teste para a função de desenhar o grafo
funcoes.desenharGrafo(grafo)