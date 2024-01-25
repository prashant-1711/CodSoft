from tkinter import *
from tkinter import messagebox

#even if the app is closed the list is stored in a database.
import sqlite3

connectSql = sqlite3.connect('ToDoList.db')
cursor = connectSql.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
''')
connectSql.commit()

def CheckIerror():
    if EnterTask_Field.get() == "":
        messagebox.showerror("Input Error", "Enter a task.")
        return 0
    else:
        return 1

def clear_TaskNumField():
    TaskNumField.delete(0.0, END)

def clear_task_field():
    EnterTask_Field.delete(0, END)

def insert_task(event=None):
    value = CheckIerror()
    if value == 0:
        return

    content = EnterTask_Field.get()
    cursor.execute("INSERT INTO tasks (content) VALUES (?)", (content,))
    connectSql.commit()

    display_tasks()

    clear_task_field()
    EnterTask_Field.focus_set()

def delete_task(event=None):
    number = TaskNumField.get(1.0, END).strip()

    if number == "":
        messagebox.showerror("Input Error", "Enter a task number to delete.")
        return

    try:
        display_index = int(number)
        cursor.execute("SELECT id FROM tasks")
        tasks = cursor.fetchall()

        if 1 <= display_index <= len(tasks):
            task_id = tasks[display_index - 1][0]
            cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            connectSql.commit()

            display_tasks()
        else:
            messagebox.showerror("Input Error", "Task number Invalid.")
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid task number.")

    clear_TaskNumField()
    text_area.focus_set()

def display_tasks():
    text_area.config(state=NORMAL)
    text_area.delete(1.0, END)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    for i, task in enumerate(tasks, start=1):
        text_area.insert("end", f" {i} . {task[1]}\n")

    text_area.config(state=DISABLED)

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="black")

    gui.title("To Do List ")

    gui.geometry("300x350")

    EnterTask_label = Label(gui, text="Enter Your Task", bg="black", fg="gold")
    EnterTask_Field = Entry(gui, bg="black", fg="gold")
    submit_button = Button(gui, text="Submit", fg="black", bg="gold", command=insert_task)

    text_area = Text(gui, height=7, width=30, font="lucida 13", state=DISABLED, bg="black", fg="gold")

    task_number_label = Label(gui, text="Delete Task Number", bg="black", fg="gold")
    TaskNumField = Text(gui, height=1, width=2, font="lucida 13", bg="black", fg="gold")

    delete_button = Button(gui, text="Delete", fg="black", bg="gold", command=delete_task)

    exit_button = Button(gui, text="Exit", fg="black", bg="gold", command=exit)

   #can use ENTER Key to interact with submit and delete buttons.
    EnterTask_Field.bind("<Return>", insert_task)
    TaskNumField.bind("<Return>", delete_task)
    
    
    EnterTask_label.grid(row=0, column=2)
    EnterTask_Field.grid(row=1, column=2, ipadx=50)
    submit_button.grid(row=2, column=2)
    text_area.grid(row=3, column=2, padx=10, sticky=W)
    task_number_label.grid(row=4, column=2, pady=5)
    TaskNumField.grid(row=5, column=2)
    delete_button.grid(row=6, column=2, pady=5)
    exit_button.grid(row=7, column=2)

    display_tasks()

    gui.mainloop()

    connectSql.close()
