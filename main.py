import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    new_password = "".join(password_list)
    password.insert(index=0, string=new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    user_website = website.get()
    user_email = email.get()
    user_password = password.get()
    new_data = {user_website: {"email": user_email,
                               "password": user_password}}

    if len(user_email) < 11 or len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Do not leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                json_data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new one
            json_data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(json_data, file, indent=4)
        finally:
            website.delete(0, "end")
            email.delete(0, len(email.get()) - 10)
            password.delete(0, "end")


def find_password():
    try:
        with open("data.json", "r") as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Oops",
                            message="No data file found")

    else:
        if website.get() in json_data.keys():
            messagebox.showinfo(title=f"{website.get()}",
                                message=f"Email: {json_data[website.get()]['email']} "
                                        f"\nPassword: {json_data[website.get()]['password']}")
        else:
            messagebox.showinfo(title=f"{website.get()}",
                                message=f"No details for the website exists.")


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

locker_file = tk.PhotoImage(file="logo.png")
locker = tk.Canvas(width=200, height=200, highlightthickness=0)
locker.create_image(100, 100, image=locker_file)
locker.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
website = tk.Entry(width=30)
website.grid(column=1, row=1)
website.focus()

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email = tk.Entry(width=49, justify="left")
email.grid(column=1, row=2, columnspan=2)
email.insert(index=0, string="@gmail.com")

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
password = tk.Entry(width=30)
password.grid(column=1, row=3)

password_button = tk.Button(text="Generate Password", width=15, background="yellow", command=generate_password)
password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, background="red", command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tk.Button(text="Search", width=15, background="green", command=find_password)
search_button.grid(column=2, row=1)

# ---------------------------- UI SETUP ------------------------------- #
window.mainloop()
