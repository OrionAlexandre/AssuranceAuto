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


class FrameManager:
    def __init__(self, master):
        self.master = master

        self.load_frames()
        pass

    def load_frames(self):
        from AssuranceAuto.interfaces.connectaccount import ConnectionFrame
        from AssuranceAuto.interfaces.createaccount import CreateAccountFrame

        self.frames_dict: dict[str: CTkFrame] = dict()

        connect_account_frame = ConnectionFrame(self.master)
        create_account_frame = CreateAccountFrame(self.master)

        for frame in (connect_account_frame,create_account_frame):
            self.frames_dict[frame.name] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
            print(len(self.frames_dict.keys()), frame.name)
        pass

    def show_frame(self, frame_name):
        self.frames_dict[frame_name].tkraise()
        pass
    pass