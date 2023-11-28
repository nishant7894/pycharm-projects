from tkinter import *

def miles_to_km():
    miles = eval(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result.config(text =f"{km}")

window = Tk()
window.title("Miles to Kilometre Converter")
window.minsize(width=200, height=100)

window.config(padx=20, pady=20)

miles_input= Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.config(padx=20, pady=20)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result = Label()
kilometer_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)











window.mainloop()

