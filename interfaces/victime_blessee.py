from tkinter.constants import DISABLED, END

from customtkinter import CTk, CTkFrame, set_appearance_mode, set_default_color_theme, CTkButton, CTkLabel
from tkinter import StringVar
from tkinter.ttk import Combobox

from AssuranceAuto.interfaces.base import CustomFrame, CustomEntry, CustomCombobox
from AssuranceAuto.interfaces.buttons import CustomMenuBarButton

set_appearance_mode("light")
set_default_color_theme(r"interfaces/themes/macos.json")

class IncapaciteTemporaireFrame(CustomFrame):
    def __init__(self, master: CTk | CTkFrame):
        super(IncapaciteTemporaireFrame, self).__init__(master=master)

        self.name = "IncapaciteTemporaireFrame"
        self.master_ = master

        self.place(relwidth=1, relheight=1, relx=0, rely=0)

    def config_frame(self):
        self.configure(fg_color="#dde0ec") #dde0ec
        pass

    def create_widgets(self):
        self.menu_bar = CTkFrame(self)

        self.incapacite_temporaire_but = CustomMenuBarButton(self.menu_bar)
        self.incapacite_permanente_but = CustomMenuBarButton(self.menu_bar)

        self.smig_cima = {"Bénin": 52000,
                                    "Burkina Faso": 45000,
                                    "Cameroun": 60000,
                                    "Centrafrique": 36000,
                                    "Congo (brazaville)": 90000,
                                    "Côte d'Ivoire": 75000,
                                    "Gabon": 150000,
                                    "Guinée Bissau": 129035,
                                    "Guinée Equatoriale": 128000,
                                    "Mali": 40000,
                                    "Niger": 30047,
                                    "Sénégal": 64223,
                                    "Tchad": 60000,
                                    "Togo": 52500}

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # La frame de l'IT.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Les différentes frames.
        self.incapacite_temporaire_frame = CTkFrame(self)
        self.frame_infos_personne_1 = CTkFrame(self.incapacite_temporaire_frame)
        self.frame_infos_personne_it = CTkFrame(master=self.incapacite_temporaire_frame)
        self.frame_results_it = CTkFrame(master=self.incapacite_temporaire_frame)

        # Les bouttons
        self.compute_it_but = CTkButton(master=self.incapacite_temporaire_frame)
        self.but_save_it = CTkButton(master=self.incapacite_temporaire_frame)
        self.but_clean_it = CTkButton(master=self.incapacite_temporaire_frame)

        self.nom_person_entry = CustomEntry(master=self.frame_infos_personne_1)
        self.prenom_person_entry = CustomEntry(master=self.frame_infos_personne_1)

        self.age_person_entry = CustomEntry(master=self.frame_infos_personne_1)
        self.profession_person_entry = CustomEntry(master=self.frame_infos_personne_1)


        self.var_residence, self.var_accident = StringVar(), StringVar()
        self.pays_residence_person_entry = CustomCombobox(master=self.frame_infos_personne_1)
        self.pays_accident_person_entry = CustomCombobox(master=self.frame_infos_personne_1)

        self.smig_pays_residence_enty = CustomEntry(master=self.frame_infos_personne_1)
        self.smig_pays_accident_entry = CustomEntry(master=self.frame_infos_personne_1)

        self.salary_entry = CustomEntry(master=self.frame_infos_personne_1)
        self.salary_new_entry = CustomEntry(master=self.frame_infos_personne_1)

        self.infos_but = CTkButton(self.frame_infos_personne_1)

        self.duree_1 = CustomEntry(master=self.frame_infos_personne_it)
        self.taux_1 = CustomEntry(master=self.frame_infos_personne_it)
        self.duree_2 = CustomEntry(master=self.frame_infos_personne_it)
        self.taux_2 = CustomEntry(master=self.frame_infos_personne_it)
        self.duree_3 = CustomEntry(master=self.frame_infos_personne_it)
        self.taux_3 = CustomEntry(master=self.frame_infos_personne_it)
        self.pretium_doloris = Combobox(master=self.frame_infos_personne_it)
        self.prejudice_esthetique = Combobox(master=self.frame_infos_personne_it)


        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # La frame de l'IP.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.incapacite_permanente_frame = CTkFrame(self.incapacite_temporaire_frame)

        pass

    def place_widgets(self):
        self.menu_bar.place(relwidth=1, relheight=0.05, relx=0, rely=0)
        self.incapacite_temporaire_but.place(relx=0.01, rely=0.1, relwidth=0.15)
        self.incapacite_permanente_but.place(relx=0.17, rely=0.1, relwidth=0.15)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # La frame de l'IT.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.incapacite_temporaire_frame.place(relwidth=0.96, relheight=0.9, relx=0.02, rely=0.07)
        self.frame_infos_personne_1.place(relwidth=0.96, relheight=0.25, relx=0.02, rely=0.04)

        self.compute_it_but.place(relx=0.850, rely=0.455, relwidth=0.10)
        self.frame_results_it.place(relwidth=0.96, relheight=0.45, relx=0.02, rely=0.50)
        self.but_save_it.place(relx=0.850, rely=0.95, relwidth=0.10)
        self.but_clean_it.place(relx=0.730, rely=0.95, relwidth=0.10)

        self.nom_person_entry.place(relx=0.02, rely=0.2, relwidth=0.25)
        self.prenom_person_entry.place(relx=0.02, rely=0.65, relwidth=0.25)

        self.age_person_entry.place(relx=0.285, rely=0.2, relwidth=0.1)
        self.profession_person_entry.place(relx=0.285, rely=0.65, relwidth=0.15)

        self.pays_residence_person_entry.place(relx=0.45, rely=0.2, relwidth=0.15, relheight=0.15)
        self.pays_accident_person_entry.place(relx=0.45, rely=0.65, relwidth=0.15, relheight=0.15)

        self.smig_pays_residence_enty.place(relx=0.620, rely=0.2, relwidth=0.12)
        self.smig_pays_accident_entry.place(relx=0.620, rely=0.65, relwidth=0.12)

        self.salary_entry.place(relx=0.755, rely=0.2, relwidth=0.12)
        self.salary_new_entry.place(relx=0.755, rely=0.65, relwidth=0.12)

        self.infos_but.place(relx=0.93, rely=0.87, relwidth=0.05, relheight=0.1)

        # Les différents labels (Pas besoin de les stocker dans des variables, ils sont directement placés).
        CTkLabel(self.frame_infos_personne_1, text="Nom :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.025, rely=0.03)
        CTkLabel(self.frame_infos_personne_1, text="Prénom :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.025, rely=0.47)
        CTkLabel(self.frame_infos_personne_1, text="Age :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.291, rely=0.03)
        CTkLabel(self.frame_infos_personne_1, text="Profession :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.290, rely=0.47)
        CTkLabel(self.frame_infos_personne_1, text="Pays de résidence :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.45, rely=0.03)
        CTkLabel(self.frame_infos_personne_1, text="Pays de l'accident :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.45, rely=0.47)
        CTkLabel(self.frame_infos_personne_1, text="SMIG :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.625, rely=0.03)
        CTkLabel(self.frame_infos_personne_1, text="SMIG :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.625, rely=0.47)
        CTkLabel(self.frame_infos_personne_1, text="Salaire avant l'accident :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.760, rely=0.03)
        CTkLabel(self.frame_infos_personne_1, text="Salaire après l'accident :",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.760, rely=0.47)
        #------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------
        self.frame_infos_personne_it.place(relwidth=0.96, relheight=0.1, relx=0.02, rely=0.35)
        CTkLabel(self.incapacite_temporaire_frame, text="IT Période 1",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.040, rely=0.33)
        CTkLabel(self.incapacite_temporaire_frame, text="IT Période 2",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.24, rely=0.33)
        CTkLabel(self.incapacite_temporaire_frame, text="IT Période 3",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.48, rely=0.33)
        CTkLabel(self.incapacite_temporaire_frame, text="Pretium Doloris",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.66, rely=0.33)
        CTkLabel(self.incapacite_temporaire_frame, text="Préjudice esthétique",
                 anchor="w", font=("Segoe UI", 14),
                 text_color="#838C9A").place(relx=0.83, rely=0.33)

        CTkLabel(self.incapacite_temporaire_frame, text="   Durée                            Taux",
                 anchor="w", font=("Segoe UI", 9),
                 text_color="#838C9A").place(relx=0.03, rely=0.365, relheight=0.015)
        CTkLabel(self.incapacite_temporaire_frame, text="Durée                            Taux",
                 anchor="w", font=("Segoe UI", 9),
                 text_color="#838C9A").place(relx=0.24, rely=0.365, relheight=0.015)
        CTkLabel(self.incapacite_temporaire_frame, text="Durée                            Taux",
                 anchor="w", font=("Segoe UI", 9),
                 text_color="#838C9A").place(relx=0.48, rely=0.365, relheight=0.015)

        self.duree_1.place(relx=0.01, rely=0.40, relwidth=0.07)
        self.taux_1.place(relx=0.09, rely=0.40, relwidth=0.07)

        self.duree_2.place(relx=0.22, rely=0.40, relwidth=0.07)
        self.taux_2.place(relx=0.30, rely=0.40, relwidth=0.07)

        self.duree_3.place(relx=0.47, rely=0.40, relwidth=0.07)
        self.taux_3.place(relx=0.55, rely=0.40, relwidth=0.07)

        self.pretium_doloris.place(relx=0.66, rely=0.40, relwidth=0.10, relheight=0.3)
        self.prejudice_esthetique.place(relx=0.83, rely=0.40, relwidth=0.10, relheight=0.3)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # La frame de l'IP.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # self.incapacite_permanente_frame.place(relwidth=0.96, relheight=0.25, relx=0.02, rely=0.35)
        pass

    def config_widgets(self):
        self.menu_bar.configure(corner_radius=1, fg_color="#d7dae6")
        self.incapacite_temporaire_but.configure(text="● Incapacité temporaire")
        self.incapacite_permanente_but.configure(text="● Incapacité permanente")

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # La frame de l'IT.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.incapacite_temporaire_frame.configure(fg_color="#f6f8fa", corner_radius=7)

        self.compute_it_but.configure(fg_color="#0b8719", border_color="#0ea617",
                                      border_width=2, hover_color="#0ea617",
                                      text="Computer")
        self.but_save_it.configure(fg_color="#0b5787", border_color="#1362bb",
                                      border_width=2, hover_color="#1362bb",
                                      text="Enregistrer")
        self.but_clean_it.configure(fg_color="#980a39", border_color="#bb134a",
                                   border_width=2, hover_color="#bb134a",
                                   text="Supprimer")
        self.smig_pays_residence_enty.configure(fg_color="#dde0ec", state=DISABLED)
        self.smig_pays_accident_entry.configure(fg_color="#dde0ec", state=DISABLED)

        self.pays_accident_person_entry.config(textvariable=self.var_accident)
        self.pays_accident_person_entry.set("Togo")
        self.fill_combobox(self.smig_pays_accident_entry, "Togo")

        self.pays_residence_person_entry.config(textvariable=self.var_residence)
        self.pays_residence_person_entry.set("Togo")
        self.fill_combobox(self.smig_pays_residence_enty, "Togo")

        self.var_residence.trace_add("write", self.on_change_residence)
        self.var_accident.trace_add("write", self.on_change_accident)

        self.infos_but.configure(fg_color="#16265c", border_width=1,
                              border_color="#dde0ec", corner_radius=5,
                              text="infos", font=("Freestyle Script", 17),
                                 text_color="white")

        # La seconde frame.
        self.frame_infos_personne_it.configure(fg_color="transparent", border_width=2, border_color="#dde0ec")
        self.duree_1.configure(placeholder_text="Jours")
        self.taux_1.configure(placeholder_text="0-100")
        self.duree_2.configure(placeholder_text="Jours")
        self.taux_2.configure(placeholder_text="0-100")
        self.duree_3.configure(placeholder_text="Jours")
        self.taux_3.configure(placeholder_text="0-100")

        self.pretium_doloris.config(font=("Segoe UI", 11),
                                    values=["-", "Très léger",
                                            "Léger",
                                            "Modéré",
                                            "Moyen",
                                            "Assez important",
                                            "Très important",
                                            "Exceptionnel"], state="readonly")
        self.prejudice_esthetique.config(font=("Segoe UI", 11),
                                         values=["-", "Très léger",
                                            "Léger",
                                            "Modéré",
                                            "Moyen",
                                            "Assez important",
                                            "Très important",
                                            "Exceptionnel"], state="readonly")
        self.pretium_doloris.set("-")
        self.prejudice_esthetique.set("-")

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # La frame de l'IP.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.incapacite_permanente_frame.configure(fg_color="#f6f8fa", corner_radius=7)


        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# La frame de l'IP.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def fill_combobox(self, combobox, value: str):
        combobox.configure(state="normal")
        combobox.insert(0, self.smig_cima.get(value))
        combobox.configure(state=DISABLED)

    def on_change_accident(self, *args):
        print("Hello world")
        self.smig_pays_accident_entry.configure(state="normal")
        self.smig_pays_accident_entry.delete(0, END)
        self.smig_pays_accident_entry.insert(0, self.smig_cima.get(self.var_accident.get()))
        self.smig_pays_accident_entry.configure(state=DISABLED)

        # Algorithme de comparaison des smig.
        if self.smig_cima.get(self.var_accident.get()) > self.smig_cima.get(self.var_residence.get()):
            self.smig_pays_accident_entry.configure(border_color="red")
            self.smig_pays_residence_enty.configure(border_color="#dde0ec")
        else:
            self.smig_pays_accident_entry.configure(border_color="#dde0ec")
            self.smig_pays_residence_enty.configure(border_color="red")
        pass

    def on_change_residence(self, *args):
        print("Hello world")
        self.smig_pays_residence_enty.configure(state="normal")
        self.smig_pays_residence_enty.delete(0, END)
        self.smig_pays_residence_enty.insert(0, self.smig_cima.get(self.var_residence.get()))
        self.smig_pays_residence_enty.configure(state=DISABLED)

        # Algorithme de comparaison des smig.
        if self.smig_cima.get(self.var_accident.get()) > self.smig_cima.get(self.var_residence.get()):
            self.smig_pays_accident_entry.configure(border_color="red")
            self.smig_pays_residence_enty.configure(border_color="#dde0ec")
        else:
            self.smig_pays_accident_entry.configure(border_color="#dde0ec")
            self.smig_pays_residence_enty.configure(border_color="red")
        pass
