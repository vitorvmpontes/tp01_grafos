import funcoes

grafo = funcoes.criarGrafo("grafosTeste/grafo3.graphml")

#Teste para função ordem()
ordem = funcoes.ordem(grafo)
print("Ordem: " + str(ordem))

#Teste para a função tamanho()
tamanho = funcoes.tamanho(grafo)
print("Tamanho: " + str(tamanho))

#Teste para função vizinhosDoVertice()
verticeAlvo = "2"
vizinhos = funcoes.vizinhosDoVertice(grafo,verticeAlvo)
print(vizinhos)

#Teste para a função CalcularGrau()
grau = funcoes.CalcularGrau(grafo,verticeAlvo)
print("O grau do vértice " + str(verticeAlvo)+ " é: " + str(grau))

#Teste para a função ImprimeVertice()
print("Vértices:")
vertices = funcoes.ImprimeVertice(grafo)

#Teste para a função SequenciaGraus()
graus = funcoes.SequenciaGraus(grafo)
print("Sequencia de graus:")
print(graus)

#Teste para a função excentricidade()
excentricidade = funcoes.excentricidade(grafo,verticeAlvo)
print(f"Excentricidade do vertice {verticeAlvo}: {excentricidade}")

#Teste para a função raio()
raio = funcoes.raio(grafo)
print(f"Raio: {raio}")

#Teste para a função diametro()
diametro = funcoes.diametro(grafo)
print(f"Diâmetro: {diametro}")

#Teste para a função centro()
centro = funcoes.centro(grafo)
print(f"Centro: {centro}")

#Teste para a função de desenhar o grafo
#funcoes.desenharGrafo(grafo)
