from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="New Text", font=('Arial', 26, "bold"))
my_label.grid(column = 0, row = 0)

# button
def button_cicked():
    my_label.config(text=(input.get()).title(), font=('Arial', 26, "bold"))

button = Button(text="Click me", command=button_cicked)
button.grid(column=1, row=1)
# new button
newButton = Button(text='mere ko v dabao')
newButton.grid(column=2, row=0)

# input
input = Entry(width=30)
input.grid(column=3,row=2)
input.get()





window.mainloop()