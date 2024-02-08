import tkinter as tk
import tkinter.font as tkFont
import scrollableContainer
import todo


class App:
    def __init__(self, root, connection):
        self.root = root
        self.con = connection;
        self.cursor = self.con.cursor()
        self.root.title("PyTodo")
        self.dimensions = (360, 500)

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = "%dx%d+%d+%d" % (
            self.dimensions[0],
            self.dimensions[1],
            (screenwidth - self.dimensions[0]) / 2,
            (screenheight - self.dimensions[1]) / 2,
        )

        self.root.geometry(align_str)
        self.root.resizable(width=False, height=False)

        ft = tkFont.Font(family="Arial", size=10)

        self.todo_box = scrollableContainer.ScrollableContainer(self.root)
        self.todo_box.pack(expand=True, fill=tk.BOTH)

        self.input_box = tk.Entry(root)
        self.input_box["borderwidth"] = "1px"
        self.input_box["relief"] = tk.FLAT
        self.input_box["font"] = ft
        self.input_box.place(x=10, y=460, width=240, height=30)

        submit_button = tk.Button(root)
        submit_button["bg"] = "#0d9467"
        submit_button["font"] = ft
        submit_button["relief"] = tk.FLAT
        submit_button["fg"] = "#ffffff"
        submit_button["justify"] = "center"
        submit_button["text"] = "save"
        submit_button.place(x=260, y=460, width=83, height=30)
        submit_button["command"] = self.save_todo


        self.todos = self.load_todos()

    def save_todo(self):
        value = self.input_box.get()

        if value:
            self.cursor.execute("INSERT INTO todos (text, checked) VALUES (?, ?)", [value, False])
            self.con.commit()
            last_id = self.todos[-1][0]

            item = todo.Todo(self.todo_box.interior, value, False, last_id)
            self.input_box.delete(0, tk.END)


    def load_todos(self):
        result = []

        def delete_task(id):
            self.cursor.execute("DELETE FROM todos WHERE id = ?", (id))
            self.connection.commit()


        for row in self.cursor.execute("SELECT * FROM todos"):
            if row:
                print(row)
                id, text, checked = row[0], row[1], row[2]
                item = todo.Todo(self.todo_box.interior, text, checked, id)    
                item.delete_button.config(command=lambda id=id: delete_task(id))
                result.append((id, item))
        
        return result    

