from tkinter import *

def button_clicked():
    new_text = input_.get()
    my_label.config(text = new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height  = 300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text = "I Am a label",font=("Arial", 24, ))
my_label["text"] = "New Text"
my_label.config(text = "New Text")
my_label.grid(column = 0, row = 0)


# Button
button = Button(text = "Click Me", command= button_clicked)
button.grid(column = 1, row = 1)

new_button = Button(text = "New_Button", command= button_clicked)
new_button.grid(column = 2, row = 0)

# Entry
input_ = Entry(width = 10)
input_.get()
input_.grid(column = 3, row =3 )





window.mainloop()
