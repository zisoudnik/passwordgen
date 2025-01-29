from tkinter import *
import tkinter
from tkinter.ttk import *
from ttkthemes import ThemedTk
import random
import pyperclip


screen=ThemedTk(theme="aqua")
screen.configure(themebg="aqua")

screen.title("Password Generator App")
screen.geometry('400x400')



letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%"
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%"

def encrypt():
    a=entry1.get()
    entry2.delete(0,END)
    encr_pass = ''
    shift = 3

    for i in a:
        if i in characters:
            pos = characters.index(i)
            new_pos = (pos + shift) % len(characters)
            encr_pass += characters[new_pos]
        else:
            encr_pass += i
    entry2.insert(END,encr_pass)
    print(encr_pass)
def generate():
    global password
    strength = level.get()
    length = int(combo.get())
    print(length, strength)
    password = ''

    if strength == 1:
        for i in range(length):
            a = random.choice(letters)
            password += a


    elif strength == 2:
        lettersnumbers = letters + numbers
        for i in range(length):
            b = random.choice(lettersnumbers)
            password += b

    elif strength == 3:
        lettersnumberssymbols = letters + numbers + symbols
        for i in range(length):
            c = random.choice(lettersnumberssymbols)
            password += c
    print(password)
    entry1.insert(END, password)

def decrypt():
    passw = entry2.get()
    entry3.delete(0,END)
    characters = letters + numbers + symbols
    encr_pass = ''
    shift = -3

    for i in passw:
        if i in characters:
            pos = characters.index(i)
            new_pos = (pos + shift) % len(characters)
            encr_pass += characters[new_pos]
        else:
            encr_pass += i
    entry3.insert(END, encr_pass)


def copy():
    pyperclip.copy(entry1.get())

screen = Tk()
#screen =

title1=Label(screen,text="Password:")
title2=Label(screen,text="Length:")
title3=Label(screen,text="Encrypted:")
entry1=Entry(screen)
combo=Combobox(screen)
combo['values']=('8','10','12','32')
entry2=Entry(screen)
btn1=Button(screen,text="Copy",command=copy)
btn2=Button(screen,text="Generate",command=generate)
level=IntVar()
rad1=Radiobutton(screen,text="Low",value=1,variable=level)
rad2=Radiobutton(screen,text="Medium",value=2,variable=level)
rad3=Radiobutton(screen,text="Storng",value=3,variable=level)
btn3=Button(screen,text="Copy")
btn4=Button(screen,text="Encrypt",command=encrypt)
btn5=Button(screen,text="Decrypt",command=decrypt)
entry3=Entry(screen)
title4=Label(screen,text="Decrypted")

title1.grid(row=0,column=0)
title2.grid(row=1,column=0)
title3.grid(row=2,column=0)
title4.grid(row=3,column=0)
entry1.grid(row=0,column=1)
combo.grid(row=1,column=1)
entry2.grid(row=2,column=1)
entry3.grid(row=3,column=1)
btn1.grid(row=0,column=2)
btn2.grid(row=0,column=3)
btn3.grid(row=0,column=3)
rad1.grid(row=1,column=2)
rad2.grid(row=1,column=3)
rad3.grid(row=1,column=4)
btn3.grid(row=2,column=2)
btn4.grid(row=2,column=3)
btn5.grid(row=2,column=4)












































screen.mainloop()