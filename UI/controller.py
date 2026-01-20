import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):

        int(self._view.txtNumAlbumMin.value)
        try:
            if int(self._view.txtNumAlbumMin.value) > 0:
                pass
        except (ValueError, TypeError):
            self._view.show_alert('Inserisci un numero valido ')

        self._model.build_graph(int(self._view.txtNumAlbumMin.value))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi {self._model._graph.number_of_nodes()}, "
                                                      f"Numero di archi {self._model._graph.number_of_edges()}"
                                                      ))

        for nodo in self._model._graph.nodes():
            self._view.ddArtist.options.append(ft.dropdown.Option(str(nodo.name)))


        self._view._page.update()






    def handle_connected_artists(self, e):
        self._model.build_graph(int(self._view.txtNumAlbumMin.value))

        self._view._page.update()


