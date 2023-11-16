import tkinter as tk


class WouldYouRather(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        tk.Label(text='Would you rather...').pack()

        self.remarks = tk.StringVar()
        self.response = tk.Label(textvariable=self.remarks)
        self.response.pack(side='bottom')

        self.a = tk.Button(text='...fight 100 duck-sized horses?')
        self.a.pack(side='left')
        tk.Label(text='or').pack(side='left')
        self.b = tk.Button(text='...fight 1 horse-sized duck?')
        self.b.pack(side='left')


root = tk.Tk()
app = WouldYouRather(root)
app.mainloop()
