from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_question = self.canvas.create_text(150, 120,
                                                       font=("Arial", 20, "italic"),
                                                       fill=THEME_COLOR,
                                                       width=280)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        correct_button_img = PhotoImage(file="./images/true.png")
        false_button_img = PhotoImage(file="./images/false.png")

        self.correct_button = Button(image=correct_button_img, highlightthickness=0, command=self.correct_button_click)
        self.correct_button.grid(row=2, column=0)

        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_button_click)
        self.false_button.grid(row=2, column=1)

        self.has_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_question, text=q_text)

    def correct_button_click(self):
        self.is_right(self.quiz.check_answer("true"))

    def false_button_click(self):
        self.is_right(self.quiz.check_answer("false"))

    def is_right(self, true_false):
        if true_false:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.has_next_question)

    def has_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.canvas_question, text="You reached end of the quiz.")
            self.false_button.config(state="disabled")
            self.correct_button.config(state="disabled")
