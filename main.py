import tkinter as tk
from tkinter import ttk
import psutil
import threading

#pip install psutil
#pip install customtkinter







def update_process_states(process_states):
    for process in psutil.process_iter(['pid', 'name']):
        if 'ankama launcher.exe' in process.info['name'].lower():
            process_states["Ankama Launcher.exe"] = True
        elif 'brave.exe' in process.info['name'].lower():
            process_states["brave.exe"] = True
        elif 'excel.exe' in process.info['name'].lower():
            process_states["excel.exe"] = True
    return process_states



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

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toggle Buttons")

        # Dictionnaire pour stocker l'état de chaque processus
        process_states = {
            'Ankama Launcher.exe': False,
            'brave.exe': False,
            'excel.exe': False,
            # Ajoutez d'autres processus si nécessaire
        }
        process_states = update_process_states(process_states)

        # Créer plusieurs ToggleButtons avec des textes différents et des états initiaux
        self.toggle1 = ToggleButton(self, text="Ankama", initial_state=process_states["Ankama Launcher.exe"])
        self.toggle1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.toggle2 = ToggleButton(self, text="Brave", initial_state=process_states["brave.exe"])
        self.toggle2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.toggle3 = ToggleButton(self, text="Excel", initial_state=process_states["excel.exe"])
        self.toggle3.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Ajuster la taille de la fenêtre
        self.geometry("500x200")

        # Lancer la boucle de vérification des processus
        # self.check_processes()
        # Lancer la boucle de vérification des processus dans un thread
        self.thread = threading.Thread(target=self.check_processes)
        self.thread.daemon = True  # Le thread s'arrêtera lorsque le programme principal se terminera
        self.thread.start()
        
    def check_processes(self):
        while True:

            # Dictionnaire pour stocker l'état de chaque processus
            process_states = {
                'Ankama Launcher.exe': False,
                'brave.exe': False,
                'excel.exe': False,
                # Ajoutez d'autres processus si nécessaire
            }
            process_states = update_process_states(process_states)
            # Vérifier l'état des processus
            self.toggle1.set_initial_state(process_states['Ankama Launcher.exe'])
            self.toggle2.set_initial_state(process_states['brave.exe'])
            self.toggle3.set_initial_state(process_states['excel.exe'])
            
            # Attendre 4 secondes avant la prochaine vérification
            threading.Event().wait(4)

if __name__ == "__main__":
    app = App()
    app.mainloop()
