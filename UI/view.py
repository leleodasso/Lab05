import flet as ft
import database.corso_DAO as cd
corso_dao = cd.CorsoDao()  # Creiamo un'istanza

class View(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_corso = None
        self.btn_cercaIscritti = None
        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cognome = None
        self.btn_cercaStudente = None
        self.btn_cercaCorsi = None
        self.btn_Iscrivi = None
        self.txt_result=None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1 with some controls
        self.dd_corso = ft.Dropdown(label="corso",width=450,hint_text="Selezionare un corso", options=[ft.dropdown.Option(i) for i in corso_dao.getAllNomiCorsi()])
        self.btn_cercaIscritti = ft.ElevatedButton(text="Cerca Iscritti ", on_click=self._controller.handle_cercaIscritti)
        row1 = ft.Row([self.dd_corso, self.btn_cercaIscritti],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        # ROW2 with some controls
        self.txt_matricola = ft.TextField(label="matricola",width=150, on_change=self._controller.handle_NomeCognome)
        self.txt_nome = ft.TextField(label="nome",width=200, read_only = True)
        self.txt_cognome = ft.TextField(label="cognome",width=200, read_only = True)
        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        # ROW3 with some controls
        self.btn_cercaStudente = ft.ElevatedButton(text="Cerca studente ", on_click=self._controller.handle_cercaStudente)
        self.btn_cercaCorsi =  ft.ElevatedButton(text="Cerca corsi ", on_click=self._controller.handle_cercaCorsi)
        self.btn_Iscrivi=  ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_Iscrivi)
        row3 = ft.Row([self.btn_cercaStudente, self.btn_cercaCorsi, self.btn_Iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
