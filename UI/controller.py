import flet as ft
from flet.cli.commands import options

from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        list_cr = self._model.getAllChromosoma()
        for cr in list_cr:
            self._view.dd_min_ch.options.append(ft.dropdown.Option(cr))
            self._view.dd_max_ch.options.append(ft.dropdown.Option(cr))

    def handle_graph(self, e):
        Cmin = self._view.dd_min_ch.value
        min_int = int(Cmin)
        Cmax = self._view.dd_max_ch.value
        max_int = int(Cmax)

        if min_int > max_int:
            print(f"Cmin-{min_int}----Cmaz {max_int}")
            self._view.txt_result1.controls.append(ft.Text(f"Selezione non valida, selezionare altri valori"))
            self._view.update_page()
        else:
            print("ok validazione, pre build")
            self._model.buildGraph(min_int, max_int)
            nodi, archi = self._model.getGraphDetails()
            self._view.txt_result1.controls.append(ft.Text(f"Grafo con {nodi} nodi e {archi} archi"))
            #self._model.get_node_max_uscenti()
            self._view.txt_result1.controls.append(ft.Text(f"Best 5:"))
            self._view.txt_result1.controls.append(ft.Text(f"{self._model.getBest5Nodi()} "))
            self._view.update_page()

    def handle_dettagli(self, e):
        pass

    def handle_path(self, e):
        pass
