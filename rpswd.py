from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from pyperclip import copy
from random import *
class Password:
    def __init__(self):

        self.length = {'Poor': 8, 'Medium': 16, 'Strong': 32}
        self.password = ''
        self.string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*():;?'
        self.root = Tk()
        self.root.title("Random Password Generator")
        self.root.geometry("350x200")
        self.label2 = Label(self.root, text="")
        Label(self.root, text='Password :').place(x=20, y=20)
        self.entry = Entry(self.root, width=40)
        self.entry.place(x=90, y=20)
        Label(self.root, text='Strength :').place(x=26, y=55)
        self.combo = Combobox(self.root, values=("Poor", "Medium", "Strong"), state='readonly')
        self.combo.bind('<<ComboboxSelected>>')
        self.combo.place(x=90, y=55)
        Button(self.root, text='Copy', command=self.cpy).place(x=50, y=150)
        Button(self.root, text='Generate', command=self.generate).place(x=200, y=150)
        self.root.mainloop()

    def cpy(self):
        copy(self.password)
        self.label2.configure(text='Password copied')
        self.label2.place(x=140, y=100)

    def generate(self):
        try:
            self.label2.configure(text='')
            self.entry.delete(0, END)
            self.password = ''
            for _ in range(self.length[str(self.combo.get())]):
                self.password += choice(self.string)
            self.entry.insert(10, self.password)
        except KeyError:
            messagebox.showinfo("Warning", "Select the strength of the password")





k = Password()
