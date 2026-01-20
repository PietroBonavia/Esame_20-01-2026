import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.map = {}
        self.archi = []

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        pass

    def build_graph(self, n_album):
        self._artists_list = DAO.get_all_artists()
        for a in self._artists_list:
            self.map[a.id] = a

        nodi = DAO.get_artisti_nodi(n_album)

        for n in nodi:
            nodo = self.map[n[0]]
            self._graph.add_node(nodo)

        self.archi = DAO.get_archi()

        for arco in self.archi:
            arco1 = self.map[arco[0]]
            arco2 = self.map[arco[1]]
            if arco1 in self._graph.nodes() and arco2 in self._graph.nodes():
                  self._graph.add_edge(arco1, arco2, weight = 0)

