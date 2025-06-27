
from customtkinter import CTk, CTkButton, CTkCheckBox, CTkEntry, CTkFrame, CTkImage, CTkLabel
from AssuranceAuto.interfaces.base import CustomFrame
from pathlib import Path
from PIL import Image


class ConnectionFrame(CustomFrame):
    def __init__(self, master: CTk | CTkFrame):
        super(ConnectionFrame, self).__init__(master=master)
        self.name = "ConnectionFrame"
        self.master_ = master

        self.config_frame()

        self.place(relwidth=1, relheight=1, relx=0, rely=0)

    def config_frame(self):
        self.configure(fg_color="#dde0ec")
        pass

    def create_widgets(self):
        self.container = CTkFrame(self)

        # Les différents widgtes
        self.label_image_login = CTkLabel(master=self.container)
        self.label_intro = CTkLabel(master=self.container)

        self.label_identifiant = CTkLabel(master=self.container)
        self.label_password = CTkLabel(master=self.container)

        self.entry_identifiant = CTkEntry(master=self.container)
        self.entry_password = CTkEntry(master=self.container)

        self.remember_me_check = CTkCheckBox(master=self.container)
        self.connection_button = CTkButton(master=self.container)
        self.create_account_button = CTkButton(master=self.container)
        pass

    def place_widgets(self):
        self.container.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)

        self.label_image_login.place(relx=0.07, rely=0.15)
        self.label_intro.place(relx=0.55, rely=0.12)

        self.label_identifiant.place(relx=0.56, rely=0.24, relwidth=0.3)
        self.entry_identifiant.place(relx=0.55, rely=0.3, relwidth=0.3)

        self.label_password.place(relx=0.56, rely=0.39, relwidth=0.3)
        self.entry_password.place(relx=0.55, rely=0.45, relwidth=0.3)

        self.remember_me_check.place(relx=0.56, rely=0.52, relwidth=0.3)
        self.connection_button.place(relx=0.75, rely=0.57, relwidth=0.09)
        self.create_account_button.place(relx=0.56, rely=0.57, relwidth=0.17)
        pass

    def config_widgets(self):
        self.container.configure(fg_color="#f6f8fa", corner_radius=7)

        image_login = CTkImage(Image.open(Path("interfaces/assets_/ConnectionPagina.png")), size=(350, 350))
        self.label_image_login.configure(image=image_login, text="")
        self.label_intro.configure(text="Connection au compte d'utilisateur", font=("Segoe UI", 20),
                                   text_color="#1759b5")

        self.entry_identifiant.configure(font=("Segoe UI", 15), border_width=2)
        self.label_identifiant.configure(text="Identifiant :", anchor="w", font=("Segoe UI", 14), text_color="#838C9A")

        self.label_password.configure(text="Mot de passe :", anchor="w", font=("Segoe UI", 14), text_color="#838C9A")
        self.entry_password.configure(font=("Segoe UI", 15), border_width=2)

        self.remember_me_check.configure(text="Se souvenir de moi ?", text_color="#838C9A")
        self.connection_button.configure(text="Ok", font=("Segoe UI", 15), fg_color="#1759b5", cursor="hand2")
        self.create_account_button.configure(text="Créer un compte ?", font=("Segoe UI", 12, "underline"),
                                             fg_color="transparent", border_width=0, text_color="black",
                                             hover_color="#e1e4e8", cursor="hand2",
                                             command=self.create_account)
        pass

    def create_account(self):
        from AssuranceAuto.interfaces.createaccount import CreateAccountFrame
        self.container.destroy()

        CreateAccountFrame(self.master_).tkraise()
    pass

