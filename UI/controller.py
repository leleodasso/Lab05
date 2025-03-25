import flet as ft

from database.corso_DAO import CorsoDao
from database.studente_DAO import StudenteDao
# Creazione di un'istanza della classe CorsoDao
daoC = CorsoDao()
daoS = StudenteDao()



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_cercaIscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        nomeCorso = self._view.dd_studenti.value
        if nomeCorso is None or nomeCorso == "":
            self._view.create_alert("Selezionare un corso!")
            return
        self._view.txt_result.controls.append(ft.Text(f"hai selezionato il corso di, {nomeCorso}!"))
        self._view.update_page()

    def handle_NomeCognome(self,e):
        # Creiamo un'istanza
        listaStudenti = daoS.getAllStudenti()

        matricola_target = int(self._view.txt_matricola.value)
        Nomestudente=""
        Cognomestudente=""
        for s in listaStudenti:
              if s['matricola'] == matricola_target:
                  Nomestudente = s['nome']
                  Cognomestudente = s['cognome']
                  break
        if Nomestudente is None or Nomestudente == "":
            self._view.create_alert("Matricola non presente!")
            return
        self._view.txt_nome.value = Nomestudente
        self._view.txt_cognome.value = Cognomestudente
        self._view.update_page()



    def handle_cercaCorsi(self, e):
        pass

    def handle_Iscrivi(self, e):
        pass

