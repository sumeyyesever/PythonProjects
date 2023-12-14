from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_cart = {}

# --------------------- Data --------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    new_data = data.to_dict("records")
except FileNotFoundError:
    data = pandas.read_csv("./data/italian-to-english.csv")
    new_data = data.to_dict("records")  # list

# --------------------- Button Click --------------- #


def random_word():
    global random_cart, timer
    window.after_cancel(timer)
    random_cart = random.choice(new_data)
    canvas.itemconfig(lang_title, text="Italian", fill="black")
    canvas.itemconfig(lang_word, text=random_cart["Italian"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    timer = window.after(3000, flip_card)

# ------------------- FLIP CARD -------------------- #


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(lang_title, text="English", fill="white")
    canvas.itemconfig(lang_word, text=random_cart["English"], fill="white")


# ------------------ REMOVE CARD ----------------------- #

def remove_card():
    global random_cart
    new_data.remove(random_cart)
    new_dataf = pandas.DataFrame(new_data)
    new_dataf.to_csv("./data/words_to_learn.csv")
    random_word()


# ---------------------- IU SETUP ----------------------------- #


# first create the window
window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

# second canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
lang_title = canvas.create_text(400, 150, text="Italian", font=("Ariel", 40, "italic"))
lang_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

timer = window.after(3000, flip_card)

correct_button_image = PhotoImage(file="./images/right.png")
wrong_button_image = PhotoImage(file="./images/wrong.png")

correct_button = Button(image=correct_button_image, highlightthickness=0, command=remove_card)
correct_button.grid(row=2, column=1)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=2, column=2)

random_word()


window.mainloop()

