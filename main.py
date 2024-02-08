import tkinter as tk
import tkinter.font as tkFont


class Todo:
    def __init__(self, master, text):
        self.master = master;
        self.text = text;
        self.checked = tk.BooleanVar(value=False)

        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.X)

        self.checkbox = tk.Checkbutton(self.frame, variable=self.checked, command=self.toggle_strike)
        self.checkbox.pack(side=tk.LEFT)

        self.label = tk.Label(self.frame, text=self.text, font=("Helvetica", 12))
        self.label.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete)
        self.delete_button.pack(side=tk.RIGHT)

    def toggle_strike(self):
        if self.checked.get():
            self.label.config(font=("Helvetica", 12, "strike"))
        else:
            self.label.config(font=("Helvetica", 12))

    def delete(self):
        self.frame.destroy()


class App:
    def __init__(self, root):
        self.root = root;
        self.root.title("PyTodo")
        self.dimensions=(360, 500)
        
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (self.dimensions[0], self.dimensions[1], (screenwidth - self.dimensions[0]) / 2, (screenheight - self.dimensions[1]) / 2)
        
        self.root.geometry(align_str)
        self.root.resizable(width=False, height=False)

        self.todo_items = []
        
        ft = tkFont.Font(family='Arial',size=10)

        self.todo_box=tk.Frame(root)
        self.todo_box["borderwidth"] = "1px"
        self.todo_box.place(x=10,y=10,width=330,height=444)

    
        self.input_box=tk.Entry(root)
        self.input_box["borderwidth"] = "1px"
        self.input_box["relief"] = tk.FLAT
        self.input_box["font"] = ft
        self.input_box.place(x=10,y=460,width=240,height=30)

        submit_button=tk.Button(root)
        submit_button["bg"] = "#0d9467"
        submit_button["font"] = ft
        submit_button["relief"] = tk.FLAT
        submit_button["fg"] = "#ffffff"
        submit_button["justify"] = "center"
        submit_button["text"] = "save"
        submit_button.place(x=260,y=460,width=83,height=30)
        submit_button["command"] = self.save_todo



    def save_todo(self):
        value = self.input_box.get()

        if value:
            item = Todo(self.todo_box, value)
            self.input_box.delete(0, tk.END)


def prepare_config_directory():
    pass


if __name__ == "__main__":
    prepare_config_directory()

    root = tk.Tk()
    App(root)
    root.mainloop()
