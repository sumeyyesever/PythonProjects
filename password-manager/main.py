import json
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

    new_data = {
        web_name: {
            "email": email_name,
            "password": password_name
        }
    }

    if web_name == "" or password_name == "":
        messagebox.showinfo("Oops", "Please do not leave empty fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # reading old data. after this line can be putting in else part
                data.update(new_data)  # updating old data with new data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        web_input.delete(0, "end")  # this three lines can be put in finally
        password_input.delete(0, "end")
        web_input.focus()


# -----------------------------FIND PASSWORD -----------------------------#

def find():
    web_name = web_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Oops", "File you trying to reach does not exist.")
    else:
        if web_name in data:
            mail = data[web_name]["email"]
            password = data[web_name]["password"]
            messagebox.showinfo(f"{web_name}", f"E-Mail: {mail}\nPassword: {password}")
        else:
            messagebox.showinfo(f"{web_name}", "This website does not exist in the file")

        # try:
        #    mail_pass = data[web_name]
        # except KeyError:
        #     messagebox.showinfo(f"{web_name}", "This website does not exist in the file")
        # else:
        #     messagebox.showinfo(f"{web_name}", f"Password: {mail_pass["password"]}")
# if you can do something with if and else very easily, then you should stick to if and else.
# If you can't do it with if and else very easily, and it's actually an error that's going to be thrown
# that you don't have any other way of dealing with,then you should be using the try, except, else, finally, keywords.


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

web_input = Entry(width=32)
web_input.grid(row=1, column=1)

search_button = Button(text="Search", width=13, command=find)
search_button.grid(row=1, column=2)

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
