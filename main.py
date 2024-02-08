import app
import tkinter as tk
import os
import sqlite3




if __name__ == "__main__":
    BASE_PATH=os.path.expanduser("~")
    CONF_DIR_PATH=BASE_PATH+"/.pytodo/"
    
    if os.path.exists(CONF_DIR_PATH) == False:
        os.makedirs(CONF_DIR_PATH)

    print(CONF_DIR_PATH)
    
    con=sqlite3.connect(CONF_DIR_PATH+"pytodo.db")
    cur=con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY,
            text TEXT NOT NULL,
            checked INTEGER NOT NULL
        );
    """)

    root = tk.Tk()
    app.App(root, con)
    root.mainloop()
    con.close()