from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import randint, choice, shuffle


def password_gen():
    pw_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    emai = email_entry.get()
    p = pw_entry.get()

    if len(web) == 0 or len(emai) == 0 or len(p) == 0:
        messagebox.showinfo("Error", "Please enter all fields")
    else:
        is_ok = messagebox.askokcancel("Confirmation", f"Website: {web} \n Email: {emai} \n Password: {p} \n Save?")

        if is_ok:
            with open("password.txt", "a") as file:
                file.write(f"{web} | {emai} | {p}\n")
                website_entry.delete(0, END)
                pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(window, text='Website')
website.grid(column=0, row=1)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email = Label(window, text='Email')
email.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sm997190@gmail.com")

pw = Label(window, text='Password')
pw.grid(column=0, row=3)

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

generate = Button(text="Generate Password", command=password_gen)
generate.grid(column=2, row=3)

add = Button(text="Add Password", width=50, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
