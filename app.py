
from AssuranceAuto.interfaces.base import CustomFrame
from customtkinter import (CTk, CTkButton, CTkCheckBox, CTkEntry, CTkFrame,
                           CTkImage, CTkLabel,set_appearance_mode, set_default_color_theme)
from pathlib import Path
from PIL import Image


from interfaces.buttons import CustomMenuButton
from interfaces.settings import app_settings

set_appearance_mode("light")
set_default_color_theme("interfaces/themes/macos.json")


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

        image_login = CTkImage(Image.open(Path("assets/ConnectionPagina.png")), size=(350, 350))
        self.label_image_login.configure(image=image_login, text="")
        self.label_intro.configure(text="Connexion au compte d'utilisateur", font=("Segoe UI", 20),
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
        self.destroy()
        create_account_frame = CreateAccountFrame(self.master_)
        pass
    pass


class CreateAccountFrame(CustomFrame):
    def __init__(self, master: CTk | CTkFrame):
        super(CreateAccountFrame, self).__init__(master=master)
        self.name = "CreateAccountFrame"
        self.master_ = master

        self.config_frame()

        self.place(relwidth=1, relheight=1, relx=0, rely=0)

    def config_frame(self):
        self.configure(fg_color="#dde0ec")
        pass

    def create_widgets(self):
        self.container = CTkFrame(self)

        self.label_create_account = CTkLabel(master=self.container)

        self.label_intro = CTkLabel(master=self.container)

        self.label_nom = CTkLabel(master=self.container)
        self.label_prenom = CTkLabel(master=self.container)

        self.label_password = CTkLabel(master=self.container)
        self.label_confirm_password = CTkLabel(master=self.container)

        self.entry_nom = CTkEntry(master=self.container)
        self.entry_prenom = CTkEntry(master=self.container)
        self.entry_password = CTkEntry(master=self.container)
        self.entry_confirm_password = CTkEntry(master=self.container)

        self.connection_button = CTkButton(master=self.container)
        self.have_an_account_button = CTkButton(master=self.container)

        pass

    def place_widgets(self):
        self.container.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)

        self.label_create_account.place(relx=0.07, rely=0.22)
        self.label_intro.place(relx=0.55, rely=0.12)

        self.label_nom.place(relx=0.56, rely=0.20, relwidth=0.3)
        self.entry_nom.place(relx=0.55, rely=0.26, relwidth=0.3)

        self.label_prenom.place(relx=0.56, rely=0.35, relwidth=0.3)
        self.entry_prenom.place(relx=0.55, rely=0.41, relwidth=0.3)

        self.label_password.place(relx=0.56, rely=0.50, relwidth=0.3)
        self.entry_password.place(relx=0.55, rely=0.56, relwidth=0.3)

        self.label_confirm_password.place(relx=0.56, rely=0.65, relwidth=0.3)
        self.entry_confirm_password.place(relx=0.55, rely=0.71, relwidth=0.3)

        self.connection_button.place(relx=0.75, rely=0.78, relwidth=0.09)
        self.have_an_account_button.place(relx=0.56, rely=0.78, relwidth=0.17)
        pass

    def config_widgets(self):
        self.container.configure(fg_color="#f6f8fa", corner_radius=7)

        image_create_account = CTkImage(Image.open("assets/noprofile.png"), size=(300, 300))
        self.label_create_account.configure(image=image_create_account, text="")
        self.label_intro.configure(text="Création du compte d'utilisateur", font=("Segoe UI", 20), text_color="#1759b5")

        self.label_nom.configure(text="Nom :", anchor="w", font=("Segoe UI", 14), text_color="#838C9A")
        self.entry_nom.configure(font=("Segoe UI", 15), border_width=2)

        self.label_prenom.configure(text="Prénom :", anchor="w", font=("Segoe UI", 14), text_color="#838C9A")
        self.entry_prenom.configure(font=("Segoe UI", 15), border_width=2)

        self.label_password.configure(text="Mot de passe :", anchor="w", font=("Segoe UI", 14), text_color="#838C9A")
        self.entry_password.configure(font=("Segoe UI", 15), border_width=2)

        self.label_confirm_password.configure(text="Confirmez le mot de passe :", anchor="w", font=("Segoe UI", 14),
                                              text_color="#838C9A")
        self.entry_confirm_password.configure(font=("Segoe UI", 15), border_width=2)

        self.connection_button.configure(text="Ok", font=("Segoe UI", 15), fg_color="#1759b5", cursor="hand2")
        self.have_an_account_button.configure(text="J'ai déjà un compte.", font=("Segoe UI", 12, "underline"),
                                              fg_color="transparent", border_width=0, text_color="black",
                                              hover_color="#e1e4e8", cursor="hand2",
                                              command=self.connection_frame)

    def connection_frame(self):
        self.destroy()
        connection_frame = ConnectionFrame(self.master_)
        pass
    pass


class App(CTk):
    def __init__(self):
        super(App, self).__init__()

        self.configure(height=app_settings.height,
                       width=app_settings.width,
                       fg_color="#dde0ec")
        self.center_window(app_settings.width, app_settings.height)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # La frame de menu
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.menu_frame = CTkFrame(self, fg_color="#f6f8fa")
        self.menu_frame.place(relx=0, rely=0, relwidth=0.16, relheight=1)

        self.but_victime_blessee = CustomMenuButton(master=self.menu_frame)
        self.but_victime_decedee = CustomMenuButton(master=self.menu_frame)
        self.but_gestion_groupe = CustomMenuButton(master=self.menu_frame)
        self.but_valeur_point_ip = CustomMenuButton(master=self.menu_frame)
        self.but_table_conversion_viagere = CustomMenuButton(master=self.menu_frame)
        self.but_table_conversion_temporaire = CustomMenuButton(master=self.menu_frame)
        self.but_logique_calcul = CustomMenuButton(master=self.menu_frame)
        self.but_historique = CustomMenuButton(master=self.menu_frame)
        self.but_parametre = CustomMenuButton(master=self.menu_frame)

        self._but_list: list[CustomMenuButton] = [self.but_victime_blessee,
                                                  self.but_victime_decedee,
                                                  self.but_gestion_groupe,
                                                  self.but_valeur_point_ip,
                                                  self.but_table_conversion_temporaire,
                                                  self.but_table_conversion_viagere,
                                                  self.but_historique,
                                                  self.but_logique_calcul,
                                                  self.but_parametre]
        images = ["assets/028-medical.png",
                  "assets/021-user-1.png",
                  "assets/053-group.png",
                  "assets/031-pulse.png",
                  "assets/064-browsers.png",
                  "assets/064-browsers.png",
                  "assets/073-calculator.png",
                  "assets/038-time.png",
                  "assets/044-settings.png"]
        labels = ["  Victime blessée                    ",
                  "  Victime décédée                   ",
                  "  Victimes groupées             ",
                  " Valeur du point d'IP           ",
                  "Table de rente temporaires",
                  "Table de rente viagères      ",
                  " Historique                         ",
                  " Méthodes de calcul               ",
                  "  Paramètres                           "]

        for i in range(len(self._but_list)):
            text_, image_ = labels[i], CTkImage(Image.open(images[i]), size=(33, 33))
            self._but_list[i].configure(text=text_, image=image_)

        pas = 0
        for but_ in self._but_list[0:-2]:
            but_.place(relx=0.030, rely=0.20 + pas,
                         relwidth=0.96,
                         relheight=0.05)
            pas += 0.08

        self.but_logique_calcul.place(relx=0.030, rely=0.82,
                                      relwidth=0.96,
                                      relheight=0.05)
        self.but_parametre.place(relx=0.030, rely=0.90,
                                 relwidth=0.95,
                                 relheight=0.05)


        self.separation_line = CTkFrame(master=self.menu_frame, height=2, fg_color="#979DA0")
        self.separation_line.place(relx=0.026, rely=0.8, relwidth=0.95)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        self.container_frame = CTkFrame(self, fg_color="#dde0ec")
        self.container_frame.place(relx=0.16, rely=0, relwidth=0.84, relheight=1)

        connection_frame = ConnectionFrame(self.container_frame)
        create_account_frame = CreateAccountFrame(self.container_frame)

        create_account_frame.tkraise()


        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Pour centrer l'application
    def center_window(self, width, height):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    pass


app = App()

if __name__ == '__main__':
    app.mainloop()