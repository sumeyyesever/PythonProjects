import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tick = []
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = 15
    short_break_sec = 5
    long_break_sec = 6
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global tick
        if reps % 2 == 0:
            tick.append("✔")
            tick_string = ''.join(tick)
            label_tick.config(text=tick_string)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer")
timer_label.grid(row=0, column=1)
timer_label.config(font=(FONT_NAME, 34, "normal"), fg=GREEN, bg=YELLOW)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 100, image=tomato_img)
timer_text = canvas.create_text(105, 120, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

label_tick = Label()
label_tick.grid(row=3, column=1)
label_tick.config(font=(FONT_NAME, 13, "bold"), bg=YELLOW, fg=GREEN)


window.mainloop()
