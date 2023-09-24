import networkx as nx #Biblioteca necessária para criação dos grafos
import matplotlib.pyplot as plt #Biblioteca necessária para plotar o grafo
import lxml.etree as ET

def criarGrafo(caminho_arquivo):
    try:
        grafo = nx.read_graphml(caminho_arquivo)
        return grafo
    except Exception as e:
        print("Ocorreu um erro ao criar o grafo:", e)
        return None


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
def SequenciaGraus(grafo):
    graus = sorted([grau for _, grau in grafo.degree()], reverse=True)
    return graus

#Determinar a excentricidade de um vértice
def excentricidade(grafo, vertice):
    try:
        excentricidade = nx.eccentricity(grafo, v=vertice)
        return excentricidade
    except nx.NetworkXError as e:
        print(f"Ocorreu um erro ao calcular a excentricidade do vértice {vertice}: {e}")
        return None

#Determinar o raio do grafo
def raio(grafo):
    try:
        excentricidades = [nx.eccentricity(grafo, v=vertice) for vertice in grafo.nodes()]
        raio = min(excentricidades)
        return raio
    except nx.NetworkXError as e:
        print(f"Ocorreu um erro ao calcular o raio do grafo: {e}")
        return None


#Determinar o diâmetro do grafo
def diametro(grafo):
    try:
        excentricidades = [nx.eccentricity(grafo, v=vertice) for vertice in grafo.nodes()]
        diametro = max(excentricidades)
        return diametro
    except nx.NetworkXError as e:
        print(f"Ocorreu um erro ao calcular o diâmetro do grafo: {e}")
        return None

#Determinar o centro do grafo
def centro(grafo):
    try:
        excentricidades = nx.eccentricity(grafo)
        raio = min(excentricidades.values())
        centro = [vertice for vertice, excentricidade in excentricidades.items() if excentricidade == raio]
        return centro
    except nx.NetworkXError as e:
        print(f"Ocorreu um erro ao calcular o centro do grafo: {e}")
        return None


#Realiza a busca em largura
def buscaLargura(grafo, ponto_partida):
    arvore = nx.Graph()
    fila = [ponto_partida]
    visitados = set()
    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.add(vertice)
            vizinhos = list(grafo.neighbors(vertice))
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    arvore.add_edge(vertice, vizinho)
    SalvarArvoreGraphml(arvore)                
    return visitados

#Retorna as arestas fora da busca
def arestasFora(grafo,ponto_partida):
    arvore = nx.Graph()
    fila = [ponto_partida]
    visitados = set()
    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.add(vertice)
            vizinhos = list(grafo.neighbors(vertice))
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    arvore.add_edge(vertice, vizinho)
    return list(set(grafo.edges()) - set(arvore.edges()))

#Salva a árvore em formato .graphml
def SalvarArvoreGraphml(arvore):
    graphml = ET.Element("graphml")
    graph = ET.SubElement(graphml, "graph", id="G", edgedefault="directed")

    for node in arvore.nodes():
        ET.SubElement(graph, "node", id=str(node))

    for edge in arvore.edges():
        ET.SubElement(graph, "edge", source=str(edge[0]), target=str(edge[1]))

    tree = ET.ElementTree(graphml)
    tree.write("arvoresBusca/resultadoBusca.graphml", pretty_print=True)
    
#Mostrar arvore de busca
def MostrarArvoreBusca():
        
        arvoreBusca = nx.read_graphml("arvoresBusca/resultadoBusca.graphml")
        pos = nx.spring_layout(arvoreBusca)
        nx.draw(arvoreBusca, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black', font_weight='bold')
        print("Carregando imagem...")
        plt.show()    
        

#Determinar distância e caminho mínimo

#Determinar a centralidade de proximidade C de um vértice x, dada por1:

#Desenha o grafo na tela
def desenharGrafo(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black', font_weight='bold')
    print("Carregando imagem...")
    plt.show()    
    
    
def ImprimeVertice(grafo):
    vertices = list(grafo.nodes)
    for vertice in vertices:
        print(vertice)    
        
        
        
def imprimeOpcoesMenu():
    print("1 - Retornar a ordem do grafo")
    print("2 - Retornar o tamanho do grafo")
    print("3 - Retornar os vizinhos de um vértice fornecido")
    print("4 - Determinar o grau de um vértice fornecido")
    print("5 - Retornar a sequência de graus do grafo")
    print("6 - Determinar a excentricidade de um vértice")
    print("7 - Determinar o raio do grafo")
    print("8 - Determinar o diâmetro do grafo")
    print("9 - Determinar o centro do grafo")
    print("10 - Desenhar o grafo")
    print("11 - Realizar busca em largura")
    print("12 - Mostrar árvore da busca em largura")
    print("13 - Sair")
    
def menu():
    arquivoGrafo = "grafosTeste/grafovini.graphml" 
    grafo = criarGrafo(arquivoGrafo)
    opcao = 0
    while(opcao != 13 ):
        imprimeOpcoesMenu()
        opcao = int(input("Digite uma opção:"))
        
        if (opcao == 1):
            ordem1 = ordem(grafo)
            print("----------------------------")
            print("Ordem: " + str(ordem1))
            print("----------------------------")
            
        if (opcao == 2):
            tamanho1 = tamanho(grafo)
            print("----------------------------")
            print("Tamanho: " + str(tamanho1))
            print("----------------------------")
            
        if (opcao == 3):
            verticeAlvo = str(input("Digite o vértice desejado:"))
            vizinhos = vizinhosDoVertice(grafo,verticeAlvo)  
            print("----------------------------")
            print(f"Vizinhos do vértice {verticeAlvo}")
            print(vizinhos)
            print("----------------------------")
              
        if (opcao == 4):
            verticeAlvo = str(input("Digite o vértice desejado:"))
            grau = CalcularGrau(grafo,verticeAlvo)     
            print("----------------------------")
            print("O grau do vértice " + str(verticeAlvo)+ " é: " + str(grau)) 
            print("----------------------------")   
        
        if(opcao == 5):
            sequencia = SequenciaGraus(grafo)
            print("----------------------------")
            print("Sequencia de graus:")
            print(sequencia)
            print("----------------------------")
     
        if(opcao == 6):
            verticeAlvo = str(input("Digite o vértice desejado"))
            excentricidade1 = excentricidade(grafo,verticeAlvo)
            print("----------------------------")
            print(f"Excentricidade do vertice {verticeAlvo}: {excentricidade1}")
            print("----------------------------")
            
        if(opcao == 7):
            raio1 = raio(grafo)
            print("----------------------------")
            print(f"Raio: {raio1}")
            print("----------------------------")
            
        if(opcao == 8):    
            diametro1 = diametro(grafo)
            print("----------------------------")
            print(f"Diâmetro: {diametro1}")
            print("----------------------------")
            
        if(opcao == 9):
            centro1 = centro(grafo)
            print("----------------------------")
            print(f"Centro: {centro1}")   
            print("----------------------------") 
         
        if(opcao == 10):
            print("Carregando imagem...")
            desenharGrafo(grafo)
            
        if(opcao == 11):
            verticeAlvo = str(input("Digite o vértice desejado para iniciar a busca:"))
            visitados1 = buscaLargura(grafo,verticeAlvo)
            naoVisitados = arestasFora(grafo,verticeAlvo)
            print("")
            print("----------Resultado da Busca em Largura----------")
            print("Vértices visitados:" + str(visitados1))
            print("Arestas não visitadas:" + str(naoVisitados))  
            print("-------------------------------------------------")
            print("")
        if(opcao == 12):
            MostrarArvoreBusca()      
        
        if(opcao == 13):
            return 0