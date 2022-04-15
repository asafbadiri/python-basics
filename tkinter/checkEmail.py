import sys
import re
from validate_email import validate_email
import tkinter as tk
from tkinter import ttk

class CheckMailFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.name = tk.StringVar()
        self.result_string = tk.StringVar()
        self.result_string.set("ליימיא תבותכ לש תויקוח תקידב  Good bye ! LOL")

        info_label = ttk.Label(self, text="Email:")
        email_entry = ttk.Entry(self, textvariable=self.name)
        verify_button = ttk.Button(self, text="Check", command=self.check_email)
        result_label = ttk.Label(self, textvariable=self.result_string, font=("TkTextFont",28),wraplength=600)

        # Layout form
        info_label.grid(row=0, column=0)
        email_entry.grid(row=0, column=1, sticky= tk.W )
        verify_button.grid(row=0, column=2, sticky=(tk.W +tk.E))
        result_label.grid(row=1, column=0, columnspan=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

    def check_email(self):
        if self.name.get().strip():
            email = self.name.get()
            if email_full_validation(email):
                self.result_string.set("Email " + email + " verified successfully!")
            else:
                self.result_string.set("Email " + email + " verification failed!")
        else:
            self.result_string.set("ליימיא תבותכ לש תויקוח תקידב  Good bye ! LOL")


class MyApplication(tk.Tk):
    """Hello World Main Application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window properties
        self.title("Check Email")
        self.geometry("600x400")
        self.resizable(width=False, height=False)

        # Define the UI
        CheckMailFrame(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)

def email_full_validation(email):
    pattern = "^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$"
    verify = re.search(pattern, email)
    is_valid = validate_email(
        email_address= email,
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=10,
        check_smtp=False, #True
        smtp_timeout=10,
        smtp_helo_host='my.host.name',
        smtp_from_address='my@from.addr.ess',
        smtp_skip_tls=False,
        smtp_tls_context=None,
        smtp_debug=False)
    return (is_valid and verify)

def main():
    user_input = sys.argv
    if len(user_input) == 2:
        print("Thank you for using " + user_input[0])
        email = user_input[1]
        if email_full_validation(email):
            print("Email " + email + " verified successfully!")
        else:
            print("Email " + email + " verification failed!")
    else:
        app = MyApplication()
        app.mainloop()

if __name__ == '__main__':
    main()
