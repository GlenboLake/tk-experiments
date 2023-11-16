import tkinter as tk

window = tk.Tk()

tk.Label(text='Would you rather...').pack()

a = tk.Button(text='...fight 100 duck-sized horses?')
a.pack(side='left')
tk.Label(text='or').pack(side='left')
b = tk.Button(text='...fight 1 horse-sized duck?')
b.pack(side='left')

window.mainloop()