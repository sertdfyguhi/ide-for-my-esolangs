import tkinter as tk
import run

def plts():
    l = editor.get(0.0, tk.END).rsplit('\n', 1)
    result = run.pltsrun(''.join(l))
    editor.insert(tk.END, f'\n\nResult:\n\n{result}')

def ewpl():
    l = editor.get(0.0, tk.END).rsplit('\n', 1)
    result = run.ewplrun(''.join(l))
    editor.insert(tk.END, f'\n\nResult:\n\n{result}')

root = tk.Tk()
root.geometry('550x320')
menu = tk.Menu(root)
editor = tk.Text(master=root, width=1920, height=1080, bg='#333333', font=('Menlo', 20), highlightthickness=0, fg='#fff', undo=True, insertbackground='#ffffff')
editor.pack()
runmenu = tk.Menu(menu)
runmenu.add_command(label='Run ewpl', command=ewpl)
runmenu.add_command(label='Run plts', command=plts)
menu.add_cascade(label='Run', menu=runmenu)
root.config(menu=menu)
root.title('ide for my esolangs')
root.mainloop()