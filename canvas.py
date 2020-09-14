import tkinter
import tkinter.messagebox as tk

def helloCallBack(C):
    tk.showinfo( "Hello Python", "pretty picture")

    coord = 10, 50, 240, 210
    arc = C.create_arc(coord, start=0, extent=150, fill="red")


top = tkinter.Tk()
C = tkinter.Canvas(top, bg="blue", height=250, width=300)
B = tkinter.Button(top, text="Hello", command = helloCallBack(C))

B.pack()
C.pack()
top.mainloop()