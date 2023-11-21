import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Radio
def create_list():
    return [i for i in range(1, 101)]

# Validation
def valid_name(entry_text):
    return all(char.isalpha() or char.isspace() for char in entry_text)


def valid_age(entry_text):
    return entry_text.isdigit()

# Submit
def submit():
    first_name = first_name_entry.get()
    middle_name = middle_name_entry.get()
    last_name = last_name_entry.get()
    age = age_selection.get()
    address = address_entry.get()
    sex = radiovar.get()

    if not all(valid_name(entry_text) for entry_text in (first_name, middle_name, last_name)):
        messagebox.showwarning("Error", "Name is invalid, please make sure it does not contain numbers or is blank.")
        return

    if any(not entry.get() for entry in (first_name_entry, middle_name_entry, last_name_entry, age_selection, address_entry)):
        messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
        return

    if radiovar.get() == "":
        messagebox.showerror("Incomplete Information", "Please fill in all fields.")
        return

    result = f"Good day, {first_name} {middle_name} {last_name}! You are {age} years old. You live in {address}."
    messagebox.showinfo("Submission successful", result)


# Cancel
def close_window():
    root.destroy()

# main_window

root = tk.Tk()
root.title("Personal Information")

# GUI_components

frame = tk.Frame(root)
frame.grid(row=0, column=0)

confirmation_frame = tk.LabelFrame(frame, font=('times new roman', 15))
confirmation_frame.grid(row=1, column=0, columnspan=4, sticky=tk.W+tk.E,)

form_frame = tk.LabelFrame(frame, text='Please Answer the Form Below', font=('times new roman', 15))
form_frame.grid(row=0, column=0, padx=3, pady=5)

first_name_label = tk.Label(form_frame, text='First Name:', font=('times new roman', 15))
first_name_label.grid(row=0, column=0, padx=3, pady=5)

middle_name_label = tk.Label(form_frame, text="Middle Name:", font=('times new roman', 15))
middle_name_label.grid(row=0, column=2, padx=3, pady=5)

last_name_label = tk.Label(form_frame, text='Last Name:', font=('times new roman', 15))
last_name_label.grid(row=0, column=4, padx=3, pady=5)

age_label = tk.Label(form_frame, text='Select Age:', font=('times new roman', 15))
age_label.grid(row=1, column=0, padx=3, pady=5)

gender_label = tk.Label(form_frame, text='Sex:', font=('times new roman', 15))
gender_label.grid(row=1, column=2, padx=3, pady=5)

address_label = tk.Label(form_frame, text='Address:', font=('times new roman', 15))
address_label.grid(row=2, column=0)

# Entries

first_name_entry = tk.Entry(form_frame)
first_name_entry.grid(row=0, column=1, padx=3, pady=5)

middle_name_entry = tk.Entry(form_frame)
middle_name_entry.grid(row=0, column=3, padx=3, pady=5)

last_name_entry = tk.Entry(form_frame)
last_name_entry.grid(row=0, column=5, padx=3, pady=5)

var = tk.StringVar()
age_selection = ttk.Combobox(form_frame, textvariable=var)
age_selection['values'] = create_list()
age_selection.grid(row=1, column=1)

radiovar = tk.StringVar()

radio_male = tk.Radiobutton(form_frame, variable=radiovar, text='Male', value='Male', font=('times new roman', 15))
radio_male.grid(row=1, column=3)

radio_female = tk.Radiobutton(form_frame, variable=radiovar, text='Female', value='Female', font=('times new roman', 15))
radio_female.grid(row=1, column=4)

radio_not = tk.Radiobutton(form_frame, variable=radiovar, text='Prefer not to say', value='Not', font=('times new roman', 15))
radio_not.grid(row=1, column=5)

address_entry = tk.Entry(form_frame)
address_entry.grid(row=2, column=1, columnspan=4, padx=5, pady=5, sticky=tk.W+tk.E, )

# buttons
submit_button = tk.Button(confirmation_frame, text="Confirm", command=submit)
submit_button.grid(row=0, column=0, padx=5, pady=5, sticky='news')

cancel_button = tk.Button(confirmation_frame, text='Cancel', command=close_window)
cancel_button.grid(row=0, column=1, padx=5, pady=5, sticky='news')


root.mainloop()
