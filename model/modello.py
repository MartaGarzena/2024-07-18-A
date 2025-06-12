from xml.sax.saxutils import prepare_input_source

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}
        self._chromosoma = []
        self._grafo = nx.DiGraph()
        self._allGenes = DAO.get_all_genes()

        self._NodoPesoUscenti = {}
        self._NodoNumUscenti = {}

        for o in self._allGenes:
            self._idMap[(o.GeneID, o.Function)] = o

    def getAllChromosoma(self):
        self._chromosoma = DAO.get_all_Chromosoma()
        return self._chromosoma

    def buildGraph(self, min, max):
        self._grafo.clear()
        print("model, building graph")
        for gene in self._allGenes:
            if max >= gene.Chromosome >= min:
                self._grafo.add_node(gene)

        self.addEdge()

    def getGraphDetails(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def addEdge(self):
        '''tuple = DAO.haveInteraction()
        print("aggiungo archi")
        for tup in tuple:
            u = tup[0] #sono gli id
            v = tup[1]
            peso = DAO.haveLocalizzazione(u, v)
            geneu = self._idMap[u]
            genev = self._idMap[v]

            print(f"coppia {u}-{v}")
            if peso is not None and geneu in self._grafo.nodes and genev in self._grafo.nodes:
                if geneu.Chromosome < genev.Chromosome:
                    self._grafo.add_edge(geneu, genev, weight=peso)
                if geneu.Chromosome == genev.Chromosome:
                    self._grafo.add_edge(geneu, genev, weight=peso)
                    self._grafo.add_edge(genev, geneu, weight=peso)
        print("fine archi")'''
        tuple = DAO.getArchi()
        for tup in tuple:
            u = tup[0]
            fun_u = tup[1]
            v = tup[2]
            fun_v = tup[3]
            peso = tup[4]

            geneu = self._idMap[(u, fun_u)]
            genev = self._idMap[(v, fun_v)]
            if u != v and geneu in self._grafo.nodes and genev in self._grafo.nodes:
                if geneu.Chromosome < genev.Chromosome:
                    self._grafo.add_edge(geneu, genev, weight=peso)
                    self.Add(geneu, peso)
                if geneu.Chromosome == genev.Chromosome:
                    self._grafo.add_edge(geneu, genev, weight=peso)
                    self.Add(geneu, peso)
                    self._grafo.add_edge(genev, geneu, weight=peso)
                    self.Add(genev, peso)
                if geneu.Chromosome > genev.Chromosome:
                    self._grafo.add_edge(genev, geneu, weight=peso)
                    self.Add(genev, peso)

    def Add(self, gene, peso):
        if gene not in list(self._NodoPesoUscenti.keys()):
            self._NodoPesoUscenti[gene] = peso
        else:
            self._NodoPesoUscenti[gene] += peso

        if gene not in list(self._NodoNumUscenti.keys()):
            self._NodoNumUscenti[gene] = 1
        else:
            self._NodoNumUscenti[gene] += 1

    def getBest5Nodi(self):

        # sorting values in descending order
        output = dict(sorted(self._NodoNumUscenti.items(), key=lambda item: item[1], reverse=True))

        i = 0
        daStm=""

        for key in output:
            i = i + 1
            daStm += f" \n {key} | NUM ARCHI: {self._NodoNumUscenti[key]} | PESO TOTALE: {self._NodoPesoUscenti[key]} \n"
            if i > 5: break

        return daStm
