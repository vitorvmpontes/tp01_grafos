import networkx as nx #Biblioteca necessária para criação dos grafos
import matplotlib.pyplot as plt #Biblioteca necessária para plotar o grafo
import lxml.etree as ET
import os

def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')

def criarGrafo(caminho_arquivo):
    try:
        grafo = nx.read_graphml(caminho_arquivo)
        return grafo
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except IOError as e:
        print(f"Erro de E/S ao ler o arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o grafo: {e}")
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
        

def mostrarArvoreGeradoraMinima():

    arvoreGeradora = nx.read_graphml("grafosTeste/arvore_geradora_minima.graphml")
    pos = nx.spring_layout(arvoreGeradora)
    nx.draw(arvoreGeradora, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black',font_weight='bold')
    print("Carregando imagem...")
    plt.show()

#Determinar distância e caminho mínimo
def distanciaMinimaDijkstra(grafo, noOrigem, noDestino):
    if noOrigem not in grafo or noDestino not in grafo:
        return None
    try:
        #Calcula a distância mínima usando o algoritmo de Dijkstra
        distanciaMinima = nx.shortest_path_length(grafo, noOrigem, noDestino)
        return distanciaMinima
    except nx.NetworkXNoPath:
        #Caso não exista um caminho entre os nós de origem e destino
        raise float('inf')
    
def caminhoMinimoDijkstra(grafo, noOrigem, noDestino):
    if noOrigem not in grafo or noDestino not in grafo:
        return None
    try:
        #Calcula o caminho mínimo usando o algoritmo de Dijkstra
        caminhoMinimo = nx.shortest_path(grafo, noOrigem, noDestino)
        return caminhoMinimo
    except nx.NetworkXNoPath:
        #Caso não exista um caminho entre os nós de origem e destino
        return []


#Determinar a centralidade de proximidade C de um vértice x
def DeterminarCentralidade(grafo, vertice_x):
    # Verifica se o vértice_x pertence ao grafo
    if vertice_x not in grafo.nodes():
        print("O vértice fornecido não pertence ao grafo.")
        return ('inf')  # Ou qualquer valor apropriado para indicar um erro

    # Obtém o número de vértices no grafo
    num_vertices = grafo.number_of_nodes()
    
    # Inicializa a soma das distâncias
    soma_distancias = 0
    
    # Calcula a distância entre o vértice_x e todos os outros vértices no grafo
    for outro_vertice in grafo.nodes():
        if outro_vertice != vertice_x:
            try:
                distancia = nx.shortest_path_length(grafo, source=vertice_x, target=outro_vertice)
                soma_distancias += distancia
            except nx.NetworkXNoPath:
                # Caso não exista um caminho entre os vértices, tratamos como uma distância infinita (conforme a fórmula)
                soma_distancias += float('inf')
    
    # Calcula a centralidade de proximidade
    centralidade = (num_vertices - 1) / soma_distancias
    
    return centralidade


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
        
        

# Verificar se o grafo possui ciclo
def possuiCiclo(grafo):
    try:
        ciclos = nx.algorithms.cycles.simple_cycles(grafo)
        # Se houver algum ciclo, a função retorna True
        return any(ciclos)
    except nx.NetworkXNoCycle:
        # Se não houver ciclo, a exceção NetworkXNoCycle será tratada e a função retornará False
        return False
    
# Algoritmo de Kruskal
def kruskal(grafo):
    arestas = [(u, v, grafo[u][v].get('weight', 1)) for u, v in grafo.edges()]
    arestas = sorted(arestas, key=lambda x: x[2])  # Ordena as arestas pelo peso
    conjuntos = {vertice: {vertice} for vertice in grafo.nodes()}
    arvore_geradora = nx.Graph()

    for u, v, peso in arestas:
        if conjuntos[u] != conjuntos[v]:
            arvore_geradora.add_edge(u, v, weight=peso)
            conjunto_uniao = conjuntos[u].union(conjuntos[v])
            for vertice in conjunto_uniao:
                conjuntos[vertice] = conjunto_uniao

    return arvore_geradora

def peso_total_arvore(arvore):
    return sum(arvore[u][v]['weight'] for u, v in arvore.edges())

# Determina a árvore geradora mínima do grafo
def determinar_arvore_geradora_minima(grafo):
    try:
        arvore_geradora = kruskal(grafo)
        peso_total = peso_total_arvore(arvore_geradora)

        # Salvando a árvore geradora mínima no formato GraphML
        SalvarArvoreGraphml(arvore_geradora, "grafosTeste/arvore_geradora_minima.graphml")

        print("-------------------------------------")
        print(f"Árvore geradora mínima salva em 'grafosTeste/arvore_geradora_minima.graphml'")
        mostrarArvoreGeradoraMinima()
        return peso_total
    except Exception as e:
        print(f"Ocorreu um erro ao determinar a árvore geradora mínima: {e}")
        return None

# Salva em um arquivo a árvore geradora mínima
def SalvarArvoreGraphml(arvore, caminho):
    graphml = ET.Element("graphml")
    graph = ET.SubElement(graphml, "graph", id="G", edgedefault="undirected")

    for node in arvore.nodes():
        ET.SubElement(graph, "node", id=str(node))

    for u, v in arvore.edges():
        peso = arvore[u][v].get('weight', 1)
        ET.SubElement(graph, "edge", source=str(u), target=str(v), weight=str(peso))

    tree = ET.ElementTree(graphml)
    tree.write(caminho)
    
# Eurística para determinar um conjunto estável de vértices
def conjunto_estavel_heuristica(grafo):
    conjunto_estavel = set()  # Conjunto que armazenará o conjunto estável
    vizinhos_escolhidos = set()  # Vizinhos dos vértices escolhidos

    # Enquanto houver vértices não escolhidos
    while grafo:
        # Encontrar o vértice com o menor número de vizinhos não escolhidos
        vertice_min_vizinhos = min(grafo, key=lambda v: len(set(grafo.neighbors(v)) - vizinhos_escolhidos))

        # Adicionar o vértice ao conjunto estável
        conjunto_estavel.add(vertice_min_vizinhos)

        # Adicionar os vizinhos do vértice ao conjunto de vizinhos escolhidos
        vizinhos_escolhidos.update(grafo.neighbors(vertice_min_vizinhos))

        # Remover o vértice e seus vizinhos do grafo
        grafo.remove_nodes_from(set(grafo.neighbors(vertice_min_vizinhos)) | {vertice_min_vizinhos})

    return conjunto_estavel

# Define o emparelhamento máximo de um grafo
def emparelhamentoMaximo(grafo):
    try:
        emparelhamento = nx.maximal_matching(grafo)
        return emparelhamento
    except nx.NetworkXError as e:
        print(f"Ocorreu um erro ao calcular o emparelhamento máximo do grafo: {e}")
        return None

def menor_ciclo(G):

  if not nx.is_connected(G):
    return None

  if eh_ponderado(G) != 1:
      return "O grafo não é ponderado!"

  # Inicializa o conjunto de vértices visitados.

  visitados = set()

  # Inicializa o menor ciclo encontrado.

  menor_ciclo = []

  # Percorre o grafo em busca de ciclos.

  for u in G.nodes():
    if u not in visitados:
      ciclo = _percorre_ciclo(G, u, visitados)
      if ciclo is not None and len(ciclo) > 1:
        menor_ciclo = ciclo

  return menor_ciclo


def _percorre_ciclo(G, u, visitados):

  visitados.add(u)

  ciclo = [u]
  v = u

  while True:
    for w in G.neighbors(v):
      if w not in visitados:
        ciclo.append(w)
        v = w
        break
    else:
      # Não há mais vértices adjacentes não visitados.
      if len(ciclo) > 1:
        return ciclo
      else:
        return None

def eh_ponderado(G):

  for u, v, d in G.edges(data=True):
    if d is not None:
      return 1
  return 0
               
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
    print("13 - Determinar distância e caminho mínimo")
    print("14 - Determinar a centralidade de proximidade C de um vértice x")
    print("15 - Verificar se o grafo possui ciclo")
    print("16 - Encontrar o menor ciclo")
    print("17 - Determinar a árvore geradora mínima de um grafo")
    print("18 - Determinar um conjunto estável de vértices de um grafo por meio de uma heurística")
    print("19 - Determinar o emparelhamento máximo em um grafo")
    print("20 - Sair")
    
def menu():
    arquivoGrafo = "grafosTeste/grafo1.graphml"
    grafo = criarGrafo(arquivoGrafo)
    grafo_original = grafo.copy() # Crie uma cópia do grafo original para que o original não seja afetado
    opcao = 0
    while(opcao != 20 ):
        imprimeOpcoesMenu()
        opcao = int(input("Digite uma opção:"))
        limparTela()
        
        if (opcao == 1):
            ordem1 = ordem(grafo)
            print("-------------------------------------")
            print("Ordem: " + str(ordem1))
            print("-------------------------------------")
            
        if (opcao == 2):
            tamanho1 = tamanho(grafo)
            print("-------------------------------------")
            print("Tamanho: " + str(tamanho1))
            print("-------------------------------------")
            
        if (opcao == 3):
            verticeAlvo = str(input("Digite o vértice desejado:"))
            vizinhos = vizinhosDoVertice(grafo,verticeAlvo)  
            print("-------------------------------------")
            print(f"Vizinhos do vértice {verticeAlvo}")
            print(vizinhos)
            print("-------------------------------------")
              
        if (opcao == 4):
            verticeAlvo = str(input("Digite o vértice desejado:"))
            grau = CalcularGrau(grafo,verticeAlvo)     
            print("-------------------------------------")
            print("O grau do vértice " + str(verticeAlvo)+ " é: " + str(grau)) 
            print("-------------------------------------")   
        
        if(opcao == 5):
            sequencia = SequenciaGraus(grafo)
            print("-------------------------------------")
            print("Sequencia de graus:")
            print(sequencia)
            print("-------------------------------------")
     
        if(opcao == 6):
            verticeAlvo = str(input("Digite o vértice desejado"))
            excentricidade1 = excentricidade(grafo,verticeAlvo)
            print("-------------------------------------")
            print(f"Excentricidade do vertice {verticeAlvo}: {excentricidade1}")
            print("-------------------------------------")
            
        if(opcao == 7):
            raio1 = raio(grafo)
            print("-------------------------------------")
            print(f"Raio: {raio1}")
            print("-------------------------------------")
            
        if(opcao == 8):    
            diametro1 = diametro(grafo)
            print("-------------------------------------")
            print(f"Diâmetro: {diametro1}")
            print("-------------------------------------")
            
        if(opcao == 9):
            centro1 = centro(grafo)
            print("-------------------------------------")
            print(f"Centro: {centro1}")   
            print("-------------------------------------") 
         
        if(opcao == 10):
            print("Carregando imagem...")
            desenharGrafo(grafo)
            
        if(opcao == 11):
            verticeAlvo = str(input("Digite o vértice desejado para iniciar a busca:"))
            visitados1 = buscaLargura(grafo,verticeAlvo)
            naoVisitados = arestasFora(grafo,verticeAlvo)
            print("")
            print("----------Resultado da Busca em Largura--------------------------------------")
            print('\n')
            print("Vértices visitados:" + str(visitados1))
            print("Arestas não visitadas:" + str(naoVisitados))  
            print('\n')
            print("-----------------------------------------------------------------------------")
            print("")
        if(opcao == 12):
            MostrarArvoreBusca()

        if(opcao==13):
            VerticePartida = str(input("Digite o vértice de partida:"))
            VerticeFim = str(input("Digite o vértice de chegada:"))
            Distancia1 = distanciaMinimaDijkstra(grafo, VerticePartida, VerticeFim)
            Caminho1 = caminhoMinimoDijkstra(grafo, VerticePartida, VerticeFim)
            if Caminho1:
                print("")
                print("-------------------------------------------------")
                print(f"Caminho: {Caminho1}")
                print(f"Distancia: {Distancia1}")
                print("-------------------------------------------------")
            else:
                print(f"Os vértices {VerticePartida} ou {VerticeFim} não pertecem ao grafo")          
        
        if opcao == 14:
            vertice_x = str(input("Digite o vértice para calcular a centralidade de proximidade: "))
            centralidade_x = DeterminarCentralidade(grafo, vertice_x)
            print(f"\n\nA centralidade de proximidade do vértice {vertice_x} é {centralidade_x}\n\n")
            
        if opcao == 15:
            temCiclo = possuiCiclo(grafo)
            if temCiclo:
                print("-------------------------------------")
                print("O grafo possui ciclo.")
                print("-------------------------------------")
            else:
                print("-------------------------------------")
                print("O grafo não possui ciclo.")
                print("-------------------------------------")
        
        if opcao == 16:
            menorCiclo = menor_ciclo(grafo)
            print("---------------------------------------")
            print(menorCiclo)
            print("---------------------------------------")
        
        if opcao == 17:
            peso_total = determinar_arvore_geradora_minima(grafo)
            if peso_total is not None:
                print(f"Peso total da árvore geradora mínima: {peso_total}")
                print("---------------------------------------")
                            
        if opcao == 18:
            grafo = grafo_original.copy()
            print("---------------------------------------")
            conjunto_resultante = conjunto_estavel_heuristica(grafo)
            print("Conjunto Estável Encontrado:", conjunto_resultante)
            print("---------------------------------------")
            
        if opcao == 19:
            grafo = grafo_original.copy()
            if grafo:
                emparelhamento = emparelhamentoMaximo(grafo)
                if emparelhamento:
                    print("-------------------------------------")
                    print("Emparelhamento máximo:")
                    print(emparelhamento)
                    print("---------------------------------------")
            
        if opcao == 20:
            return 0
        
        if(opcao <= 0 or opcao > 20):
            print("---------------------------------------")
            print("[ERRO] Opção inválida, tente novamente!")
            print("---------------------------------------")
            
