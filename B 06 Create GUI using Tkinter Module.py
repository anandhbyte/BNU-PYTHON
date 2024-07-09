import tkinter as tk
from tkinter import messagebox, ttk

def submit():
    messagebox.showinfo("Submitted", "Form submitted successfully.")

root = tk.Tk()
root.geometry("300x300")
root.title("Student Registration Form")

tk.Label(root, text="Student Name").grid(row=8)
tk.Label(root, text="Phone Number").grid(row=1)
tk.Label(root, text="Email Address").grid(row=2)
tk.Label(root, text="Residential Address").grid(row=3)
tk.Label(root, text="Gender").grid(row=4)
tk.Label(root, text="Course").grid(row=5)
tk.Label(root, text="Hobbies").grid(row=6)

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_text = tk.Text(root, width=20, height=5)

name_entry.grid(row=8, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_text.grid(row=3, column=1)

gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=4, column=1, sticky='w')
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=4, column=1, sticky='e')

course_var = tk.StringVar()
course_combobox = ttk.Combobox(root, textvariable=course_var)
course_combobox['values'] = ('BCA', 'BBA', 'BCOM')
course_combobox.grid(row=5, column=1)

hobbies = {"Singing": tk.BooleanVar(), "Reading": tk.BooleanVar(), "Sports": tk.BooleanVar()}
for idx, (hobby, var) in enumerate(hobbies.items()):
    tk.Checkbutton(root, text=hobby, variable=var).grid(row=6 + idx, column=1, sticky='w')

tk.Button(root, text="Submit", command=submit).grid(row=10, column=1)
root.mainloop()
