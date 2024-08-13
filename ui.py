THEME_COLOR = "#375362"
from tkinter import*
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text='Score:0', fg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas  = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text='Some Questioin text',
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'),
                                                     width=280


                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.right_button = Button(image=true_img,command=self.true_click)
        self.right_button.grid(column=0, row=2)

        false_img = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image= false_img, command=self.false_click)
        self.wrong_button.grid(column=1, row=2)


        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')



    def true_click(self):
        # is_right = self.quiz.check_answer('True')
        self.give_feedback(self.quiz.check_answer('True'))



    def false_click(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")

        else:
            self.canvas.config(bg='Red')

        self.window.after(1000, self.get_next_question)








