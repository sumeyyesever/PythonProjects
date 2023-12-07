from tkinter import *

window = Tk()
window.title("miles to kilometers")
window.minsize(200, 100)
window.config(padx=20, pady=20)


entry = Entry(width=20)
entry.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label()
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)


def action():
    kilometer = int(entry.get()) * 1.6
    label3.config(text=kilometer)


button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)

window.mainloop()
