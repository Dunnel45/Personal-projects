#!/usr/bin/python

import tkinter
import tkinter.messagebox as tk

top = tkinter.Tk()

def helloCallBack():
    tk.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text="Hello", command = helloCallBack)

B.pack()
top.mainloop()