THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizzUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("quiz_api")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quote_text = self.canvas.create_text(150, 125, text="yxfcfcu uy fvtyfr /n cyttc Goes HERE", width=280, font=("Arial", 15, "bold"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        kanye_img = PhotoImage(file="true.png")
        kanye_img = kanye_img.subsample(2, 2)
        self.kanye_button = Button(image=kanye_img, highlightthickness=0, command=self.true_press)
        self.kanye_button.grid(row=2, column=0)

        kany_img = PhotoImage(file="false.png")
        kany_img = kany_img.subsample(2, 2)
        self.kanye_button = Button(image=kany_img, highlightthickness=0, command=self.false_press)
        self.kanye_button.grid(row=2, column=1)

        self.get_next_quiz()

        self.window.mainloop()

    def get_next_quiz(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions(): 
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text="the end")
            
    def true_press(self):
        self.fedback(self.quiz.check_answer("true"))

    def false_press(self):
        is_right = self.quiz.check_answer("false")
        self.fedback(is_right)

    def fedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_quiz)