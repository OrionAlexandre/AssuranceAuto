from customtkinter import CTk, CTkFrame, CTkImage, set_appearance_mode, set_default_color_theme
from PIL import Image

from interfaces.base import FrameManager
from interfaces.buttons import CustomMenuButton
from interfaces.settings import app_settings

set_appearance_mode("light")
set_default_color_theme("interfaces/themes/macos.json")


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

        self.frame_manager = FrameManager(master=self.container_frame)
        self.frame_manager.show_frame("CreateAccountFrame")

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