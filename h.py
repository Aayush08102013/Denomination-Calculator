from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("main")

def topwin():
    # Set the top window
    top = Toplevel()
    top.geometry("200x200")
    top.title("Toplevel")
    l2 = Label(top, text="This is Toplevel window")
    l2.pack()

    top.mainloop()

l = Label(window, text="This the window window!")
btn = Button(window, text= "click here to open another window", command= topwin)

l.pack()
btn.pack()

window.mainloop()