import tkinter as tk
from tkinter import messagebox
from utils.password_manager import PassMng
from utils.grant_access import Granter


def login():
    access = Granter(pass_entry.get())
    if not access.granted:
        messagebox.showerror(title='!! Invalid Password !!',
                             message='You have entered an invalid master password.\nTry again.')
        pass_entry.delete(0, tk.END)
    else:
        clear_frame(main_frame)
        root.geometry('500x500')
        main_frame.config(width=500, height=500)


def clear_frame(frame: tk.LabelFrame):
    for child in frame.winfo_children():
        child.destroy()


root = tk.Tk()
root.geometry('350x200')
root.resizable(False, False)
root.title('All-in-One Password Manager')
PassMng.create_table()

main_frame = tk.LabelFrame(root, text='Main Frame', width=350, height=200)
main_frame.grid(row=0, column=0)
main_frame.grid_propagate(False)
tk.Label(main_frame, text='Master Password: ').grid(row=0, column=0)
pass_entry = tk.Entry(main_frame, show=' ')
pass_entry.grid(row=0, column=1)
login_button = tk.Button(main_frame, text='Login', width=20, command=login)
login_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
