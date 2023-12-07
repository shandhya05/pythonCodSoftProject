from tkinter import *
import pyperclip
import random

root = Tk()
root.geometry("400x400")  # Corrected typo: "400x400" instead of "400*400"

passtr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2',
             '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^',
             '&', '*', '(', ')']  # Corrected missing comma in the list

    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passtr.set(password)

def copytoclipboard():
    random_password = passtr.get()
    pyperclip.copy(random_password)

Label(root, text="Password Generator Application", font="Calibri 20 bold").pack()
Label(root, text="Enter Password Length").pack(pady=3)  # Corrected typo: "pad" to "pady"
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate Password", command=generate).pack()
Entry(root, textvariable=passtr).pack(pady=3)
Button(root, text="Copy to Clipboard", command=copytoclipboard).pack()  # Corrected function name

root.mainloop()