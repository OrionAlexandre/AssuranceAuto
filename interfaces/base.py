from abc import ABC, abstractmethod
from customtkinter import CTk, CTkFrame, CTkEntry
from functools import lru_cache
from tkinter import ttk
from tkinter.constants import DISABLED


MAX_SIZE_MEMOIZATION = 1000


class CustomFrame(CTkFrame, ABC):
    def __init__(self, master: CTk | CTkFrame):
        super(CustomFrame, self).__init__(master=master)

        self.__name = ""

        self.config_frame()
        self.create_widgets()
        self.place_widgets()
        self.config_widgets() # Chaque custom frame aura un nom afin de permettre sa manipulation plutard dans le programme.

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @lru_cache(maxsize=MAX_SIZE_MEMOIZATION)
    @abstractmethod
    def config_frame(self):
        pass

    @lru_cache(maxsize=MAX_SIZE_MEMOIZATION)
    @abstractmethod
    def create_widgets(self):
        pass

    @lru_cache(maxsize=MAX_SIZE_MEMOIZATION)
    @abstractmethod
    def place_widgets(self):
        pass

    @lru_cache(maxsize=MAX_SIZE_MEMOIZATION)
    @abstractmethod
    def config_widgets(self):
        pass


class CustomEntry(CTkEntry, ABC):
    def __init__(self, master: CTk | CTkFrame):
        super(CustomEntry, self).__init__(master=master)

        self.configure(font=("Segoe UI", 15),
                       border_width=2, border_color="#dde0ec")
    pass


class CustomCombobox(ttk.Combobox, ABC):
    def __init__(self, master: CTk | CTkFrame):
        super(CustomCombobox, self).__init__(master=master)

        self.values = ["Bénin",
                       "Burkina Faso",
                       "Cameroun",
                       "Centrafrique",
                       "Congo (brazaville)",
                       "Côte d'Ivoire",
                       "Gabon",
                       "Guinée Bissau",
                       "Guinée Equatoriale",
                       "Mali",
                       "Niger",
                       "Sénégal",
                       "Tchad",
                       "Togo"]
        self.__smig: float = 0.

        self.config(font=("Segoe UI", 14),
                    values=self.values,
                    state="readonly")
        self.set(self.values[-1])

        self.smig_cima = {"Gabon": 150000,
                          "Guinée Équatoriale": 128000,
                          "Congo": 90000,
                          "Côte d'Ivoire": 75000,
                          "Sénégal": 64223,
                          "Tchad": 60000,
                          "Cameroun": 60000,
                          "Togo": 52500,
                          "Bénin": 52000,
                          "Burkina Faso": 45000,
                          "Mali": 40000,
                          "Centrafrique": 36000,
                          "Niger": 30047}
    pass


class CustomResultatEntry(CTkEntry):
    def __init__(self, master: CTk | CTkFrame):
        super(CustomResultatEntry, self).__init__(master=master)

        self.configure(font=("Segoe UI", 15),
                   border_width=2, border_color="#dde0ec", fg_color="#dde0ec", state=DISABLED)
    pass

