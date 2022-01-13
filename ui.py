from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
RED = "#FF333F"
GREEN = "#5EFF33"
BLACK = "#2B2B2B"
style_text = ('Arial', 18, 'italic')


class QuizUi():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('QuizzLer')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f'Score: {self.quiz.score}', fg=WHITE,bg=THEME_COLOR, font=style_text)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250,bg=WHITE, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 110, text='Hola Mundo', font=style_text, width=280, fill=BLACK)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_t = PhotoImage(file='./images/true.png')
        img_f = PhotoImage(file='./images/false.png')

        self.right = Button(image=img_t, highlightthickness=0, border=0, command=self.check_true)
        self.right.grid(column=0, row=2)

        self.wrong = Button(image=img_f, highlightthickness=0, border=0, command=self.check_false)
        self.wrong.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg=WHITE)
        self.canvas.itemconfig(self.question_text,fill=BLACK)

        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')    
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.!")
            self.right.config(state="disable")
            self.wrong.config(state="disable")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.itemconfig(self.question_text, fill=WHITE)
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.itemconfig(self.question_text, fill=WHITE)
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)
