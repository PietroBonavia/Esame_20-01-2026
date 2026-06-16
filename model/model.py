import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self._artists_list = []
        self._nodi = []
        self.load_all_artists()

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, n_album):
        self._nodi = DAO.get_nodi(n_album)

    def build_graph(self):

        self.map = {}
        for artist in self._artists_list:
            self.map[artist.id] = artist

        for nodo in self._nodi:
            artista = self.map[nodo[0]]
            self.graph.add_node(artista)

        archi = DAO.get_archi()
        for arco in archi:
            nodo1 = self.map[arco[0]]
            nodo2 = self.map[arco[1]]
            if nodo1 in self.graph and nodo2 in self.graph:
                 self.graph.add_edge(nodo1, nodo2, weight = arco[2])





