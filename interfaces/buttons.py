
from customtkinter import CTk, CTkButton, CTkFrame



class CustomMenuButton(CTkButton):
    """
    Ceci servira de boutton personnalisé pour les fonctionnalités du menu.
    """
    def __init__(self, master: CTkFrame | CTk):
        self.master: CTkFrame | CTk = master
        super(CustomMenuButton, self).__init__(self.master)

        self.config_button()

    def config_button(self):
        self.configure(corner_radius=4,
                       fg_color="transparent",
                       text_color="black",
                       font=("Segoe UI", 14))