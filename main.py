from tkinter import *

window = Tk()
window.title("Python Password Manager")
window.config(pady=50, padx=50, bg="BLACK")
window.resizable(False, False)

# Canvas
new_canvas = Canvas(width=200, height=200, bg="BLACK", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
new_canvas.create_image(100, 100, image=logo_img)
new_canvas.grid(row=0, column=1, columnspan=2)

# Labels
website_label = Label(text="Website: ", bg="BLACK", fg="GRAY", font="Arial 12")
email_label = Label(text="Email/Username: ", bg="BLACK", fg="GRAY", font="Arial 12")
password_label = Label(text="Password: ", bg="BLACK", fg="GRAY", font="Arial 12")
website_label.grid(row=1, column=0, pady=(0, 10))
email_label.grid(row=2, column=0, pady=(0, 10))
password_label.grid(row=3, column=0, pady=(0, 10))

# Input
website_input = Entry(font="Arial 12")
website_input.grid(row=1, column=1, columnspan=2, sticky="WE", ipady=5, pady=(0, 10))
website_input.focus()
email_input = Entry(font="Arial 12")
email_input.grid(row=2, column=1, columnspan=2, sticky="EW", ipady=5, pady=(0, 10))
password_input = Entry(font="Arial 12")
password_input.grid(row=3, column=1, sticky="EW", pady=(0, 10), ipady=5, padx=(0, 10))
# Buttons
gen_pwd_btn = Button(text="Generate password", font="Arial 10")
gen_pwd_btn.grid(row=3, column=2, sticky="we", pady=(0, 10), ipady=2)
add_button = Button(text="Add", font="Arial 10", width=60)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", ipady=2)

window.mainloop()
