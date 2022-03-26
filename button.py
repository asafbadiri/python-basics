from tkinter import *

#The window main widget
root = Tk()

def myClick():
    myLable = Label(root, fg= "blue", text= 5+3).pack()

myButton = Button(root, text="Click Me",background = "red", padx=50, pady= 80, command=myClick).pack()#grid(row=1,column=1)


root.mainloop()