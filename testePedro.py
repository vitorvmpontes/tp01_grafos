import funcoes
from tabulate import tabulate

# Carregar o grafo a partir do arquivo "grafosTeste/grafo3.graphml"
grafo = funcoes.criarGrafo("grafosTeste/grafoPedro.graphml")

# Teste para a função ordem()
ordem = funcoes.ordem(grafo)

# Teste para a função tamanho()
tamanho = funcoes.tamanho(grafo)

# Teste para a função vizinhosDoVertice()
# Usando o vertice 6 como exemplo
verticeAlvo = "6"
vizinhos = funcoes.vizinhosDoVertice(grafo, verticeAlvo)

# Teste para a função CalcularGrau()
grau = funcoes.CalcularGrau(grafo, verticeAlvo)

# Teste para a função SequenciaGraus()
graus = funcoes.SequenciaGraus(grafo)

# Teste para a função excentricidade()
excentricidade = funcoes.excentricidade(grafo, verticeAlvo)

# Teste para a função raio()
raio = funcoes.raio(grafo)

# Teste para a função diametro()
diametro = funcoes.diametro(grafo)

# Teste para a função centro()
centro = funcoes.centro(grafo)

# Teste para a função de busca em largura
# Usando o vertice 7 como exemplo
vertice_inicial = "7"
visitados1 = funcoes.buscaLargura(grafo, vertice_inicial)

# Usando o vertice 3 como exemplo
vertice_alvo = "3"
naoVisitados = funcoes.arestasFora(grafo, vertice_alvo)

# Formate as tuplas em `naoVisitados` como strings
naoVisitados = [f"{aresta[0]} -> {aresta[1]}" for aresta in naoVisitados]

# Crie uma lista de listas para tabular os dados
table_data = [
    ["Ordem", ordem],
    ["Tamanho", tamanho],
    ["Vizinhos do Vértice " + verticeAlvo, ", ".join(vizinhos)],
    ["Grau do Vértice " + verticeAlvo, grau],
    ["Sequência de Graus", ", ".join(map(str, graus))],
    ["Excentricidade do Vértice " + verticeAlvo, excentricidade],
    ["Raio", raio],
    ["Diâmetro", diametro],
    ["Centro", centro],
    ["Vértices visitados a partir do Vértice " + vertice_inicial, ", ".join(visitados1)],
    ["Arestas não visitadas a partir do Vértice " + vertice_alvo, ", ".join(naoVisitados)],
]

# Imprima a tabela
print(tabulate(table_data, headers=["Informação", "Valor"], tablefmt="grid"))
