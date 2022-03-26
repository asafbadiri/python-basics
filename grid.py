from tkinter import *

#The window main widget
root = Tk()
#Create a lable widget
myLable = Label(root, text="Hello first Lable")
myLable2 = Label(root, text="Hello second Lable")
#Playing lable on screen
myLable.grid(row=7,column=7)
myLable2.grid(row=14,column=0)


root.mainloop()