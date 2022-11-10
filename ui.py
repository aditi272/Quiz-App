from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.label_score = Label(text="Score: 0", bg=THEME_COLOR,fg="#FFFFFF")
        self.label_score.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Trivia Quiz Question", fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"),width=280)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50,padx=50)

        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img,highlightthickness=0,bg=THEME_COLOR,command=self.true_pressed)
        self.right_button.grid(row=2,column=0)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)
        self.get_next_que()

        self.window.mainloop()

    def get_next_que(self):
        if self.quiz.still_has_questions():

           self.canvas.config(bg="white")
           self.label_score.config(text=f"Score: {self.quiz.score}")
           q_text = self.quiz.next_question()
           self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.false_button.config(state=DISABLED)
            self.right_button.config(state=DISABLED)
            self.canvas.itemconfig(self.question_text,text=f"You've have reached the end of the quiz.\nScore: {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))





    def false_pressed(self):
         self.give_feedback(self.quiz.check_answer("False"))



    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="#00D100")
        else:
             self.canvas.config(bg="#FF2E2E")
        self.window.after(1000,self.get_next_que)

