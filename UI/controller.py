import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        distmedia = self._view.txt_mindist.value

        if distmedia=="" or distmedia is None or not distmedia.isdigit():
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire una distanza valida", color="red"))
            self._view.update_page()

        elif float(distmedia) < 0.0:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire una distanza positiva", color="red"))
            self._view.update_page()

        else:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Caricamento..."))
            self._view.update_page()
            self._model.fillgraph(int(distmedia))
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Grafico creato correttamente", color="green", size=18))
            self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getnumnodi()}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getnumarchi()}"))

            for edge in self._model.getarchi():
                self._view.txt_result.controls.append(ft.Text(f"{edge[0]} - {edge[1]} - {edge[2]["weight"]}"))
            self._view.update_page()



