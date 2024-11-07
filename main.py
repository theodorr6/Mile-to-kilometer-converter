from tkinter import *

window = Tk()
window.title("My First GUI")
window.config(padx=25, pady=25)

# Labels

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

my_label2 = Label(text="is euqal to")
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0")
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km")
my_label4.grid(column=2, row=1)


# Buttons
def button_click():
    calculate = (int(input.get()) * 1.609)
    my_label3.config(text=f"{calculate}")


button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

# Entry
input = Entry(width=15)
input.grid(column=1, row=0)

window.mainloop()
