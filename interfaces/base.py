from abc import ABC, abstractmethod
from customtkinter import CTk, CTkFrame, CTkEntry
from tkinter import ttk

class CustomFrame(CTkFrame, ABC):
    def __init__(self, master: CTk | CTkFrame):
        super(CustomFrame, self).__init__(master=master)

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

    @abstractmethod
    def config_frame(self):
        pass

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def place_widgets(self):
        pass

    @abstractmethod
    def config_widgets(self):
        pass


class CustomEntry(CTkEntry, ABC):
    def __init__(self, master: CTk | CTkFrame):
        super(CustomEntry, self).__init__(master=master)

        self.configure(font=("Segoe UI", 15),
                       border_width=2, border_color="#dde0ec")


class CustomCombobox(ttk.Combobox):
    def __init__(self, master: CTk | CTkFrame, *args):
        super(CustomCombobox, self).__init__(master=master)

        self.config(font=("Segoe UI", 15),)
