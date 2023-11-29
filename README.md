# tp01_grafos

1) INTEGRANTES DO GRUPO:                       

 - Vitor Vasconcelos de Melo Pontes (4255);
 - Henrique Alves (4231);         
 - Henrique Campos (4673);                       
 - Pedro Augusto.                          


2) OBJETIVO:

   O objetivo do trabalho é utilizar o pacote NetworkX (https://networkx.org/ ) para
 desenvolver um programa que implementa um conjunto de algoritmos para grafos não
 direcionados ponderados. As ponderações são valores reais que devem estar associados
 às arestas do grafo.
   Entrada de dados: O grafo de entrada deve ser fornecido no formato GraphML
 (http://graphml.graphdrawing.org/index.html). Pode-se utilizar a ferramenta
 https://graphonline.ru/pt/ para construir um grafo visualmente e exportá-lo para o formato
 GraphML.

   O programa desenvolvido deve ler um grafo e implementar funções para:
     - Retornar a ordem do grafo
     - Retornar o tamanho do grafo
     - Retornar os vizinhos de um vértice fornecido
     - Determinar o grau de um vértice fornecido
     - Retornar a sequência de graus do grafo
     - Determinar a excentricidade de um vértice
     - Determinar o raio do grafo
     - Determinar o diâmetro do grafo
     - Determinar o centro do grafo
     - Determinar a sequência de vértices visitados na busca em largura e informar a(s) aresta(s) que não faz(em) parte da árvore de busca em largura. OBS: a árvore de largura deve ser gerada também em formato GraphML.
     - Determinar distância e caminho mínimo
     - Determinar a centralidade de proximidade C de um vértice x.
     - Verificar se um grafo possui ciclo.
     - Encontrar o menor ciclo (considerar a soma dos pesos de cada aresta do ciclo) em um grafo não dirigido ponderado (somente com pesos positivos).
     -Determinar a árvore geradora mínima de um grafo.
     - A árvore geradora mínima deve ser gerada no formato GraphML e o seu peso total deve ser retornado.
     - Determinar um conjunto estável de vértices de um grafo por meio de uma heurística.
     - Determinar o emparelhamento máximo em um grafo.
