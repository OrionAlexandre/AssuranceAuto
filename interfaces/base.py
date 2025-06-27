from customtkinter import CTk, CTkFrame
from abc import ABC, abstractmethod

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

