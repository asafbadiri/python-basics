from tkinter import *

win=Tk()
win.title("Calculater TKinter");
win.geometry("300x165")
#window.iconbitmap('@c.xbm');

def cal_sum(a,b): return a + b
def cal_sub(a,b): return a - b
def cal_mult(a,b): return a * b
def cal_div(a,b): return "Dont use Zero" if b == 0 else a/b

def action(act):
   funcions_list = {'cal_sum':(cal_sum,"+"),'cal_sub':(cal_sub,"-"),'cal_mult':(cal_mult,"*"),'cal_div':(cal_div,"/")}
   try:
      sm = funcions_list[act][0](int(a.get()),int(b.get()))
      if isinstance(sm, float):
            txt = "{0} {1} {2} = {3:.3}".format(a.get(),funcions_list[act][1],b.get(),sm)
      else:
            txt = "{0} {1} {2} = {3}".format(a.get(),funcions_list[act][1],b.get(),sm)     
   except ValueError:
         txt = "Wrong inputs"
   label.config(text=txt)

Label(win, text="Enter First Number", font=('Calibri 10')).grid(row=1, column= 1,columnspan=4)
a=Entry(win, width=35)
a.grid(row=2, column= 1,columnspan=4)
Label(win, text="Enter Second Number", font=('Calibri 10')).grid(row=3, column= 1,columnspan=4)
b=Entry(win, width=35)
b.grid(row=4, column= 1,columnspan=4)

label=Label(win, text="Total: ", font=('Calibri 15'))
label.grid(row=5, column= 1, columnspan=4, padx=20)

Button(win, text="ADD", command= lambda: action("cal_sum")).grid(row=6, column= 1)
Button(win, text="SUB", command= lambda: action("cal_sub")).grid(row=6, column= 2)
Button(win, text="MULT", command= lambda: action("cal_mult")).grid(row=6, column= 3)
Button(win, text="DIV", command= lambda: action("cal_div")).grid(row=6, column= 4)

win.mainloop()
