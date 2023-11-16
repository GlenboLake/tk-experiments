import random
import tkinter as tk


questions = [
    # Choice A, Remark A, Choice B, Remark B
    ('fight 100 duck-sized horses', 'Protect your shins!',
     'fight1 horse-sized duck', 'Distract it with apples!'),
    ("get A's and B's but learn nothing", 'Coward!',
     "get C's and D's but learn everything", 'I like your attitude.')
]


class WouldYouRather(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # Create variables that will be updated
        self.value_a = tk.StringVar()
        self.value_b = tk.StringVar()
        self.remarks = tk.StringVar()
        self.response_a = ''
        self.response_b = ''
        self.pick_next_question(None)

        # Set up layout
        tk.Label(text='Would you rather...').pack()

        # Put the buttons with the choices side-by-side; easiest to do with a frame
        question = tk.Frame()
        self.choice_a = tk.Button(master=question, textvariable=self.value_a)
        self.choice_a.pack(side='left')
        self.choice_a.bind('<Button-1>', self.snide_remarks)
        tk.Label(master=question, text='or').pack(side='left')
        self.choice_b = tk.Button(master=question, textvariable=self.value_b)
        self.choice_b.pack(side='left')
        self.choice_b.bind('<Button-1>', self.snide_remarks)
        question.pack()

        self.response = tk.Label(textvariable=self.remarks)
        self.response.pack()

        next_question = tk.Button(text='Next Question')
        next_question.bind('<Button-1>', self.pick_next_question)
        next_question.pack()

    def pick_next_question(self, event):
        a, self.response_a, b, self.response_b = random.choice(questions)
        self.value_a.set(a)
        self.value_b.set(b)
        self.remarks.set('')

    def snide_remarks(self, event):
        if event.widget is self.choice_a:
            self.remarks.set(self.response_a)
        else:
            self.remarks.set(self.response_b)


root = tk.Tk()
app = WouldYouRather(root)
app.mainloop()
