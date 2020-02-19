import tkinter as tk
from tkinter import messagebox
from utils.password_manager import PassMng
from utils.grant_access import Granter


def login():
    # pass_entry.get()
    access = Granter('masterpassword')
    if not access.granted:
        messagebox.showerror(title='!! Invalid Password !!',
                             message='You have entered an invalid master password.\nTry again.')
        pass_entry.delete(0, tk.END)
    else:
        entered()


def entered():
    clear_frame(main_frame)
    root.geometry('500x250')
    main_frame.config(width=500, height=250)

    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
    scrollbar.place(relx=0.95, y=0, relheight=0.7)
    accounts = PassMng.get_accounts()
    account_list_box = tk.Listbox(main_frame, yscrollcommand=scrollbar)
    account_list_box.place(x=0, y=0, relwidth=0.95, relheight=0.7)
    scrollbar.config(command=account_list_box.yview)
    for account in accounts:
        print(account)
        name, oid = account
        account_list_box.insert(oid, f'{name.title()}')

    add_btn = tk.Button(main_frame, text='Add', width=15, command=add_pass)
    add_btn.place(x=5, rely=0.8)

    get_pass_btn = tk.Button(main_frame, text='Get Password', width=15, command=lambda: get_pass(account_list_box))
    get_pass_btn.place(x=150, rely=0.8)

    delete_entry_btn = tk.Button(main_frame, text='Delete', width=15, command=lambda: delete(account_list_box))
    delete_entry_btn.place(x=295, rely=0.8)


def add_pass():
    pass


def get_pass(lb: tk.Listbox):
    pass


def delete(lb: tk.Listbox):
    pass


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
