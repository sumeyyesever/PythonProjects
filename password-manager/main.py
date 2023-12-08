from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_name = web_input.get()
    email_name = mail_input.get()
    password_name = password_input.get()

    if web_name == "" or password_name == "":
        messagebox.showinfo("Oops", "Please do not leave empty fields.")
    else:
        data_string = f"{web_name} - {email_name} - {password_name}"
        with open("data.txt", mode="a") as file:
            file.write(f"{data_string}\n")
        web_input.delete(0, "end")
        password_input.delete(0, "end")
        web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)
web_label.focus()

web_input = Entry(width=50)
web_input.grid(row=1, column=1, columnspan=2)

mail_label = Label(text="Email/Username: ")
mail_label.grid(row=2, column=0)

mail_input = Entry(width=50)
mail_input.grid(row=2, column=1, columnspan=2)
mail_input.insert(0, "sumeysever@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=random_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
