import tkinter as tk


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result
    

class Todo:
    def __init__(self, master, text, checked, id):
        self.master = master
        self.text = text
        self.id = id
        self.checked = tk.BooleanVar(value=checked)

        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.X)

        self.checkbox = tk.Checkbutton(
            self.frame, variable=self.checked, command=self.toggle_strike
        )
        self.checkbox.pack(side=tk.LEFT)

        self.label = tk.Label(self.frame, text=self.text, font=("Arial", 12))
        self.label.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete)
        self.delete_button.pack(side=tk.RIGHT)

    def toggle_strike(self):
        if self.checked.get():
            self.label.config(text=strike(self.text))
        else:
            self.label.config(text=self.text)

    def delete(self):
        self.frame.destroy()

