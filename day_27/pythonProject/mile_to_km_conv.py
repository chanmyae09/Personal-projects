from tkinter import *

def convert():
    miles = float(miles_input.get())
    km = miles * 1.689
    km_result_label.config(text = km)


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width = 300, height = 100)
window.config(padx = 20, pady =20 )


miles_input = Entry(width = 7)

miles_input.grid(column = 1, row = 0)

my_label = Label(text = "is equal to ",font=("Arial", 15, ))
my_label.grid(column = 0, row = 1)


mile_label = Label(text = "Miles",font=("Arial", 15, ))
mile_label.grid(column = 2, row = 0)


km_label = Label(text = "Km",font=("Arial", 15, ))
km_label.grid(column = 2, row = 1)

km_result_label = Label(text = "0")
km_result_label.grid (column =1, row = 1)



calculate_button = Button(text = "Calculate", command = convert)
calculate_button.grid(row= 2, column = 1)












window.mainloop()