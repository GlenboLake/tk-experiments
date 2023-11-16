import tkinter as tk


class WouldYouRather(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        tk.Label(text='Would you rather...').pack()

        self.value_a = tk.StringVar(value='...fight 100 duck-sized horses?')
        self.value_b = tk.StringVar(value='...fight 1 horse-sized duck?')

        self.remarks = tk.StringVar()
        self.response = tk.Label(textvariable=self.remarks)
        self.response.pack(side='bottom')

        self.choice_a = tk.Button(textvariable=self.value_a)
        self.choice_a.pack(side='left')
        self.choice_a.bind('<Button-1>', self.snide_remarks)
        tk.Label(text='or').pack(side='left')
        self.choice_b = tk.Button(textvariable=self.value_b)
        self.choice_b.pack(side='left')
        self.choice_b.bind('<Button-1>', self.snide_remarks)

    def snide_remarks(self, event):
        if event.widget is self.choice_a:
            self.remarks.set('Protect your shins!')
        else:
            self.remarks.set('Distract it with apples!')


root = tk.Tk()
app = WouldYouRather(root)
app.mainloop()
