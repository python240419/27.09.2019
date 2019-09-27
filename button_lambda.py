from tkinter import *
import tkinter.font as font

class MyCoolWindow():
    def __init__(self, root):
        root.title("Hello World!")
        # create label
        lbl1 = Label(root, text='Hello tkinter...')
        lbl1.pack()
        hellobtn = Button(root, text="Greet",
                          width = 30,
                          command=lambda: print("hello")) # HERE !!!

        hellobtn['font'] = font.Font(size=20,
                                     weight='bold')
        hellobtn.pack()
        quitbtn = Button(root, text="Quit",fg ="red",
                         bg = "white",
                         font=font.Font(size=20),
                         command=root.quit)
        quitbtn.pack()

root = Tk() # create window
mywindow = MyCoolWindow(root)
root.mainloop() # present window - blocking

# after closing window
print("Goodbye...")
