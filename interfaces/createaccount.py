
from customtkinter import CTk, CTkButton, CTkEntry, CTkFrame, CTkImage, CTkLabel
from AssuranceAuto.interfaces.base import CustomFrame
from PIL import Image


class CreateAccountFrame(CustomFrame):
    def __init__(self, master: CTk | CTkFrame):
        super(CreateAccountFrame, self).__init__(master=master)
        self.name = "CreateAccountFrame"

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
                                              command=self.connection_frame())

    def connection_frame(self):
        from AssuranceAuto.interfaces.connectaccount import ConnectionFrame
        frame = ConnectionFrame(self)
    pass

    pass