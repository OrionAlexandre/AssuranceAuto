from tkinter.constants import DISABLED, END

from customtkinter import CTk, CTkFrame, set_appearance_mode, set_default_color_theme, CTkButton, CTkLabel
from tkinter import StringVar

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
        self.incapacite_temporaire_frame = CTkFrame(self)
        self.frame_infos_personne_1 = CTkFrame(self.incapacite_temporaire_frame)
        self.frame_infos_personne_it = CTkFrame(master=self.incapacite_temporaire_frame)
        self.frame_results_it = CTkFrame(master=self.incapacite_temporaire_frame)
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
        self.frame_infos_personne_it.place(relwidth=0.96, relheight=0.1, relx=0.02, rely=0.35)
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
        self.frame_infos_personne_it.configure(fg_color="transparent", border_width=2, border_color="#dde0ec")
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

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # La frame de l'IP.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.incapacite_permanente_frame.configure(fg_color="#f6f8fa", corner_radius=7)

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
