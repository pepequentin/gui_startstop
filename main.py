import tkinter as tk
from tkinter import ttk
import psutil
import threading

# Install required packages
# pip install psutil
# pip install customtkinter

# Function to update the state of various processes
def update_process_states(process_states):
    for process in psutil.process_iter(['pid', 'name']):
        if 'ankama launcher.exe' in process.info['name'].lower():
            process_states["Ankama Launcher.exe"] = True
        elif 'brave.exe' in process.info['name'].lower():
            process_states["brave.exe"] = True
        elif 'excel.exe' in process.info['name'].lower():
            process_states["excel.exe"] = True
    return process_states

# Custom ToggleButton widget
class ToggleButton(tk.Frame):
    def __init__(self, master=None, text="", initial_state=False, **kwargs):
        super().__init__(master, **kwargs)
        self.value = tk.BooleanVar(value=initial_state)

        # Add text to the left of the slider using a Label with wraplength
        self.left_label = tk.Label(self, text=text, anchor="w", padx=5)
        self.left_label.grid(row=0, column=0, sticky="w")

        # Create a slider
        self.slider = ttk.Checkbutton(self, variable=self.value, command=self.toggle)
        self.slider.grid(row=0, column=1, padx=5, pady=5)

        # Add text to the right of the slider using a Label with wraplength
        self.right_label = tk.Label(self, text="Off", anchor="w", padx=5, foreground="red")
        self.right_label.grid(row=0, column=2, sticky="w")

        # Update text and color based on the initial state
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

# Main application class
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toggle Buttons")

        # Dictionary to store the state of each process
        process_states = {
            'Ankama Launcher.exe': False,
            'brave.exe': False,
            'excel.exe': False,
            # Add other processes if needed
        }
        process_states = update_process_states(process_states)

        # Create multiple ToggleButtons with different texts and initial states
        self.toggle1 = ToggleButton(self, text="Ankama", initial_state=process_states["Ankama Launcher.exe"])
        self.toggle1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.toggle2 = ToggleButton(self, text="Brave", initial_state=process_states["brave.exe"])
        self.toggle2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.toggle3 = ToggleButton(self, text="Excel", initial_state=process_states["excel.exe"])
        self.toggle3.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Adjust the window size
        self.geometry("500x200")

        # Start the process checking loop in a thread
        self.thread = threading.Thread(target=self.check_processes)
        self.thread.daemon = True  # The thread will stop when the main program ends
        self.thread.start()

    def check_processes(self):
        while True:

            # Dictionary to store the state of each process
            process_states = {
                'Ankama Launcher.exe': False,
                'brave.exe': False,
                'excel.exe': False,
                # Add other processes if needed
            }
            process_states = update_process_states(process_states)
            # Check the state of processes
            self.toggle1.set_initial_state(process_states['Ankama Launcher.exe'])
            self.toggle2.set_initial_state(process_states['brave.exe'])
            self.toggle3.set_initial_state(process_states['excel.exe'])
            
            # Wait for 4 seconds before the next check
            threading.Event().wait(4)

if __name__ == "__main__":
    app = App()
    app.mainloop()
