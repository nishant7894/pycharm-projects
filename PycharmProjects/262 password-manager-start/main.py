from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
font = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letter = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbol = [choice(symbols) for _ in range(randint(8, 10))]
    pw_number = [choice(numbers) for _ in range(randint(8, 10))]
    password_list= pw_number + pw_symbol + pw_letter
    shuffle(password_list)

    password1 = "".join(password_list)
    pw_entry.insert(0, password1)
    pyperclip.copy(password1)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pw_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops..", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are details entered: \n Email: {email}\nPassword: {password}\nIs It ok to save?')

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                pw_entry.delete(0, END)
        else:
            web_entry.delete(0, END)
            pw_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=52)
web_entry.focus()
email_entry = Entry(width=52)
pw_entry = Entry(width=34)
email_entry.insert(0, "nishant@gmail.com")

web_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
pw_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
