import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model



    def handle_create_graph(self, e):
        valore_inserito = self._view.txtNumAlbumMin.value

        try:
            # Tenta di convertire in intero
            valore = int(valore_inserito)

            # Se è un numero, controlla che sia maggiore di zero
            if valore <= 0:
                self._view.show_alert("Inserire un numero intero > 0")
                return

        except (ValueError, TypeError):
            # Se la conversione fallisce (es. lettere, simboli o vuoto)
            self._view.show_alert("Inserire un numero intero valido")
            return

        self._model.load_artists_with_min_albums(self._view.txtNumAlbumMin.value)
        self._model.build_graph()

        self._view.txt_result.controls.append(ft.Text(f'Numero di nodi: {self._model.graph.number_of_nodes()}, '
                                                        f'Numero di archi {self._model.graph.number_of_edges()}'))


        self._view.ddArtist.options.clear()
        for artista in self._model.graph.nodes:
            self._view.ddArtist.options.append(ft.dropdown.Option(text = artista.name, key=str(artista.id)))

        self._view.update_page()

    def handle_connected_artists(self, e):

        nodo = int(self._view.ddArtist.value)
        self._view.txt_result.controls.append(ft.Text(f'Artisti direttamente collegati all artista {nodo}:'))

        result = []

        for u, v, w in self._model.graph.edges(data=True):
            if u.id == nodo:
                result.append([v.name, w['weight']])
            elif v.id == nodo:
                result.append([u.name, w['weight']])

        result.sort(key=lambda x: x[1], reverse=True)

        for conesso in result:
            self._view.txt_result.controls.append(ft.Text(f'{conesso[0]} - Numero di generi in comune {conesso[1]}'))

        self._view.update_page()


