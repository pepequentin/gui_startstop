import tkinter as tk
from tkinter import ttk
import psutil
#pip install psutil
#pip install customtkinter
class ToggleButton(tk.Frame):
    def __init__(self, master=None, text="", initial_state=False, **kwargs):
        super().__init__(master, **kwargs)
        self.value = tk.BooleanVar(value=initial_state)

        # Ajouter un texte à gauche du slider en utilisant un Label avec wraplength
        self.left_label = tk.Label(self, text=text, anchor="w", padx=5)
        self.left_label.grid(row=0, column=0, sticky="w")

        # Créer un slider
        self.slider = ttk.Checkbutton(self, variable=self.value, command=self.toggle)
        self.slider.grid(row=0, column=1, padx=5, pady=5)

        # Ajouter un texte à droite du slider en utilisant un Label avec wraplength
        self.right_label = tk.Label(self, text="Off", anchor="w", padx=5, foreground="red")
        self.right_label.grid(row=0, column=2, sticky="w")

        # Mettre à jour le texte et la couleur en fonction de l'état initial
        self.update_label()

    def toggle(self):
        self.update_label()

    def update_label(self):
        if self.value.get():
            self.right_label.config(text="On", foreground="green")
        else:
            self.right_label.config(text="Off", foreground="red")

    def set_initial_state(self, state):
        self.value.set(state)
        self.update_label()

def isbraveup():
    for process in psutil.process_iter(['pid', 'name']):
        if 'brave.exe' in process.info['name'].lower():
            return True
    return False

def isankamaup():
    for process in psutil.process_iter(['pid', 'name']):
        if 'ankama launcher.exe' in process.info['name'].lower():
            return True
    return False

def isexcelup():
    for process in psutil.process_iter(['pid', 'name']):
        if 'excel.exe' in process.info['name'].lower():
            return True
    return False


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toggle Buttons")

        # Créer plusieurs ToggleButtons avec des textes différents et des états initiaux
        self.toggle1 = ToggleButton(self, text="Ankama", initial_state=isankamaup())
        self.toggle1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.toggle2 = ToggleButton(self, text="Brave", initial_state=isbraveup())
        self.toggle2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.toggle3 = ToggleButton(self, text="Excel", initial_state=isexcelup())
        self.toggle3.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Ajuster la taille de la fenêtre
        self.geometry("500x200")

        # Lancer la boucle de vérification des processus
        self.check_processes()

    def check_processes(self):
        # Vérifier l'état des processus
        self.toggle1.set_initial_state(isankamaup())
        self.toggle2.set_initial_state(isbraveup())
        self.toggle3.set_initial_state(isexcelup())

        # Planifier la prochaine vérification dans 4000 millisecondes (4 secondes)
        self.after(4000, self.check_processes)

if __name__ == "__main__":
    app = App()
    app.mainloop()
