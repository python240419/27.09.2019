from tkinter import *

# place items on self (window)
# IntVar
# StringVar
# grid
# validate?
# listbox ?

class CalculatorWindow:
    def __init__(self, root):
        self.root= root
        root.title("Calculator")
        # the next 2 lines syntax is not good since  this will not be accessed beyond this method
        # (better to place this variables on self)
        #total_label = Label(root, text="hello")
        #total_label.pack()
        # ----------------------------
        # IntVar / StringVar
        self.total_value = IntVar()
        self.total_value.set(0)
        self.total_label = Label(root,
                                 textvariable=self.total_value,
                                 font=("david", 72))
        self.total_label.pack()
        self.addBtn = Button(text="Add",
                             #command=self.add1)
                             command=lambda: self.total_value.set(self.total_value.get() + 1))
        self.addBtn.pack()
    def add1(self):
        self.total_value.set(self.total_value.get() + 1)

root = Tk()
my_window = CalculatorWindow(root)
root.mainloop()  # blocking

# targil;
# add button which decrease 1
# add button which sets the value back to 0
# with lambda?
# add string label with hello (StringVar)
# add button which modifies the text of the label to the current datetime
