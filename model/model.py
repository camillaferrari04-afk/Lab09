import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getallairports()
        self._idMap={}
        for node in self._nodes:
            self._idMap[node.ID]=node

    def fillgraph(self, distmedia:float):
        self._graph.clear()
        self._graph.add_nodes_from(self._nodes)
        self.addedges(distmedia)

    def addedges(self, distmedia:float):
        #edges è una lista di dizionari air1(id), air2(id), distmedia(float)
        edges = DAO.getedges(distmedia)

        for edge in edges:
            self._graph.add_edge(self._idMap[edge["air1"]], self._idMap[edge["air2"]], weight=edge["weight"])

    def getnumnodi(self):
        return self._graph.number_of_nodes()
    def getnumarchi(self):
        return self._graph.number_of_edges()
    def getarchi(self):
        return self._graph.edges(data=True)