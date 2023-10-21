#Makefile para instalar os pacotes matplotlib e NetworkX e lxml
# Para instalar ambos os pacotes, navegue até o diretório do projeto e digite:
# make install-dependencies


install-dependencies:
	pip install matplotlib
	pip install networkx
	pip install lxml


.PHONY: install-dependencies
