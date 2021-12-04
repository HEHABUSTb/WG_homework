from tkinter import *
from tkinter import messagebox
from TestData.create_sql_data import CreateDB

def create_table():
    try:
        create = CreateDB()
        value = int(entry_text.get())
        create.create_ships_table(how_many_ships=value)
        create.create_engines_table()
        create.create_hulls_table()
        create.create_weapons_table()
        messagebox.showinfo(message='Success!', title='Success message')
    except Exception as e:
        messagebox.showerror(title='Error', message=f"Something got wrong {e}")


window = Tk()
window.geometry('240x120')
window.title('Create table')


label = Label(window, text='How many ships do you want?', font=('Arial', 10, 'bold'))

label.pack()
entry_text = Entry(window, text=200)
entry_text.insert(0, '200')
entry_text.pack()

button = Button(window, text='Create', command=create_table)
button.pack()


window.mainloop()
