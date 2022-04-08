from tkinter import ttk
import tkinter as tk
import sqlite3

with sqlite3.connect("details.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY AUTOINCREMENT, username text NOT NULL, password text NOT NULL);""")

def add_new_user():
    user_name = username.get()
    passwd = password1.get()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username ='" + user_name + "';")
    result = cursor.fetchone()
    commited = False

    if int(result[0]) > 0:
        error["text"] = "Error " + str(result[0]) + " USERS are using this username"
    else:
        cursor.execute("INSERT INTO users(username,password) VALUES (?,?);",(user_name,passwd))
        db.commit()
        commited = True
    if commited:
        cursor.execute("SELECT COUNT(*) FROM users WHERE username ='" + user_name + "';")
        result = cursor.fetchone()
        if int(result[0]) > 0:
            error["text"] = user_name + " inseted Successfully to DataBase"
        else:
            error["text"] = "Error when try to insert" + user_name + " to DataBase"

def find_my_password():
    old_password.delete(0,tk.END)
    user_name = serchName.get()
    cursor.execute("SELECT password FROM users WHERE username ='" + user_name + "';")
    result = cursor.fetchone()
    if str(result) == "None":
        error["text"] = "None"
    else:
        old_password.insert(0, result[0])
        #old_password.config(text = result[0]) #["text"] = result[0]

def show_all():
    print("in show_all")
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall() 
    tree.delete(*tree.get_children()) 
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)    

def change_password():
    user_name = serchName.get()
    new_password = old_password.get();
    cursor.execute("SELECT COUNT(*) FROM users WHERE username ='" + user_name + "';")
    result = cursor.fetchone()

    if int(result[0]) == 0:
        error["text"] = "Error cannot find this username"
    else:
        cursor.execute("UPDATE users SET password = ? WHERE username = ?;",(new_password,user_name))
        db.commit()
        commited = True
    if commited:
        cursor.execute("SELECT password FROM users WHERE username ='" + user_name + "';")
        result = cursor.fetchone()
        if str(result) == "None":
            error["text"] = "Error Cannot Find user"
        else:
            error["text"] = "Password changed to " + result[0]


window = tk.Tk()
window.geometry("650x680")
window.title('SQLITE SIMPLE TKINTER GUI')
window.iconbitmap('@c.xbm');

error = tk.Message(text="",width=250)
error.place(x=30, y=10, width=250, height=20)
error.config(bg="pink",padx=0)

lable1 = tk.Label(text= "Enter Username:")
lable1.place(x=30,y=40)
lable1.config(bg="lightgreen",padx=0)

username = tk.Entry(text = "")
username.place(x=150,y=40,width=200,height=25)

lable2 = tk.Label(text= "Enter Password :")
lable2.place(x=30,y=80)
lable2.config(bg="lightgreen",padx=0)

password1 = tk.Entry(text = "")
password1.place(x=150,y=80,width=200,height=25)

button = tk.Button(text= "ADD",command=add_new_user)
button.place(x=150,y=120,width=75,height=35)

lable3 = tk.Label(text= "User ID :")
lable3.place(x=30,y=180)
lable3.config(bg="yellow",padx=0)

serchName = tk.Entry(text = "")
serchName.place(x=150,y=180,width=100,height=25)

old_password = tk.Entry(text = "")
old_password.place(x=280,y=180,width=200,height=25)

button2 = tk.Button(text= "FIND Password",command=find_my_password)
button2.place(x=150,y=220,width=105,height=35)

button3 = tk.Button(text= "Change Password",command=change_password)
button3.place(x=300,y=220,width=105,height=35)

button4 = tk.Button(text= "Show All",command=show_all)
button4.place(x=250,y=270,width=105,height=35)

tree = ttk.Treeview(window,column=("c1", "c2", "c3"), show='headings')
tree.column("#1")
tree.heading("#1", text="ID")
tree.column("#2")
tree.heading("#2", text="username")
tree.column("#3")
tree.heading("#3", text="password")
tree.place(x=20,y=320)

window.mainloop()
