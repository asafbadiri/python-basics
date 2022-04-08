from tkinter import *

win=Tk()
win.title("Calculater TKinter");
win.geometry("300x165")
#window.iconbitmap('@c.xbm');

def cal_sum(a,b):
      return a + b

def cal_sub(a,b):
   return a - b

def cal_mult(a,b):
   return a * b

def cal_div(a,b):
   return "Dont use Zero" if b == 0 else a/b

def action(act):
   try:
      t1=int(a.get())
      t2=int(b.get())
      match act:
         case "ADD":
            sm = cal_sum(t1,t2)
            txt = "{0} + {1} = {2}".format(t1,t2,sm)
         case "SUB":
            sm = cal_sub(t1,t2)
            txt = "{0} - {1} = {2}".format(t1,t2,sm)
         case "MULT":
            sm = cal_mult(t1,t2)
            txt = "{0} * {1} = {2}".format(t1,t2,sm)
         case "DIV":
            div = cal_div(t1,t2)
            if isinstance(div, str):
               txt = "{0} / {1} = {2}".format(t1,t2,div)
            else:
               txt = "{0} / {1} = {2:.3}".format(t1,t2,div)
   except ValueError:
      txt = "Wrong inputs"
   label.config(text=txt)

Label(win, text="Enter First Number", font=('Calibri 10')).grid(row=1, column= 1,columnspan=4)
a=Entry(win, width=35)
a.grid(row=2, column= 1,columnspan=4)
a.insert(0, "First number")
Label(win, text="Enter Second Number", font=('Calibri 10')).grid(row=3, column= 1,columnspan=4)
b=Entry(win, width=35)
b.grid(row=4, column= 1,columnspan=4)

label=Label(win, text="Total: ", font=('Calibri 15'))
label.grid(row=5, column= 1, columnspan=4, padx=20)

Button(win, text="ADD", command= lambda: action("ADD")).grid(row=6, column= 1)
Button(win, text="SUB", command= lambda: action("SUB")).grid(row=6, column= 2)
Button(win, text="MULT", command= lambda: action("MULT")).grid(row=6, column= 3)
Button(win, text="DIV", command= lambda: action("DIV")).grid(row=6, column= 4)

win.mainloop()
